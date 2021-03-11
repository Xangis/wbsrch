from bs4 import BeautifulSoup, Comment, Doctype
from bs4.element import ProcessingInstruction
import urllib.request
import urllib.error
import urllib.parse
from urllib.parse import urlparse
import http.client
import time
from dir.models import CrawlableUrl, DomainInfo, PageIFrame, PageJavaScript, PageLink, RandomValue, SiteInfo
from dir.utils import AddError, CanCrawlUrl, CanReCrawlUrl, ClearErrors, GetRootUrl, GetSiteInfoModelFromLanguage, IsHtmlExtension, IsHtmlUrl, LogQueries, MakeRealUrl, NormalizeUrl, RemoveExtraSpaces
from dir.robots import GetRobotsFile, AllowedByRobots
from dir.exceptions import InvalidLanguageException
from dir.language import GetInfixLanguage, GetLanguageFromDomainExtension, GetUrlParameterLanguage
from django.db.utils import DatabaseError, DataError
from django.db import connection
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

import socket
import codecs


MAX_HTML_READ = 131072
MAX_HTML_SAVED = 16384
MAX_PAGETEXT_SAVED = 16384


def html_decode(s):
    """
    Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>.
    """
    htmlCodes = (
        ("'", '&#39;'),
        ('"', '&quot;'),
        ('>', '&gt;'),
        ('<', '&lt;'),
        ('&', '&amp;')
    )
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s


def Crawler(options):
    pendinglinks = []
    if options['justthisurl']:
        CrawlSingleUrl(options['justthisurl'])
    elif options['pending']:
        QueryPendingUrls(pendinglinks, options['maxurls'], options['offset'], options['language'], options['descriptive'], options['random'], entiredomain=options['entiredomain'])
    elif options['doctyperecrawl']:
        RecrawlDoctypeUrls(pendinglinks, options['maxurls'], options['offset'], options['language'], options['descriptive'])
    elif options['xmlfix']:
        RecrawlXmlUrls(pendinglinks, options['maxurls'], options['offset'], options['language'], options['descriptive'], seconds=options['seconds'])
    elif options['recrawl']:
        RecrawlOldUrls(pendinglinks, options['maxurls'], options['offset'], options['language'], options['descriptive'], seconds=options['seconds'], entiredomain=options['entiredomain'])
    # Put doctype recrawl lines here.
    elif options['file']:
        # File mode implies recrawl is not OK. Since there's no combined setting, you'll have to swap these to recrawl file URLs.
        options['recrawl'] = False
        LoadUrlsFromFile(pendinglinks, options['file'], options['descriptive'], seconds=options['seconds'])
    else:
        print("You didn't give me anything to do. I'm done doing that nothing you asked for.")
        return
    if options['noop']:
        print('These are the URLs that would be crawled:')
        for item in pendinglinks:
            print(item)
        return
    Crawl(pendinglinks, options['maxurls'], options['seconds'], options['descriptive'], options['recrawl'])


def GetSiteInfoModelFromURL(url, descriptive=False):
    rooturl = GetRootUrl(url)
    try:
        domain = DomainInfo.objects.get(url=rooturl)
        if domain.uses_language_subdirs:
            language = GetInfixLanguage(url, descriptive)
            if descriptive and language:
                print('GetSiteInfoModelFromURL: Subdir language is {0}'.format(language))
            if not language and domain.language_association:
                language = domain.language_association
                print('GetSiteInfoModelFromURL: No Subdir language, defaulting to {0}'.format(language))
            if language and language != 'en':
                site_model = GetSiteInfoModelFromLanguage(language)
            else:
                site_model = GetSiteInfoModelFromLanguage('en')
        elif domain.uses_language_query_parameter:
            language = GetUrlParameterLanguage(url)
            if not language and domain.language_association:
                language = domain.language_association
            if descriptive and language:
                print('GetSiteInfoModelFromURL: URL Parameter language is {0}'.format(language))
            if language and language != 'en':
                site_model = GetSiteInfoModelFromLanguage(language)
            else:
                site_model = GetSiteInfoModelFromLanguage('en')
        elif domain.language_association:
            if descriptive:
                print('GetSiteInfoModelFromURL: Domain language is {0}'.format(domain.language_association))
            site_model = GetSiteInfoModelFromLanguage(domain.language_association)
        else:
            extlang = GetLanguageFromDomainExtension(rooturl)
            if descriptive:
                print('GetSiteInfoModelFromURL: Extlang is: {0}'.format(extlang))
            if extlang:
                site_model = GetSiteInfoModelFromLanguage(extlang)
            else:
                site_model = GetSiteInfoModelFromLanguage('en')
    except ObjectDoesNotExist:
        site_model = GetSiteInfoModelFromLanguage('en')
    return site_model


def PopulateSiteInfoFromHtml(siteinfo, html, descriptive=False):
    """
    Populates a SiteInfo object from HTML. When parsing the HTML, also creates
    and saves any IFrame and JavaScript objects. Does not save PageLink objects.
    """
    soup = BeautifulSoup(html, features="html.parser")
    if soup.title:
        try:
            siteinfo.pagetitle = RemoveExtraSpaces(html_decode(soup.title.string).strip()[0:255])
            if descriptive:
                print('Title: {0}'.format(siteinfo.pagetitle))
        except Exception:
            pass
    if descriptive:
        print('Root URL: {0}'.format(siteinfo.rooturl))
    description = soup.findAll(attrs={'name': 'description'})
    if len(description) > 0:
        try:
            siteinfo.pagedescription = RemoveExtraSpaces(html_decode(description[0]['content'].strip())[0:319])
            if descriptive:
                print('Description: {0}'.format(siteinfo.pagedescription))
        except Exception:
            pass
    keywords = soup.findAll(attrs={'name': 'keywords'})
    if len(keywords) > 0:
        try:
            siteinfo.pagekeywords = RemoveExtraSpaces(keywords[0]['content'].strip()[0:255].lower())
            if descriptive:
                print('Keywords: {0}'.format(siteinfo.pagekeywords))
        except Exception:
            pass
    try:
        # We don't actually store the canonical link anywhere, but we could if we wanted to.
        canonicallinks = soup.findAll('link', rel='canonical')
        for canonical in canonicallinks:
            print('Canonical link found: {0}'.format(canonical['href']))
    except Exception:
        pass
    headtags = soup.findAll('h1')
    if len(headtags) > 0:
        siteinfo.pagefirstheadtag = RemoveExtraSpaces(headtags[0].text.strip()[0:255])
    secondaryheadtags = soup.findAll('h2')
    if len(secondaryheadtags) > 0:
        siteinfo.pagefirsth2tag = RemoveExtraSpaces(secondaryheadtags[0].text.strip()[0:255])
    tertiaryheadtags = soup.findAll('h3')
    if len(tertiaryheadtags) > 0:
        siteinfo.pagefirsth3tag = RemoveExtraSpaces(tertiaryheadtags[0].text.strip()[0:255])
    iframes = soup.findAll('iframe')
    siteinfo.num_iframes = len(iframes)
    if descriptive:
        print('Num Iframes: {0}'.format(siteinfo.num_iframes))
    for iframe in iframes:
        if descriptive:
            print('IFrame: {0}'.format(iframe))
        src = iframe.attrs.get('src', None)
        if src:
            frame = PageIFrame()
            frame.rooturl_source = siteinfo.rooturl
            frame.url_source = siteinfo.url
            if src.startswith('http:') or src.startswith('https:'):
                frame.url_destination = src[0:2048]
                frame.rooturl_destination = GetRootUrl(src)
            elif src.startswith('//'):
                if frame.url_source.startswith('https'):
                    frame.url_destination = ('https:' + src)[0:2048]
                    frame.rooturl_destination = GetRootUrl(frame.url_destination)
                else:
                    frame.url_destination = ('http:' + src)[0:2048]
                    frame.rooturl_destination = GetRootUrl(frame.url_destination)
            else:
                if frame.url_source.startswith('https'):
                    frame.url_destination = ('https://' + frame.rooturl_destination + src)[0:2048]
                    frame.rooturl_destination = GetRootUrl(src)
                else:
                    frame.url_destination = ('http://' + frame.rooturl_destination + src)[0:2048]
                    frame.rooturl_destination = frame.rooturl_source
            frame.save()
            if descriptive:
                print('PageIFrame: rooturl_source = {0}, rooturl_destination = {1}, url_source = {2}, url_destination = {3}'.format(
                    frame.rooturl_source, frame.rooturl_destination, frame.url_source, frame.url_destination))
    audios = soup.findAll('audio')
    siteinfo.num_audio_tags = len(audios)
    if descriptive:
        print('Num Audio Tags: {0}'.format(siteinfo.num_audio_tags))
    videos = soup.findAll('video')
    siteinfo.num_video_tags = len(videos)
    if descriptive:
        print('Num Video Tags: {0}'.format(siteinfo.num_video_tags))
    svgs = soup.findAll('svg')
    siteinfo.num_svg_tags = len(svgs)
    if descriptive:
        print('Num svg Tags: {0}'.format(siteinfo.num_svg_tags))
    canvass = soup.findAll('canvas')
    siteinfo.num_canvas_tags = len(canvass)
    if descriptive:
        print('Num canvas Tags: {0}'.format(siteinfo.num_canvas_tags))
    images = soup.findAll('img')
    siteinfo.num_images = len(images)
    if descriptive:
        print('Num Images: {0}'.format(siteinfo.num_images))
    # Get image titles, URLs, and filenames.
    image_alt_tags = []
    image_title_tags = []
    image_filenames = []
    for img in images:
        if img.attrs.get('alt', None):
            image_alt_tags.append(img.attrs.get('alt'))
        else:
            pass
        if img.attrs.get('title', None):
            image_title_tags.append(img.attrs.get('title'))
        if img.attrs.get('src', None):
            imgsrc = img.attrs.get('src')
            fname = imgsrc.split('/')[-1]
            image_filenames.append(fname)
    siteinfo.image_alt_tags = ', '.join(image_alt_tags)
    siteinfo.image_title_tags = ', '.join(image_title_tags)
    siteinfo.image_filenames = ', '.join(image_filenames)
    links = soup.findAll('link')
    num_stylesheets = 0
    canonical = False
    for link in links:
        rel = link.attrs.get('rel', None)
        if rel and rel[0].lower() == 'stylesheet':
            num_stylesheets += 1
        elif rel and rel[0].lower() == 'canonical':
            canonical = True
    if descriptive:
        print('Total Links: {0}, Total Stylesheets: {1}, Canonical Link: {2}'.format(len(links), num_stylesheets, canonical))
    siteinfo.num_css_files = num_stylesheets
    scripts = soup.findAll('script')
    num_external_scripts = 0
    for script in scripts:
        script.attrs.get('type', None)
        src = script.attrs.get('src', None)
        if src:
            num_external_scripts += 1
            pjs = PageJavaScript()
            pjs.rooturl_source = siteinfo.rooturl
            pjs.url_source = siteinfo.url
            if src.startswith('http:') or src.startswith('https:'):
                pjs.rooturl_destination = GetRootUrl(src)
                pjs.url_destination = src[0:2048]
            elif src.startswith('//'):
                if pjs.url_source.startswith('https'):
                    pjs.url_destination = ('https:' + src)[0:2048]
                    pjs.rooturl_destination = GetRootUrl(pjs.url_destination)
                else:
                    pjs.url_destination = ('http:' + src)[0:2048]
                    pjs.rooturl_destination = GetRootUrl(pjs.url_destination)
            else:
                if pjs.url_source.startswith('https'):
                    pjs.rooturl_destination = pjs.rooturl_source
                    pjs.url_destination = ('https://' + pjs.rooturl_destination + src)[0:2048]
                else:
                    pjs.rooturl_destination = pjs.rooturl_source
                    pjs.url_destination = ('http://' + pjs.rooturl_destination + src)[0:2048]
            fname = pjs.url_destination.split('/')[-1]
            if fname:
                pjs.filename = fname[0:255]
            if descriptive:
                print('PageJavaScript: rooturl_source = {0}, rooturl_destination = {1}, url_source = {2}, url_destination = {3}, filename = {4}'.format(
                    pjs.rooturl_source, pjs.rooturl_destination, pjs.url_source, pjs.url_destination, pjs.filename))
            pjs.save()
    siteinfo.num_javascripts = num_external_scripts
    if descriptive:
        print('Num Scripts: {0}, Total Script Links (num_javascripts): {1}'.format(len(scripts), num_external_scripts))

    try:
        if not siteinfo.pagesize:
            sitehtml = str(soup)
            siteinfo.pagesize = len(sitehtml)
            if descriptive:
                print('No page size from host. Using HTML size. Will be inaccurate if page is larger than buffer.')
    except RuntimeError:
        print('Received a RuntimeError getting site HTML from BeautifulSoup. This is probably an infinite recursion error.')
    # Remove script and style tags for cleaner text.
    [item.extract() for item in soup.contents if isinstance(item, Doctype)]
    [s.extract() for s in soup(['script', 'style', 'head'])]
    # Remove comment tags for cleaner text.
    comments = soup.findAll(text=lambda text: isinstance(text, Comment))
    [comment.extract() for comment in comments]
    for item in soup:
        if isinstance(item, ProcessingInstruction):
            print('Removing {0}'.format(item))
            item.extract()
            break
    text = ' '.join(soup.findAll(text=True))
    text = RemoveExtraSpaces(text)
    if len(text) < MAX_PAGETEXT_SAVED:
        siteinfo.pagetext = text
    else:
        siteinfo.pagetext = text[0:MAX_PAGETEXT_SAVED]
    siteinfo.lastcrawled = timezone.now()
    return soup


def ParseHtml(pendinglinks, url, response, descriptive=False, recrawl=False):
    # By not reading the entire page we save some bandwidth, but we also truncate links at
    # the bottom of a page and fail to find them. This means that the footers of large pages
    # are effectively invisible to us. This may or may not ever be a problem.
    html = response.read(MAX_HTML_READ)
    realurl = response.geturl()
    ipaddr = None
    print('Real URL is: {0}'.format(realurl))
    normaled = NormalizeUrl(realurl, post_crawl_replacement=True)
    if normaled != realurl:
        try:
            print('URL Normalized to {0}'.format(normaled))
        except Exception:
            pass
        realurl = normaled
    try:
        ipaddr = socket.gethostbyname(urlparse(realurl).hostname)
        if descriptive:
            print('IP Address is: {0}'.format(ipaddr))
    except Exception:
        pass
    if (not recrawl and not CanCrawlUrl(realurl)) or (recrawl and not CanReCrawlUrl(realurl, descriptive)):
        if descriptive:
            print('Not saving URL because it is blocked or not HTML: {0}'.format(realurl))
        RemoveFromPending(pendinglinks, realurl)
        RemoveFromPending(pendinglinks, url)
        # This is problematic in that we'll remove URLs that are maxed out down to the
        # point that we can add a new URL for that maxed site, at which point we'll add one
        # and then get blocked and start removing them again. This will result in a lot of
        # URL churn, but might be desired behavior because it'll prevent us from keeping
        # too many stale, aging URLs from a maxed-out site without refreshing them.
        # The problem comes when we remove the root URL for a site, though it will be
        # re-added more frequently since URLs tend to point to their root. We'll leave it
        # be for now and see what happens.
        if recrawl:
            count = RemoveFromDatabase(realurl, descriptive, all_languages=True)
            print('Removed {0} instances of {1} from the database.'.format(count, realurl))
            remove_model = GetSiteInfoModelFromURL(url, descriptive)
            count = RemoveFromDatabase(url, descriptive, all_languages=True, model=remove_model)
            print('Removed {0} instances of {1} from the {2} database.'.format(count, url, remove_model))
        return False
    rooturl = GetRootUrl(realurl)
    # We may have been redirected to a URL that isn't in the DomainInfo table yet.
    # Make sure it is.
    try:
        domain = DomainInfo.objects.get(url=rooturl)
    except ObjectDoesNotExist:
        domain = DomainInfo()
        domain.url = rooturl
        if '.' in rooturl:
            domain.save()
        try:
            print('Created new DomainInfo entry for {0}.'.format(rooturl))
        except Exception:
            print('Created new DomainInfo entry.')
    # We need to check the real root url for blocking too. We do this in addition to
    # when we add to the pending list because we may have received something different
    # due to a redirect and we don't want to save it.
    info = None
    try:
        site_model = GetSiteInfoModelFromURL(realurl, descriptive)
    except InvalidLanguageException as e:
        print('InvalidLanguageException: {0} (not saving page)'.format(e))
        # If we're re-crawling, then we need to remove the old page. The only place we can
        # realistically remove it from is SiteInfo.
        if recrawl:
            count = RemoveFromDatabase(realurl, descriptive, all_languages=True, model=SiteInfo)
            print('Removed {0} instances of invalid language page {1} from the {2} database.'.format(count, realurl, SiteInfo))
        return False
    info = site_model()
    info.rooturl = rooturl
    info.url = realurl
    if ipaddr:
        info.ip = ipaddr
    if descriptive:
        print('URL: {0}'.format(info.url))
        print('Using language table {0}'.format(site_model))

    # Get Headers
    # Content-Length may not always be reliable, or present. In addition,
    # if we don't get the content length, our length will cap out at 40000,
    # since that's all we read.
    try:
        length = int(response.headers["Content-Length"])
        if descriptive:
            print('Content-Length: {0}'.format(length))
        if length > 0:
            info.pagesize = length
    except Exception:
        pass
    server_header = response.headers.get('server', None)
    content_type_header = response.headers.get('content-type', None)
    if server_header:
        info.server_header = server_header[0:100]
        if descriptive:
            print('Server: {0}'.format(server_header))
    if content_type_header:
        info.content_type_header = content_type_header[0:100]
        if descriptive:
            print('Content-Type: {0}'.format(content_type_header))

    if realurl != url:
        if descriptive:
            print('Requested URL: {0}, Actual URL: {1}'.format(url, realurl))
        # If something redirects somewhere else, we should make sure that the URL
        # that does the redirecting is not in the database.
        remove_model = GetSiteInfoModelFromURL(url, descriptive)
        print('Removing {0} from the database with model {1}'.format(url, remove_model))
        count = RemoveFromDatabase(url, descriptive, all_languages=True, model=remove_model)
        print('Removed {0} instances of {1} from the database.'.format(count, url))
        RemoveFromPending(pendinglinks, url)
    # Clear out old iframes and javascripts.
    # We have to do this before calling PopulateSiteInfoFromHtml because
    # that creates the PageIFrame and PageJavaScript objects. There will be
    # churn every time we recrawl a URL, but the alternative is having old links and
    # iframes build up as the page changes when they aren't on the current
    # version of the page..
    elinks = PageIFrame.objects.filter(url_source=info.url)
    if descriptive:
        print('Deleting {0} existing IFrames.'.format(elinks.count()))
    for elink in elinks:
        elink.delete()
    elinks = PageJavaScript.objects.filter(url_source=info.url)
    if descriptive:
        print('Deleting {0} existing JavaScripts.'.format(elinks.count()))
    for elink in elinks:
        elink.delete()
    elinks = PageLink.objects.filter(url_source=info.url)
    if descriptive:
        print('Deleting {0} existing links.'.format(elinks.count()))
    for elink in elinks:
        elink.delete()

    try:
        soup = PopulateSiteInfoFromHtml(info, html, descriptive)
    except html.parser.HTMLParseError as e:
        RemoveFromPending(pendinglinks, realurl)
        print('HTMLParseError: {0}.'.format(e))
        return False
    try:
        previous = site_model.objects.get(url=realurl)
        if descriptive and not recrawl:
            print('URL already crawled, not saving: {0}'.format(realurl))
        elif recrawl:
            if descriptive:
                print('Updating existing URL in database: {0}'.format(realurl))
            # TODO: See if this and CopySiteData are duplicate code. They probably are.
            previous.pagesize = info.pagesize
            previous.pagedescription = info.pagedescription
            previous.pagekeywords = info.pagekeywords
            previous.pagetext = info.pagetext
            previous.pagetitle = info.pagetitle
            previous.pagefirstheadtag = info.pagefirstheadtag
            previous.pagefirsth2tag = info.pagefirsth2tag
            previous.pagefirsth3tag = info.pagefirsth3tag
            previous.lastcrawled = info.lastcrawled
            previous.rooturl = info.rooturl
            previous.ip = info.ip
            previous.server_header = info.server_header
            previous.content_type_header = info.content_type_header
            previous.num_iframes = info.num_iframes
            previous.num_javascripts = info.num_javascripts
            previous.num_images = info.num_images
            previous.num_css_files = info.num_css_files
            previous.num_video_tags = info.num_video_tags
            previous.num_audio_tags = info.num_audio_tags
            previous.num_svg_tags = info.num_svg_tags
            previous.num_canvas_tags = info.num_canvas_tags
            previous.image_alt_tags = info.image_alt_tags
            previous.image_title_tags = info.image_title_tags
            previous.image_filenames = info.image_filenames
            if not previous.firstcrawled:
                previous.firstcrawled = previous.lastcrawled
            previous.save()
            ClearErrors(previous)
            # Make sure there's not a copy of this URL in the English database
            # if it's tagged as non-English. This causes us to avoid duplication,
            # and to self-move URLs that were not moved when the domain/url was
            # tagged as that language.
            english_model = GetSiteInfoModelFromLanguage('en')
            if site_model != english_model:
                try:
                    oldsite = SiteInfo.objects.get(url=realurl)
                    print('Deleting URL from en table for site tagged as non-English')
                    oldsite.delete()
                except ObjectDoesNotExist:
                    pass
    except Exception:
        try:
            if not info.firstcrawled:
                info.firstcrawled = info.lastcrawled
            info.save()
            ClearErrors(info)
        except UnicodeDecodeError:
            # Don't save errors with unicode fails. They won't be pages with
            # a Roman alphabet anyhow.
            pass
        except DatabaseError:
            print('Failed to save URL: {0}'.format(info.url))
            connection._rollback()
    RemoveFromPending(pendinglinks, url)
    RemoveFromPending(pendinglinks, realurl)
    # Add pending links and URL links.
    for link in soup.find_all('a'):
        hr = link.get('href')
        if hr:
            if IsHtmlUrl(hr):
                # prehr = hr
                if realurl.startswith('https:'):
                    hr = MakeRealUrl(hr, rooturl, secure=True)
                else:
                    hr = MakeRealUrl(hr, rooturl)
                # print('MAKEREALURL: {0} IS NOW {1} WITH ROOT URL {2}'.format(prehr, hr, rooturl))
                destroot = GetRootUrl(hr)
                if destroot and destroot != rooturl and '.' in destroot and destroot != '.' and not IsHtmlExtension(destroot):
                    try:
                        PageLink.objects.get(url_source=info.url, url_destination=hr)
                    except ObjectDoesNotExist:
                        ulink = PageLink()
                        ulink.rooturl_source = rooturl
                        ulink.url_source = info.url
                        ulink.url_destination = hr
                        ulink.rooturl_destination = destroot
                        try:
                            title = link.contents[0]
                            if title:
                                ulink.anchor_text = RemoveExtraSpaces(str(title))[0:255]
                        except IndexError:
                            pass
                        try:
                            ulink.save()
                        except DataError as e:
                            # We can get this if a root url is too log (>260 chars) or full URL is too long (>2048 chars)
                            connection._rollback()
                            print('Problem saving PageLink: {0}'.format(e))
                        if descriptive:
                            print('Added link from {0} to {1} with anchor {2}'.format(ulink.url_source, ulink.url_destination, ulink.anchor_text))
                AddPendingLink(pendinglinks, hr, info.rooturl, descriptive, recrawl=recrawl)
    return True


def AddPendingLink(pendinglinks, url, root=None, descriptive=False, recrawl=False):
    # Fix up prefix.
    if url is None:
        return
    # Remove leading and trailing whitespac if necessary.
    url = url.strip()
    if len(url) > 2048:
        if descriptive:
            print('Url too long to be valid (>2048): {0}'.format(url))
        return
    if not IsHtmlUrl(url):
        return
    # Normalize URL. MakeRealUrl calls NormalizeUrl.
    origurl = url
    try:
        url = MakeRealUrl(url, root)
    except UnicodeEncodeError:
        print('URL is not valid (UnicodeEncodeError). Cannot crawl.')
        if recrawl:
            remove_model = GetSiteInfoModelFromURL(url, descriptive)
            print('Removing invalid URL from the {0} database.'.format(remove_model))
            count = RemoveFromDatabase(url, descriptive, all_languages=True, model=remove_model)
            print('Removed {0} instances of the url {1} from the database.'.format(count, origurl))
        return
    if origurl != url:
        if descriptive:
            print('URL {0} normalized to {1}'.format(origurl, url))
        RemoveFromPending(pendinglinks, origurl)
        if recrawl:
            # Delete previous url because we'll never save it in that format.
            print('Removing pre-normalized URL {0} from the database.'.format(origurl))
            remove_model = GetSiteInfoModelFromURL(origurl, descriptive)
            count = RemoveFromDatabase(origurl, descriptive, all_languages=True, model=remove_model)
            try:
                print('Removed {0} instances of {1} from the database.'.format(count, origurl))
            except Exception:
                print('Removed {0} instances of the url {1} from the database.'.format(count, origurl))
    # Prevent crawling excluded sites, non-HTML, and at-url-limit sites.
    if not recrawl and not CanCrawlUrl(url):
        if descriptive:
            print('Not crawling URL because it is blocked or not HTML: {0}'.format(url))
        RemoveFromPending(pendinglinks, url)
        return
    elif recrawl and not CanReCrawlUrl(url, descriptive):
        if descriptive:
            print('Not recrawling URL because it is blocked or not HTML: {0}'.format(url))
        RemoveFromPending(pendinglinks, url)
        try:
            print('Removing blocked site URL {0} from the database.'.format(url))
            remove_model = GetSiteInfoModelFromURL(origurl, descriptive)
            count = RemoveFromDatabase(url, descriptive, all_languages=True, model=remove_model)
            try:
                print('Removed {0} instances of {1} from the database.'.format(count, url))
            except Exception:
                print('Removed {0} instances of the url {1} from the database.'.format(count, url))
        except ObjectDoesNotExist:
            pass
        return
    if not recrawl:
        try:
            site_model = GetSiteInfoModelFromURL(url, descriptive)
            site_model.objects.get(url=url)
            if descriptive:
                print('URL in DB, non recrawl mode, skip add to pending: {0}'.format(url))
            RemoveFromPending(pendinglinks, url)
            return
        except Exception:
            pass
    if url in pendinglinks:
        return
    if descriptive:
        try:
            print('Add Pending Link: {0}'.format(url))
        except Exception:
            pass
    pendinglinks.append(url)


def SavePendingUrls(pendinglinks, descriptive=False):
    numpendingadded = 0
    for url in pendinglinks:
        rooturl = GetRootUrl(url)
        # Don't save links with a bad rooturl.
        if ('.' not in rooturl) or ('.' not in url) or (' ' in rooturl):
            continue
        lang = 'en'
        try:
            domain = DomainInfo.objects.get(url=rooturl)
            if domain.language_association:
                lang = domain.language_association
        except Exception:
            pass
        # Never save links where we have existing site info.
        #
        # TODO: Check other languages.
        site_model = GetSiteInfoModelFromLanguage(lang)
        try:
            site_model.objects.get(url=url)
            continue
        except ObjectDoesNotExist:
            pass
        try:
            CrawlableUrl.objects.get(url=url)
        except ObjectDoesNotExist:
            pending = CrawlableUrl()
            pending.url = url
            pending.rooturl = rooturl
            try:
                pending.save()
                if descriptive:
                    try:
                        print('Added pending URL to database: {0}'.format(url))
                    except Exception:
                        print('Added a pending URL to the database.')
            except DatabaseError:
                connection._rollback()
            numpendingadded = numpendingadded + 1
    print('{0} URLs were added to the pending URL table.'.format(numpendingadded))


def RemoveFromPending(pendinglinks, url):
    try:
        if url in pendinglinks:
            pendinglinks.remove(url)
        existing = CrawlableUrl.objects.get(url=url)
        existing.delete()
        return True
    except Exception:
        return False


def RemoveFromDatabase(url, descriptive=False, all_languages=True, model=None):
    # TODO: Remove from all tables for language infix domains.
    removed = 0
    if model:
        try:
            info = model.objects.get(url=url)
            info.delete()
            removed = removed + 1
            if descriptive:
                print('{0} deleted from {1}'.format(url, model))
        except ObjectDoesNotExist:
            pass
    try:
        rooturl = GetRootUrl(url)
        domain = DomainInfo.objects.get(url=rooturl)
        language = domain.language_association
    except Exception:
        language = 'en'
    try:
        site_model = GetSiteInfoModelFromLanguage(language)
        existing = site_model.objects.get(url=url)
        existing.delete()
        removed = removed + 1
        if descriptive:
            print('URL deleted from {0} database: {1}'.format(language, url))
    except Exception:
        site_model = None
        pass
    # For now, all languages just means delete if from english *and* tagged language.
    if all_languages:
        english_model = GetSiteInfoModelFromLanguage('en')
        if english_model != site_model:
            try:
                existing = english_model.objects.get(url=url)
                existing.delete()
                removed = removed + 1
                print('URL deleted from en database: {0}'.format(url))
            except Exception:
                pass

    # Remove all links from all link tables (JavaScript, Iframe, PageLink).
    links = PageLink.objects.filter(url_source=url)
    num = len(links)
    if num > 0:
        print('Deleting {0} PageLink items for {1}'.format(num, url))
        links.delete()
    links = PageIFrame.objects.filter(url_source=url)
    num = len(links)
    if num > 0:
        print('Deleting {0} PageIFrame items for {1}'.format(num, url))
        links.delete()
    links = PageJavaScript.objects.filter(url_source=url)
    num = len(links)
    if num > 0:
        print('Deleting {0} PageJavaScript items for {1}'.format(num, url))
        links.delete()

    return removed


def CrawlPage(pendinglinks, url, descriptive=False, recrawl=False):
    try:
        root = GetRootUrl(url)
        domain = DomainInfo.objects.get(url=root)
    except ObjectDoesNotExist:
        # Always create domain info and check for robots.txt even if the domain doesn't exist yet.
        domain = DomainInfo()
        domain.url = root
        if '.' in root:
            domain.save()
        try:
            print('Created new DomainInfo entry for {0}.'.format(root))
        except Exception:
            print('Created new DomainInfo entry.')
    if domain.robots_last_updated is None:
        print('Robots file never checked for database {0}, retrieving now.'.format(root))
        try:
            GetRobotsFile(domain)
        except Exception as e:
            print('Could not get robots file. Acting as if no robots file exists. Exception: {0}'.format(e))
        if not AllowedByRobots(url, domain):
            print('This URL is blocked by the robots.txt file.')
            RemoveFromPending(pendinglinks, url)
            if recrawl:
                count = RemoveFromDatabase(url, descriptive)
                if count > 0:
                    print('Removed {0} instances of {1} from the database.'.format(count, url))
            return False
    try:
        print('Retrieving {0}'.format(url))
    except Exception:
        print('Retrieving URL')
    req = urllib.request.Request(url)
    req.add_header('User-agent', 'Mozilla/5.0 (compatible; WbSrch/1.2 +https://wbsrch.com)')
    try:
        response = urllib.request.urlopen(req, timeout=20)
        if ParseHtml(pendinglinks, url, response, descriptive, recrawl):
            return True
        else:
            if descriptive:
                print('Failed to parse HTML.')
            return False
    except urllib.error.HTTPError as e:
        # 4XX errors are immediately fatal and we remove the URL.
        if e.code == 404 or e.code == 403 or e.code == 401 or e.code == 400 or e.code == 410 or e.code == 406:
            if descriptive:
                print('HTTP Error: {0}'.format(e.code))
            RemoveFromPending(pendinglinks, url)
            if recrawl:
                remove_model = GetSiteInfoModelFromURL(url, descriptive)
                count = RemoveFromDatabase(url, descriptive, model=remove_model)
                print('Removed {0} instances of {1} from the database.'.format(count, url))
            return False
        elif e.code == 302:
            try:
                print('HTTP Error: {0} - {1}'.format(e.code, e.reason))
            except Exception:
                print('302 Redirect.')
            if recrawl:
                try:
                    # Regular 302 errors are handled normally and transparenty by the
                    # BeautifulSoup library. It's only fatal 302 errors that will reach
                    # this code block. Those errors will be infinite redirect loop errors.
                    site_model = GetSiteInfoModelFromURL(url)
                    info = site_model.objects.get(url=url)
                    AddError(info, str(e.code), 'HTTP Error {0} - {1}'.format(e.code, e.reason))
                except Exception:
                    pass
                # May want to return False in all cases, not just recrawl.
                return False
        # For recrawling a 500-series error, log an error. If we consistently get them, the URL will delete itself.
        elif e.code == 503 or e.code == 502 or e.code == 500 or e.code == 504 or e.code == 501:
            try:
                print('HTTP Error: {0} - {1}'.format(e.code, e.reason))
            except Exception:
                print('HTTP Error (unprintable)')
            try:
                site_model = GetSiteInfoModelFromURL(url)
                info = site_model.objects.get(url=url)
                AddError(info, str(e.code), 'HTTP Error {0}'.format(e.code))
            except Exception:
                pass
        else:
            print('HTTP Error: {0} - {1}'.format(e.code, e.reason))
            if recrawl:
                try:
                    site_model = GetSiteInfoModelFromURL(url)
                    info = site_model.objects.get(url=url)
                    AddError(info, str(e.code), 'HTTP Error {0}'.format(e.code))
                except Exception:
                    pass
    except urllib.error.URLError as e:
        print('Unable to crawl URL {0}: urllib2.URLError is {1}'.format(url, e.args))
        RemoveFromPending(pendinglinks, url)
        if isinstance(e.args, tuple):
            if descriptive:
                print('Error: {0} [{1}]'.format(e.args[0], type(e.args[0])))
            if isinstance(e.args[0], socket.timeout):
                print('Timed out retrieving URL: {0}'.format(url))
                RemoveFromPending(pendinglinks, url)
                if recrawl:
                    try:
                        site_model = GetSiteInfoModelFromURL(url)
                        print('Logging Error to {0}'.format(site_model))
                        info = site_model.objects.get(url=url)
                        AddError(info, "socket.timeout", 'Timed out Retrieving URL')
                    except ObjectDoesNotExist:
                        pass
                return False
            if isinstance(e.args[0], socket.gaierror):
                print('This is a socket.gaierror - Error: {0}, Message: {1}'.format(e.args[0].errno, e.args[0].strerror))
                # A DNS lookup failure means we should remove it from the database.
                if e.args[0].errno == -2 and recrawl:
                    print('Removing this URL from the database.')
                    count = RemoveFromDatabase(url, descriptive)
                    print('Removed {0} instances of {1} from the database.'.format(count, url))
        if recrawl:
            try:
                site_model = GetSiteInfoModelFromURL(url)
                info = site_model.objects.get(url=url)
                AddError(info, "urllib2.URLError", 'e.args: {0} ({1}) [{2}] '.format(e.args[0], type(e.args[0]), dir(e.args[0])))
            except ObjectDoesNotExist:
                pass
        return False
    except socket.timeout as e:
        print('Timed out retrieving URL: {0} - {1}'.format(url, e))
        RemoveFromPending(pendinglinks, url)
        if recrawl:
            try:
                site_model = GetSiteInfoModelFromURL(url)
                info = site_model.objects.get(url=url)
                AddError(info, "socket.timeout", 'Timed out Retrieving URL')
            except Exception:
                pass
        return False
    except socket.error as e:
        print('Socket error {0} retrieving URL: {1}'.format(e, url))
        RemoveFromPending(pendinglinks, url)
        if recrawl:
            try:
                site_model = GetSiteInfoModelFromURL(url)
                info = site_model.objects.get(url=url)
                AddError(info, "socket.error", str(e))
            except Exception:
                pass
        return False
    except ValueError as e:
        try:
            print('Value error, cannot crawl URL: {0} - {1}'.format(url, e))
        except Exception:
            print('Value error, cannot crawl URL: {0}'.format(e))
        RemoveFromPending(pendinglinks, url)
        try:
            site_model = GetSiteInfoModelFromURL(url)
            info = site_model.objects.get(url=url)
            AddError(info, 'ValueError', str(e))
        except Exception:
            pass
        return False
    except http.client.HTTPException as e:
        print('httplib.HTTPException retrieving URL: {0} - {1}'.format(url, e))
        RemoveFromPending(pendinglinks, url)
        try:
            site_model = GetSiteInfoModelFromURL(url)
            info = site_model.objects.get(url=url)
            AddError(info, 'HttpError', str(e))
        except Exception:
            pass
        return False
    except http.client.BadStatusLine as e:
        print('httplib.BadStatusLine retrieving URL: {0} - {1}'.format(url, e))
        RemoveFromPending(pendinglinks, url)
        return False
    except http.client.IncompleteRead as e:
        print('httplib.IncompleteRead read crawling URL: {0} - {1}'.format(url, e))
        RemoveFromPending(pendinglinks, url)
        return False
    except http.client.InvalidURL as e:
        print('Invalid URL: {0} - {1}'.format(url, e))
        RemoveFromPending(pendinglinks, url)
        return False


def Crawl(pendinglinks, max, sleep=10, descriptive=False, recrawl=False):
    if descriptive:
        prevqueries = 0
        start = timezone.now()
    failedurls = 0
    successfulurls = 0
    processedurls = 0
    crawled = []
    while processedurls < max and len(pendinglinks) > 0:
        # Keep a crawled list to prevent recrawling the same url in a session.
        if pendinglinks[0] in crawled:
            RemoveFromPending(pendinglinks, pendinglinks[0])
            processedurls = processedurls + 1
            continue
        else:
            crawled.append(pendinglinks[0])
        if not CrawlPage(pendinglinks, pendinglinks[0], descriptive, recrawl):
            failedurls = failedurls + 1
        else:
            successfulurls = successfulurls + 1
        processedurls = processedurls + 1
        if processedurls >= max:
            break
        time.sleep(sleep)
    print('Processed {0}, Crawled {1} URLs and failed or blocked {2} URLs.'.format(processedurls, successfulurls, failedurls))
    SavePendingUrls(pendinglinks, descriptive)
    if descriptive:
        querytime = LogQueries(connection.queries[prevqueries:])
        end_delta = timezone.now() - start
        print('Crawl time: {0} seconds (sleep {1}), queries {2} seconds.'.format(end_delta, sleep, querytime))


def CrawlSingleUrl(url):
    pendinglinks = []
    try:
        AddPendingLink(pendinglinks, url, descriptive=True, recrawl=True)
        Crawl(pendinglinks, 1, descriptive=True, recrawl=True)
    except Exception as e:
        try:
            print('Failure in CrawlSingleUrl for {0}: {1}'.format(url, e))
        except Exception:
            print('Failure in CrawlSingleUrl. Error or URL is unprintable')


def LoadUrlsFromFile(pendinglinks, filename, descriptive=False, seconds=1):
    f = open(filename, 'rb')
    reader = codecs.getreader('utf8')(f)
    for line in reader.readlines():
        # Ignore blank lines.
        if len(line) < 2:
            continue
        CrawlSingleUrl(line)
        time.sleep(seconds)


def QueryPendingUrls(pendinglinks, max, offset=0, language=None, descriptive=False, random=False, entiredomain=None):
    numloaded = 0
    if random:
        randomval = RandomValue()
        existing = CrawlableUrl.objects.filter(randval__gte=randomval).order_by('randval')[offset:(offset + max)]
    else:
        if entiredomain:
            print('Getting Pending URLs for {0}'.format(entiredomain))
            existing = CrawlableUrl.objects.filter(rooturl=entiredomain)[offset:(offset + max)]
        else:
            existing = CrawlableUrl.objects.all()[offset:(offset + max)]
    for url in existing:
        AddPendingLink(pendinglinks, url.url, descriptive=descriptive, recrawl=False)
        numloaded = numloaded + 1
        if descriptive:
            print('Loaded Pending URL from database: {0}'.format(url.url))
    print('{0} pending URLs loaded. {1} of those are crawlable and the rest were deleted.'.format(numloaded, len(pendinglinks)))


def RecrawlOldUrls(pendinglinks, max, offset=0, language=None, descriptive=False, seconds=5, entiredomain=None):
    site_model = GetSiteInfoModelFromLanguage(language)
    if entiredomain:
        print('Getting Existing URLs for {0}'.format(entiredomain))
        existing = site_model.objects.filter(rooturl=entiredomain).order_by('lastcrawled')[offset:(max + offset)]
    else:
        existing = site_model.objects.all().order_by('lastcrawled')[offset:(max + offset)]
    for url in existing:
        CrawlSingleUrl(url.url)
        time.sleep(seconds)


def RecrawlDoctypeUrls(pendinglinks, max, offset=0, language=None, descriptive=False):
    site_model = GetSiteInfoModelFromLanguage(language)
    existing = site_model.objects.filter(pagetext__istartswith='html public')[offset:(max + offset)]
    for url in existing:
        CrawlSingleUrl(url.url)
        time.sleep(1)


def RecrawlXmlUrls(pendinglinks, max, offset=0, language=None, descriptive=False, seconds=1):
    site_model = GetSiteInfoModelFromLanguage(language)
    existing = site_model.objects.filter(pagetext__istartswith='xml version')[offset:(max + offset)]
    for url in existing:
        CrawlSingleUrl(url.url)
        time.sleep(seconds)
