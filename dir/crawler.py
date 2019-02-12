from bs4 import BeautifulSoup, Comment, Doctype, Declaration, Tag, NavigableString
from bs4.element import ProcessingInstruction
import urllib2
import httplib
import time
import optparse
from dir.models import *
from dir.utils import *
from dir.robots import GetRobotsFile, AllowedByRobots
from dir.language import *
from django.db.utils import DatabaseError, DataError
from django.db import connection
from django.utils import timezone
from django.utils.timezone import utc
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import transaction
import HTMLParser
import datetime
import socket
import codecs
import random
import re

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
        #options['recrawl'] = True
        LoadUrlsFromFile(pendinglinks, options['file'], options['descriptive'], seconds=options['seconds'])
    else:
        print u"You didn't give me anything to do. I'm done doing that nothing you asked for."
        return
    if options['noop']:
        print u'These are the URLs that would be crawled:'
        for item in pendinglinks:
            print item
        return
    Crawl(pendinglinks, options['maxurls'], options['seconds'], options['descriptive'], options['recrawl'])
    #print u'Crawled ' + unicode(processedurls) + u' URLs, failed to crawl ' + unicode(failedurls) + u' out of a maximum of ' + unicode(options.maxurls) + u'. ' + unicode(removedfrompending) + u' URLs removed from pending table and ' + unicode(blockedurls) + u' not crawled because they were on the excluded list.'

def GetSiteInfoModelFromURL(url, descriptive=False):
    rooturl = GetRootUrl(url)
    try:
        domain = DomainInfo.objects.get(url=rooturl)
        # PROBLEM: We cannot identify the page's language until we have its text contents.
        #if domain.uses_langid:
        #    # TODO: Implement code.
        #    IdentifyLanguage(url.pagetext)
        if domain.uses_language_subdirs:
            language = GetInfixLanguage(url, descriptive)
            if descriptive and language:
                print u'GetSiteInfoModelFromURL: Subdir language is ' + language
            if not language and domain.language_association:
                language = domain.language_association
                print u'GetSiteInfoModelFromURL: No Subdir language, defaulting to ' + language
            if language and language != u'en':
                site_model = GetSiteInfoModelFromLanguage(language)
            else:
                site_model = GetSiteInfoModelFromLanguage('en')
        elif domain.uses_language_query_parameter:
            language = GetUrlParameterLanguage(url)
            if not language and domain.language_association:
                language = domain.language_association
            if descriptive and language:
                print u'GetSiteInfoModelFromURL: URL Parameter language is ' + language
            if language and language != u'en':
                site_model = GetSiteInfoModelFromLanguage(language)
            else:
                site_model = GetSiteInfoModelFromLanguage('en')
        elif domain.language_association:
            if descriptive:
                print u'GetSiteInfoModelFromURL: Domain language is ' + domain.language_association
            site_model = GetSiteInfoModelFromLanguage(domain.language_association)
        else:
            extlang = GetLanguageFromDomainExtension(rooturl)
            if descriptive:            
                print u'GetSiteInfoModelFromURL: Extlang is: ' + unicode(extlang)
            if extlang:
                site_model = GetSiteInfoModelFromLanguage(extlang)
            else:
                site_model = GetSiteInfoModelFromLanguage('en')
    except ObjectDoesNotExist:
        site_model = GetSiteInfoModelFromLanguage('en')
    return site_model

def PopulateSiteInfoFromHtml(siteinfo, html, descriptive=False):
    soup = BeautifulSoup(html)
    if soup.title:
        try:
            siteinfo.pagetitle = html_decode(soup.title.string).strip()[0:255]
            if descriptive:
                print u'Title: ' + siteinfo.pagetitle
        except:
            pass
    if descriptive:
        print u'Root URL: ' + siteinfo.rooturl
    description = soup.findAll(attrs = {'name': 'description'})
    if len(description) > 0:
        try:
            siteinfo.pagedescription = html_decode(description[0]['content'].strip())[0:319]
            if descriptive:
                print u'Description: ' + siteinfo.pagedescription
        except:
            pass
    keywords = soup.findAll(attrs = {'name': 'keywords'})
    if len(keywords) > 0:
        try:
            siteinfo.pagekeywords = keywords[0]['content'].strip()[0:255].lower()
            if descriptive:
                print u'Keywords: ' + siteinfo.pagekeywords
        except:
            pass
    try:
        # We don't actually store the canonical link anywhere, but we could if we wanted to.
        canonicallinks = soup.findAll('link', rel='canonical')
        for canonical in canonicallinks:
            print 'Canonical link found: {0}'.format(canonical['href'])
    except:
        pass
    headtags = soup.findAll('h1')
    if len(headtags) > 0:
        siteinfo.pagefirstheadtag = headtags[0].text.strip()[0:255]
        #if descriptive:
        #    print u'First H1 Tag: ' + siteinfo.pagefirstheadtag
    secondaryheadtags = soup.findAll('h2')
    if len(secondaryheadtags) > 0:
        siteinfo.pagefirsth2tag = secondaryheadtags[0].text.strip()[0:255]
    tertiaryheadtags = soup.findAll('h3')
    if len(tertiaryheadtags) > 0:
        siteinfo.pagefirsth3tag = tertiaryheadtags[0].text.strip()[0:255]
    iframes = soup.findAll('iframe')
    siteinfo.num_iframes = len(iframes)
    if descriptive:
        print 'Num Iframes: {0}'.format(siteinfo.num_iframes)
    for iframe in iframes:
        if descriptive:
            print 'IFrame: {0}'.format(iframe)
        src = iframe.attrs.get('src', None)
        if src:
            frame = PageIFrame()
            frame.rooturl_source = siteinfo.rooturl
            frame.url_source = siteinfo.url
            if src.startswith(u'http:') or src.startswith(u'https:'):
                frame.url_destination = src[0:2048]
                frame.rooturl_destination = GetRootUrl(src)
            elif src.startswith(u'//'):
                if frame.url_source.startswith(u'https'):
                    frame.url_destination = (u'https:' + src)[0:2048]
                    frame.rooturl_destination = GetRootUrl(frame.url_destination)
                else:
                    frame.url_destination = (u'http:' + src)[0:2048]
                    frame.rooturl_destination = GetRootUrl(frame.url_destination)
            else:
                if frame.url_source.startswith(u'https'):
                    frame.url_destination = (u'https://' + frame.rooturl_destination + src)[0:2048]
                    frame.rooturl_destination = GetRootUrl(src)
                else:
                    frame.url_destination = (u'http://' + frame.rooturl_destination + src)[0:2048]
                    frame.rooturl_destination = frame.rooturl_source
            frame.save()
            if descriptive:
                print u'PageIFrame: rooturl_source = {0}, rooturl_destination = {1}, url_source = {2}, url_destination = {3}'.format(
                    frame.rooturl_source, frame.rooturl_destination, frame.url_source, frame.url_destination)
    audios = soup.findAll('audio')
    siteinfo.num_audio_tags = len(audios)
    if descriptive:
        print 'Num Audio Tags: {0}'.format(siteinfo.num_audio_tags)
    videos = soup.findAll('video')
    siteinfo.num_video_tags = len(videos)
    if descriptive:
        print 'Num Video Tags: {0}'.format(siteinfo.num_video_tags)
    svgs = soup.findAll('svg')
    siteinfo.num_svg_tags = len(svgs)
    if descriptive:
        print 'Num svg Tags: {0}'.format(siteinfo.num_svg_tags)
    canvass = soup.findAll('canvas')
    siteinfo.num_canvas_tags = len(canvass)
    if descriptive:
        print 'Num canvas Tags: {0}'.format(siteinfo.num_canvas_tags)
    images = soup.findAll('img')
    siteinfo.num_images = len(images)
    if descriptive:
        print 'Num Images: {0}'.format(siteinfo.num_images)
    # Get image titles, URLs, and filenames.
    missingalt = ''
    image_alt_tags = []
    image_title_tags = []
    image_filenames = []
    for img in images:
        #print 'IMG: {0}\nAttrs: {2}'.format(img, img.text, img.attrs)
        if img.attrs.get('alt', None):
            image_alt_tags.append(img.attrs.get('alt'))
        else:
            #src = img.attrs.get('src', None)
            #print 'Image {0} lacks an alt tag.'.format(src)
            #if src:
            #    missingalt = missingalt + ', ' + src
            #else:
            #    missingalt = missingalt + src
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
        #print 'Link Attrs: {0}'.format(link.attrs)
        rel = link.attrs.get('rel', None)
        type = link.attrs.get('type', None)
        href = link.attrs.get('href', None)
        #print 'Link Rel: {0}, Type: {1}, href: {2}'.format(rel, type, href)
        if rel and rel[0].lower() == u'stylesheet':
            num_stylesheets += 1
        elif rel and rel[0].lower() == u'canonical':
            canonical = True
    if descriptive:
        print 'Total Links: {0}, Total Stylesheets: {1}, Canonical Link: {2}'.format(len(links), num_stylesheets, canonical)
    #siteinfo.has_canonical_tag = canonical
    siteinfo.num_css_files = num_stylesheets
    scripts = soup.findAll('script')
    num_external_scripts = 0
    for script in scripts:
        type = script.attrs.get('type', None)
        src = script.attrs.get('src', None)
        #print 'Script Type: {0}, src: {1}, attrs: {2}'.format(type, src, script.attrs)
        if src:
            #print 'SCRIPT: {0}'.format(script)
            num_external_scripts += 1
            pjs = PageJavaScript()
            pjs.rooturl_source = siteinfo.rooturl
            pjs.url_source = siteinfo.url
            if src.startswith(u'http:') or src.startswith(u'https:'):
                pjs.rooturl_destination = GetRootUrl(src)
                pjs.url_destination = src[0:2048]
            elif src.startswith(u'//'):
                if pjs.url_source.startswith(u'https'):
                    pjs.url_destination = (u'https:' + src)[0:2048]
                    pjs.rooturl_destination = GetRootUrl(pjs.url_destination)
                else:
                    pjs.url_destination = (u'http:' + src)[0:2048]
                    pjs.rooturl_destination = GetRootUrl(pjs.url_destination)
            else:
                if pjs.url_source.startswith(u'https'):
                    pjs.rooturl_destination = pjs.rooturl_source
                    pjs.url_destination = (u'https://' + pjs.rooturl_destination + src)[0:2048]
                else:
                    pjs.rooturl_destination = pjs.rooturl_source
                    pjs.url_destination = (u'http://' + pjs.rooturl_destination + src)[0:2048]
            fname = pjs.url_destination.split('/')[-1]
            if fname:
                pjs.filename = fname[0:255]
            if descriptive:
                print u'PageJavaScript: rooturl_source = {0}, rooturl_destination = {1}, url_source = {2}, url_destination = {3}, filename = {4}'.format(
                    pjs.rooturl_source, pjs.rooturl_destination, pjs.url_source, pjs.url_destination, pjs.filename)
            pjs.save()
    siteinfo.num_javascripts = num_external_scripts
    if descriptive:
        print 'Num Scripts: {0}, Total Script Links (num_javascripts): {1}'.format(len(scripts), num_external_scripts)
    #siteinfo.num_external_scripts = num_external_scripts

    # TODO: Get the domain creation and expiration date periodically.
    #(siteinfo.domain_created, siteinfo.domain_expires) = GetDomainAge(siteinfo.rooturl)
    # TODO: Load and parse the robots.txt file.
    #siteinfo.allowed_by_robots = AllowedByRobots(siteinfo.url)
    try:
        sitehtml = unicode(soup)
        if not siteinfo.pagesize:
            siteinfo.pagesize = len(sitehtml)
            if descriptive:
                print u'No page size from host. Using HTML size. Will be inaccurate if page is larger than buffer.'
        sitehtml = re.sub(">\s+<", "><", sitehtml).strip()
    except RuntimeError:
        print u'Received a RuntimeError getting site HTML from BeautifulSoup. This is probably an infinite recursion error.'
        sitehtml = ''
    if len(sitehtml) < 8192:
        siteinfo.pagecontents = sitehtml
    else:
        siteinfo.pagecontents = sitehtml[0:8192]
    # Remove script and style tags for cleaner text.
    [item.extract() for item in soup.contents if isinstance(item, Doctype)]
    [s.extract() for s in soup(['script', 'style', 'head'])]
    # Remove comment tags for cleaner text.
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    [comment.extract() for comment in comments]
    #navigablestrings = soup.findAll(text=lambda text:isinstance(text, NavigableString))
    #for navstr in navigablestrings:
    #    print u'NAVIGABLE STRING: Name = {0}, String {1}, Value = {2}'.format(navstr.name, navstr.string, navstr)
    #[navigablestring.extract() for navigablestring in navigablestrings]
    for item in soup:
        if isinstance(item, ProcessingInstruction):
            print u'Removing {0}'.format(item)
            item.extract()
            break
    # DEBUGGING: Prints every single tag in the document.
    # Move this before the extract calls above to see everything.
    #for item in soup.contents:
    #    try:
    #        print u'{0}: Name: {1}, Attributes {2}, Print: {3}'.format(item.__class__.__name__, item.name, item.attrs, item)
    #    except:
    #        try:
    #            print u'{0}: Name: {1}, String: {2}, Print: {3}'.format(item.__class__.__name__, item.name, item.string, item)
    #        except:
    #            print u'BAD TYPE: {0}'.format(item)
    text = ' '.join(soup.findAll(text=True))
    text = text.replace('\n', ' ')
    if text:
        text = re.sub('\s+', ' ', text).strip()
    if len(text) < 8192:
        siteinfo.pagetext = text
    else:
        siteinfo.pagetext = text[0:8192]
    siteinfo.lastcrawled = timezone.now()
    return soup

def ParseHtml(pendinglinks, url, response, descriptive=False, recrawl=False):
    # By not reading the entire page we save some bandwidth, but we also truncate links at
    # the bottom of a page and fail to find them. This means that the footers of large pages
    # are effectively invisible to us. This may or may not ever be a problem.
    html = response.read(65536)
    realurl = response.geturl()
    ipaddr = None
    print u'Real URL is: ' + realurl
    normaled = NormalizeUrl(realurl, post_crawl_replacement=True)
    if normaled != realurl:
        try:
            print u'URL Normalized to {0}'.format(normaled)
        except:
            pass
        realurl = normaled
    try:
        ipaddr = socket.gethostbyname(urlparse.urlparse(realurl).hostname)
        if descriptive:
            print u'IP Address is: ' + unicode(ipaddr)
    except:
        pass
    if (not recrawl and not CanCrawlUrl(realurl)) or (recrawl and not CanReCrawlUrl(realurl, descriptive)):
        if descriptive:
            print u'Not saving URL because it is blocked or not HTML: ' + realurl
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
            print 'Removed {0} instances of {1} from the database.'.format(count, realurl)
            remove_model = GetSiteInfoModelFromURL(url, descriptive)
            count = RemoveFromDatabase(url, descriptive, all_languages=True, model=remove_model)
            print 'Removed {0} instances of {1} from the {2} database.'.format(count, url, remove_model)
        return False
    rooturl = GetRootUrl(realurl)
    # We need to check the real root url for blocking too. We do this in addition to
    # when we add to the pending list because we may have received something different
    # due to a redirect and we don't want to save it.
    info = None
    try:
        site_model = GetSiteInfoModelFromURL(realurl, descriptive)
    except InvalidLanguageException, e:
        print u'InvalidLanguageException: {0} (not saving page)'.format(e)
        return False
    info = site_model()
    info.rooturl = rooturl
    info.url = realurl
    if ipaddr:
        info.ip = ipaddr
    if descriptive:
        print u'URL: ' + info.url
        print 'Using language table {0}'.format(site_model)

    # Get Headers
    # Content-Length may not always be reliable, or present. In addition,
    # if we don't get the content length, our length will cap out at 40000,
    # since that's all we read.
    try:
        length = int(response.headers["Content-Length"])
        if descriptive:
            print u'Content-Length: {0}'.format(unicode(length))
        if length > 0:
            info.pagesize = length
    except:
        pass
    server_header = response.headers.get('server', None)
    content_type_header = response.headers.get('content-type', None)
    if server_header:
        info.server_header = server_header[0:100]
        if descriptive:
            print u'Server: {0}'.format(unicode(server_header))
    if content_type_header:
        info.content_type_header = content_type_header[0:100]
        if descriptive:
            print u'Content-Type: {0}'.format(unicode(content_type_header))

    if realurl != url:
        if descriptive:
            print u'Requested URL: ' + url + ', Actual URL: ' + realurl
        # If something redirects somewhere else, we should make sure that the URL
        # that does the redirecting is not in the database.
        remove_model = GetSiteInfoModelFromURL(url, descriptive)
        print 'Removing {0} from the database with model {1}'.format(url, remove_model)
        count = RemoveFromDatabase(url, descriptive, all_languages=True, model=remove_model)
        print 'Removed {0} instances of {1} from the database.'.format(count, url)
        RemoveFromPending(pendinglinks, url)
    # Clear out old iframes and javascripts.
    # We have to do this before calling PopulateSiteInfoFromHtml because
    # that creates the PageIFrame and PageJavaScript objects.
    elinks = PageIFrame.objects.filter(url_source = info.url)
    if descriptive:
        print u'Deleting {0} existing IFrames.'.format(elinks.count())
    for elink in elinks:
        elink.delete()
    elinks = PageJavaScript.objects.filter(url_source = info.url)
    if descriptive:
        print u'Deleting {0} existing JavaScripts.'.format(elinks.count())
    for elink in elinks:
        elink.delete()

    try:
        soup = PopulateSiteInfoFromHtml(info, html, descriptive)
    except HTMLParser.HTMLParseError, e:
        RemoveFromPending(pendinglinks, realurl)     
        print u'HTMLParseError: {0}.'.format(e)
        return False
    try:
        previous = site_model.objects.get(url=realurl)
        if descriptive and not recrawl:
            print u'URL already crawled, not saving: ' + realurl
        elif recrawl:
            if descriptive:
                print u'Updating existing URL in database: ' + realurl
            # Delete links for existing pages because we'll re-add them farther down.
            elinks = PageLink.objects.filter(url_source = info.url)
            if descriptive:
                print u'Deleting {0} existing links.'.format(elinks.count())
            for elink in elinks:
                elink.delete()
            # TODO: See if this and CopySiteData are duplicate code. They probably are.
            previous.pagecontents = info.pagecontents
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
                    print u'Deleting URL from en table for site tagged as non-English'
                    oldsite.delete()
                except ObjectDoesNotExist:
                    pass
    except:
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
            print u'Failed to save URL: ' + info.url
            connection._rollback()
    RemoveFromPending(pendinglinks, url)
    RemoveFromPending(pendinglinks, realurl)
    # Add pending links and URL links.
    for link in soup.find_all('a'):
        hr = link.get('href')
        if hr:
            if IsHtmlUrl(hr):
                #prehr = hr
                if realurl.startswith(u'https:'):
                    hr = MakeRealUrl(hr, rooturl, secure=True)
                else:
                    hr = MakeRealUrl(hr, rooturl)
                #print 'MAKEREALURL: {0} IS NOW {1} WITH ROOT URL {2}'.format(prehr, hr, rooturl)
                destroot = GetRootUrl(hr)
                if destroot and destroot != rooturl and '.' in destroot and destroot != '.' and not IsHtmlExtension(destroot):
                    try:
                        existing = PageLink.objects.get(url_source=info.url, url_destination=hr)
                    except ObjectDoesNotExist:
                        ulink = PageLink()
                        ulink.rooturl_source = rooturl
                        ulink.url_source = info.url
                        ulink.url_destination = hr
                        ulink.rooturl_destination = destroot
                        try:
                            title = link.contents[0]
                            if title:
                                ulink.anchor_text = unicode(title)[0:255]
                        except IndexError:
                            pass
                        try:
                            ulink.save()
                        except DataError, e:
                            # We can get this if a root url is too log (>260 chars) or full URL is too long (>2048 chars)
                            connection._rollback()
                            print u'Problem saving PageLink: {0}'.format(e)
                        if descriptive:
                            print u'Added link from {0} to {1} with anchor {2}'.format(ulink.url_source, ulink.url_destination, ulink.anchor_text)
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
            print u'Url too long to be valid (>2048): ' + url
        return
    if not IsHtmlUrl(url):
        return
    # Normalize URL. MakeRealUrl calls NormalizeUrl.
    origurl = url
    try:
        url = MakeRealUrl(url, root)
    except UnicodeEncodeError:
        print u'URL is not valid (UnicodeEncodeError). Cannot crawl.'
        if recrawl:
            remove_model = GetSiteInfoModelFromURL(url, descriptive)
            print u'Removing invalid URL from the {0} database.'.format(remove_model)
            count = RemoveFromDatabase(url, descriptive, all_languages=True, model=remove_model)
            print 'Removed {0} instances of the url from the database.'.format(count, origurl)
        return
    #url = NormalizeUrl(url, pre_crawl_replacement=True)
    if origurl != url:
        if descriptive:
            print u'URL ' + origurl + ' normalized to ' + url
        RemoveFromPending(pendinglinks, origurl)
        if recrawl:
            # Delete previous url because we'll never save it in that format.
            print u'Removing pre-normalized URL {0} from the database.'.format(origurl)
            remove_model = GetSiteInfoModelFromURL(origurl, descriptive)
            count = RemoveFromDatabase(origurl, descriptive, all_languages=True, model=remove_model)
            try:
                print 'Removed {0} instances of {1} from the database.'.format(count, origurl)
            except:
                print 'Removed {0} instances of the url from the database.'.format(count, origurl)
    # Prevent crawling excluded sites, non-HTML, and at-url-limit sites.
    if not recrawl and not CanCrawlUrl(url):
        if descriptive:
            print u'Not crawling URL because it is blocked or not HTML: ' + url
        RemoveFromPending(pendinglinks, url)
        return
    elif recrawl and not CanReCrawlUrl(url, descriptive):
        if descriptive:
            print u'Not recrawling URL because it is blocked or not HTML: ' + url
        RemoveFromPending(pendinglinks, url)
        try:
            print u'Removing blocked site URL {0} from the database.'.format(url)
            remove_model = GetSiteInfoModelFromURL(origurl, descriptive)
            count = RemoveFromDatabase(url, descriptive, all_languages=True, model=remove_model)
            try:
                print 'Removed {0} instances of {1} from the database.'.format(count, url)
            except:
                print 'Removed {0} instances of the url from the database.'.format(count, url)
        except ObjectDoesNotExist:
            pass
        return
    if not recrawl:
        try:
            site_model = GetSiteInfoModelFromURL(url, descriptive)
            previous = site_model.objects.get(url=url)
            if descriptive:
                print u'URL in DB, non recrawl mode, skip add to pending: ' + url
            RemoveFromPending(pendinglinks, url)
            return
        except:
            pass
    if url in pendinglinks:
        return
    if descriptive:
        try:
            print u'Add Pending Link: {0}'.format(url)
        except:
            pass
    pendinglinks.append(url)

def SavePendingUrls(pendinglinks, descriptive=False):
    numpendingadded = 0
    for url in pendinglinks:
        rooturl = GetRootUrl(url)
        lang = 'en'
        try:
            domain = DomainInfo.objects.get(url=rooturl)
            if domain.language_association:
                lang = domain.language_association
        except:
            pass
        # Never save links where we have existing site info.
        #
        # TODO: Check other languages.
        site_model = GetSiteInfoModelFromLanguage(lang)
        try:
            existingpage = site_model.objects.get(url=url)
            continue
        except ObjectDoesNotExist:
            pass
        try:
            existing = CrawlableUrl.objects.get(url=url)
        except ObjectDoesNotExist:
            pending = CrawlableUrl()
            pending.url = url
            pending.rooturl = rooturl
            try:
                pending.save()
                if descriptive:
                    try:
                        print u'Added pending URL to database: ' + url
                    except:
                        print u'Added a pending URL to the database.'
            except DatabaseError:
                connection._rollback()
            numpendingadded = numpendingadded + 1
    print unicode(numpendingadded) + u' URLs were added to the pending URL table.'

def RemoveFromPending(pendinglinks, url):
    try:
        if url in pendinglinks:
            pendinglinks.remove(url)
        existing = CrawlableUrl.objects.get(url=url)
        existing.delete()
        return True
    except:
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
                print u'{0} deleted from {1}'.format(url, model)
        except ObjectDoesNotExist:
            pass
    try:
        rooturl = GetRootUrl(url)
        domain = DomainInfo.objects.get(url=rooturl)
        language = domain.language_association
    except:
        language = 'en'
    try:
        site_model = GetSiteInfoModelFromLanguage(language)
        existing = site_model.objects.get(url=url)
        existing.delete()
        removed = removed + 1
        if descriptive:
            print u'URL deleted from ' + language + ' database: ' + url
    except:
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
                print u'URL deleted from en database: ' + url
            except:
                pass
    return removed

def CrawlPage(pendinglinks, url, descriptive=False, recrawl=False):
        try:
            root = GetRootUrl(url)
            domain = DomainInfo.objects.get(url=root)
        except ObjectDoesNotExist:
            # Always create domain info and check for robots.txt even if the domain doesn't exist yet.
            domain = DomainInfo()
            domain.url = root
            try:
                print u'Created new DomainInfo entry for {0}.'.format(root)
            except:
                print u'Created new DomainInfo entry.'
        if domain.robots_last_updated == None:
            print u'Robots file never checked for database {0}, retrieving now.'.format(root)
            try:
                GetRobotsFile(domain)
            except Exception, e:
                print u'Could not get robots file. Acting as if no robots file exists. Exception: {0}'.format(e)
            if not AllowedByRobots(url, domain):
                print u'This URL is blocked by the robots.txt file.'
                RemoveFromPending(pendinglinks, url)
                if recrawl:
                    count = RemoveFromDatabase(url, descriptive)
                    if count > 0:
                        print 'Removed {0} instances of {1} from the database.'.format(count, url)
                return False
        try:
            print u'Retrieving {0}'.format(url)
        except:
            print u'Retrieving URL'
        req = urllib2.Request(url)
        req.add_header('User-agent', 'Mozilla/5.0 (compatible; WbSrch/1.1 +https://wbsrch.com)')
        try:
            response = urllib2.urlopen(req, timeout=20)
            if ParseHtml(pendinglinks, url, response, descriptive, recrawl):
                return True
            else:
                if descriptive:
                    print u'Failed to parse HTML.'
                return False
        except urllib2.HTTPError, e:
            # 4XX errors are immediately fatal and we remove the URL.
            if e.code == 404 or e.code == 403 or e.code == 401 or e.code == 400 or e.code == 410 or e.code == 406:
                if descriptive:
                    print u'HTTP Error: ' + unicode(e.code)
                RemoveFromPending(pendinglinks, url)
                if recrawl:
                    remove_model = GetSiteInfoModelFromURL(url, descriptive)
                    count = RemoveFromDatabase(url, descriptive, model=remove_model)
                    print 'Removed {0} instances of {1} from the database.'.format(count, url)
                return False
            elif e.code == 302:
                try:
                    print u'HTTP Error: {0} - {1}'.format(e.code, e.reason)
                except:
                    print u'302 Redirect.'
                if recrawl:
                    try:
                        # Regular 302 errors are handled normally and transparenty by the
                        # BeautifulSoup library. It's only fatal 302 errors that will reach
                        # this code block. Those errors will be infinite redirect loop errors.
                        site_model = GetSiteInfoModelFromURL(url)
                        info = site_model.objects.get(url=url)
                        AddError(info, unicode(e.code), u'HTTP Error {0} - {1}'.format(e.code, e.reason))
                    except:
                        pass
                    # May want to return False in all cases, not just recrawl.
                    return False
            # For recrawling a 500-series error, log an error. If we consistently get them, the URL will delete itself.
            elif e.code == 503 or e.code == 502 or e.code == 500 or e.code == 504 or e.code == 501:
                try:
                    print u'HTTP Error: {0} - {1}'.format(e.code, e.reason)
                except:
                    print u'HTTP Error (unprintable)'
                try:
                    site_model = GetSiteInfoModelFromURL(url)
                    info = site_model.objects.get(url=url)
                    AddError(info, unicode(e.code), u'HTTP Error ' + unicode(int(e.code)))
                except:
                    pass
            else:
                print u'HTTP Error: {0} - {1}'.format(e.code, e.reason)
                if recrawl:
                    try:
                        site_model = GetSiteInfoModelFromURL(url)
                        info = site_model.objects.get(url=url)
                        AddError(info, unicode(e.code), u'HTTP Error ' + unicode(int(e.code)))
                    except:
                        pass
        except urllib2.URLError, e:
            print u'Unable to crawl URL ' + url + u': urllib2.URLError is ' + unicode(e.args)
            RemoveFromPending(pendinglinks, url)
            if isinstance(e.args, (tuple,)):
                if descriptive:
                    print u'Error: {0} [{1}]]'.format(e.args[0], type(e.args[0])) + u']'
                if isinstance(e.args[0], (socket.timeout,)):
                    print u'Timed out retrieving URL: ' + url
                    RemoveFromPending(pendinglinks, url)
                    if recrawl:
                        try:
                            site_model = GetSiteInfoModelFromURL(url)
                            print 'Logging Error to {0}'.format(site_model)
                            info = site_model.objects.get(url=url)
                            AddError(info, "socket.timeout", 'Timed out Retrieving URL')
                        except ObjectDoesNotExist:
                            pass
                    return False
                if isinstance(e.args[0], (socket.gaierror,)):
                    print u'This is a socket.gaierror - Error: ' + unicode(e.args[0].errno) + u', Message: ' + e.args[0].strerror
                    # A DNS lookup failure means we should remove it from the database.
                    if e.args[0].errno == -2 and recrawl:
                        print u'Removing this URL from the database.'
                        count = RemoveFromDatabase(url, descriptive)
                        print 'Removed {0} instances of {1} from the database.'.format(count, url)
            if recrawl:
                try:
                    site_model = GetSiteInfoModelFromURL(url)
                    info = site_model.objects.get(url=url)
                    AddError(info, u"urllib2.URLError", u'e.args: ' + unicode(e.args[0]) + u' [' + unicode(type(e.args[0])) + u'] ' + unicode(dir(e.args[0])))
                except ObjectDoesNotExist:
                    pass
            return False
        except socket.timeout, e:
            print u'Timed out retrieving URL: {0} - {1}'.format(url,e)
            RemoveFromPending(pendinglinks, url)
            if recrawl:
                try:
                    site_model = GetSiteInfoModelFromURL(url)
                    info = site_model.objects.get(url=url)
                    AddError(info, "socket.timeout", 'Timed out Retrieving URL')
                except:
                    pass
            return False
        except socket.error, e:
            print u'Socket error {0} retrieving URL: {1}'.format(e, url)
            RemoveFromPending(pendinglinks, url)
            if recrawl:
                try:
                    site_model = GetSiteInfoModelFromURL(url)
                    info = site_model.objects.get(url=url)
                    AddError(info, u"socket.error", unicode(e))
                except:
                    pass
            return False
        except ValueError, e:
            try:
                print u'Value error, cannot crawl URL: {0} - {1}'.format(url,e)
            except:
                print u'Value error, cannot crawl URL: {0}'.format(e)
            RemoveFromPending(pendinglinks, url)
            try:
                site_model = GetSiteInfoModelFromURL(url)
                info = site_model.objects.get(url=url)
                AddError(info, u'ValueError', unicode(e))
            except:
                pass
            return False
        except httplib.HTTPException, e:
            print u'httplib.HTTPException retrieving URL: {0} - {1}'.format(url,e)
            RemoveFromPending(pendinglinks, url)
            try:
                site_model = GetSiteInfoModelFromURL(url)
                info = site_model.objects.get(url=url)
                AddError(info, u'HttpError', unicode(e))
            except:
                pass
            return False
        except httplib.BadStatusLine, e:
            print u'httplib.BadStatusLine retrieving URL: {0} - {1}'.format(url,e)
            RemoveFromPending(pendinglinks, url)
            return False
        except httplib.IncompleteRead, e:
            print u'httplib.IncompleteRead read crawling URL: {0} - {1}'.format(url,e)
            RemoveFromPending(pendinglinks, url)
            return False
        except httplib.InvalidURL, e:
            print u'Invalid URL: {0} - {1}'.format(url,e)
            RemoveFromPending(pendinglinks, url)
            return False
        #except:
        #    print u'Invalid or uncrawlable URL: ' + url
        #    RemoveFromPending(pendinglinks, url)
        #    return False

def Crawl(pendinglinks, max, sleep=10, descriptive=False, recrawl=False):
    if descriptive:
        #prevqueries = len(connection.queries)
        prevqueries = 0
        start = timezone.now()
    failedurls = 0
    successfulurls = 0
    # TODO: Find a way to track these in this new code.
    #removedfrompending = 0
    #blockedurls = 0
    processedurls = 0
    crawled = []
    while processedurls < max and len(pendinglinks) > 0:
        #print u'URL List top 10 before crawl: '
        #for list_url in pendinglinks[0:12]:
        #    print list_url
        
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
        #print u'URL List top 10 after crawl: '
        #for list_url in pendinglinks[0:12]:
        #    print list_url
        #print u'---'
        time.sleep(sleep)
    print u'Processed ' + unicode(processedurls) + ', Crawled ' + unicode(successfulurls) + ' URLs and failed or blocked ' + unicode(failedurls) + ' URLs.'
    SavePendingUrls(pendinglinks, descriptive)
    if descriptive:
        querytime = LogQueries(connection.queries[prevqueries:])
        end_delta = timezone.now() - start
        print u'Crawl time: ' + unicode(end_delta) + u' seconds (sleep ' + unicode(sleep) + u'), queries ' + unicode(querytime) + u' seconds.'

def CrawlSingleUrl(url):
    pendinglinks = []
    #if True:
    try:
        AddPendingLink(pendinglinks, url, descriptive=True, recrawl=True)
        Crawl(pendinglinks, 1, descriptive=True, recrawl=True)
    except Exception, e:
        try:
            print u'Failure in CrawlSingleUrl for {0}: {1}'.format(url, e)
        except:
            print u'Failure in CrawlSingleUrl. Error or URL is unprintable'

def LoadUrlsFromFile(pendinglinks, filename, descriptive=False, seconds=1):
    numloaded = 0
    f = open(filename, 'rb')
    reader = codecs.getreader('utf8')(f)
    for line in reader.readlines():
        # Ignore blank lines.
        if len(line) < 2:
            continue
        CrawlSingleUrl(line)
        time.sleep(seconds)
        #AddPendingLink(pendinglinks, line, descriptive=descriptive, recrawl=True)
        #numloaded = numloaded + 1
    #print unicode(numloaded) + ' URLs loaded from ' + filename + '. ' + unicode(len(pendinglinks)) + ' of those are crawlable and the rest were deleted.'

def QueryPendingUrls(pendinglinks, max, offset=0, language=None, descriptive=False, random=False, entiredomain=None):
    numloaded = 0
    if random:
        randomval = RandomValue()
        existing = CrawlableUrl.objects.filter(randval__gte=randomval).order_by('randval')[offset:(offset+max)]
    else:
        if entiredomain:
            print u'Getting Pending URLs for {0}'.format(entiredomain)
            existing = CrawlableUrl.objects.filter(rooturl=entiredomain)[offset:(offset+max)]
        else:
            existing = CrawlableUrl.objects.all()[offset:(offset+max)]
    for url in existing:
        AddPendingLink(pendinglinks, url.url, descriptive=descriptive, recrawl=False)
        numloaded = numloaded + 1
        if descriptive:
            print u'Loaded Pending URL from database: ' + url.url
    print unicode(numloaded) + ' pending URLs loaded. ' + unicode(len(pendinglinks)) + ' of those are crawlable and the rest were deleted.'

def RecrawlOldUrls(pendinglinks, max, offset=0, language=None, descriptive=False, seconds=5, entiredomain=None):
    numloaded = 0
    site_model = GetSiteInfoModelFromLanguage(language)
    if entiredomain:
        print u'Getting Existing URLs for {0}'.format(entiredomain)
        existing = site_model.objects.filter(rooturl=entiredomain).order_by('lastcrawled')[offset:(max + offset)]
    else:
        existing = site_model.objects.all().order_by('lastcrawled')[offset:(max + offset)]
    for url in existing:
        CrawlSingleUrl(url.url)
        time.sleep(seconds)
        #AddPendingLink(pendinglinks, url.url, descriptive=descriptive, recrawl=True)
        #numloaded = numloaded + 1
        #if descriptive:
        #    print u'Loaded Stale URL from database: ' + url.url
    #print unicode(numloaded) + ' stale URLs loaded. ' + unicode(len(pendinglinks)) + ' of those are crawlable and the rest were deleted.'

def RecrawlDoctypeUrls(pendinglinks, max, offset=0, language=None, descriptive=False):
    numloaded = 0
    site_model = GetSiteInfoModelFromLanguage(language)
    existing = site_model.objects.filter(pagetext__istartswith='html public')[offset:(max + offset)]
    for url in existing:
        CrawlSingleUrl(url.url)
        time.sleep(1)

def RecrawlXmlUrls(pendinglinks, max, offset=0, language=None, descriptive=False, seconds=1):
    numloaded = 0
    site_model = GetSiteInfoModelFromLanguage(language)
    existing = site_model.objects.filter(pagetext__istartswith='xml version')[offset:(max + offset)]
    for url in existing:
        CrawlSingleUrl(url.url)
        #print u'Sleeping {0}'.format(seconds)
        time.sleep(seconds)

