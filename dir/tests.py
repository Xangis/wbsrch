# Requires Python 2.7 or newer

# Test database:
# db: test_zetaweb
# user: zetaweb

# Note: If you get an error about not being able to create a database for lack of
# permissions, the zetaweb DB user may need CREATEDB permission:
#
# ALTER USER zetaweb CREATEDB;

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import timezone
from models import *
from exceptions import *
from utils import *
from crawler import *
from indexer import *
from language import *
from domain import *
from zetaweb.settings import *
from datetime import datetime, date, timedelta

class GetRootUrlTestCase(TestCase):

    def test_url_with_period(self):
        """
        Tests that a URL with a period at the end has the period stripped.
        """
        url = GetRootUrl(u'http://zetacentauri.com.')
        self.assertEqual(url, u'zetacentauri.com')

    def test_url_with_period_and_suffix(self):
        """
        Tests that a URL with a period at the end has the period stripped when there is data after the period.
        """
        url = GetRootUrl(u'http://zetacentauri.com./software/')
        self.assertEqual(url, u'zetacentauri.com')

    def test_url_case(self):
        """
        Tests that a URL with mixed cases gets a lowercase root URL.
        """
        url = GetRootUrl(u'http://ZetaCenTaUri.coM')
        self.assertEqual(url, u'zetacentauri.com')

    def test_url_with_https(self):
        """
        Tests that a URL with https gets a proper root URL.
        """
        url = GetRootUrl(u'https://zetacentauri.com')
        self.assertEqual(url, u'zetacentauri.com')

    def test_url_with_colon(self):
        """
        Tests that a URL containing a colon (port 8080) gets the proper root URL with the colon.
        """
        url = GetRootUrl(u'https://zetacentauri.com:8080')
        self.assertEqual(url, u'zetacentauri.com:8080')

    def test_url_with_colon_eighty(self):
        """
        Tests that a URL containing a colon (port 80) gets the proper root URL without the colon.
        """
        url = GetRootUrl(u'https://zetacentauri.com:80')
        self.assertEqual(url, u'zetacentauri.com')

    def test_url_with_subdomain(self):
        """
        Tests that a URL with a subdomain works.
        """
        url = GetRootUrl(u'https://www.zetacentauri.com:80')
        self.assertEqual(url, u'www.zetacentauri.com')

    def test_url_with_subdomain(self):
        """
        Tests that a URL with a subdomain works.
        """
        url = GetRootUrl(u'://www.zetacentauri.com')
        self.assertEqual(url, u'www.zetacentauri.com')

    def test_url_with_subdomain2(self):
        """
        Tests that a URL with a subdomain works (2).
        """
        url = GetRootUrl(u'https://another.subdomain.zetacentauri.com')
        self.assertEqual(url, u'another.subdomain.zetacentauri.com')

class GetRootDomainTestCase(TestCase):

    def test_url_with_period(self):
        """
        Tests that a URL with a period at the end has the period stripped.
        """
        url = GetRootDomain(u'http://zetacentauri.com.')
        self.assertEqual(url, u'zetacentauri.com')

    def test_url_with_period_and_suffix(self):
        """
        Tests that a URL with a period at the end has the period stripped when there is data after the period.
        """
        url = GetRootDomain(u'http://zetacentauri.com./software/')
        self.assertEqual(url, u'zetacentauri.com')

    def test_url_case(self):
        """
        Tests that a URL with mixed cases gets a lowercase root URL.
        """
        url = GetRootDomain(u'http://ZetaCenTaUri.coM')
        self.assertEqual(url, u'zetacentauri.com')

    def test_ip_case(self):
        url = GetRootDomain(u'http://192.168.0.1')
        self.assertEqual(url, u'192.168.0.1')

    def test_ip_folder_case(self):
        url = GetRootDomain(u'http://216.151.3.15/index-stats/index.htm')
        self.assertEqual(url, u'216.151.3.15')

    def test_url_with_https(self):
        """
        Tests that a URL with https gets a proper root URL.
        """
        url = GetRootDomain(u'https://zetacentauri.com')
        self.assertEqual(url, u'zetacentauri.com')

    def test_url_with_colon(self):
        """
        Tests that a URL containing a colon (port 8080) gets the proper root URL with the colon.
        """
        url = GetRootDomain(u'https://zetacentauri.com:8080')
        self.assertEqual(url, u'zetacentauri.com:8080')

    def test_url_with_colon_eighty(self):
        """
        Tests that a URL containing a colon (port 80) gets the proper root URL without the colon.
        """
        url = GetRootDomain(u'https://zetacentauri.com:80')
        self.assertEqual(url, u'zetacentauri.com')

    def test_url_with_subdomain(self):
        """
        Tests that a URL with a subdomain works.
        """
        url = GetRootDomain(u'https://www.zetacentauri.com:80')
        self.assertEqual(url, u'zetacentauri.com')

    def test_url_with_subdomain2(self):
        """
        Tests that a URL with a subdomain works (2).
        """
        url = GetRootDomain(u'https://another.subdomain.zetacentauri.com')
        self.assertEqual(url, u'zetacentauri.com')

    def test_url_with_subdomain3(self):
        """
        Tests that a URL with a subdomain works (2).
        """
        url = GetRootDomain(u'https://another.subdomain.zetacentauri.com/software/whatever/something.htm')
        self.assertEqual(url, u'zetacentauri.com')

class IsValidHtmlUrlTestCase(TestCase):
    def test_mp3_url(self):
        """
        Tests that a URL ending with MP3 does not register as valid.
        """
        url = u"http://wbsrch.com/tutorial.mp3"
        self.assertFalse(IsHtmlUrl(url))

    def test_wav_url(self):
        """
        Tests that a URL ending with wav does not register as valid.
        """
        url = u"http://wbsrch.com/tutorial.wav"
        self.assertFalse(IsHtmlUrl(url))

    def test_htm_url(self):
        """
        Tests that a URL ending with htm does register as valid.
        """
        url = u"http://wbsrch.com/tutorial.htm"
        self.assertTrue(IsHtmlUrl(url))

    def test_aspx_url(self):
        """
        Tests that a URL ending with aspx does register as valid.
        """
        url = u"http://wbsrch.com/tutorial.aspx"
        self.assertTrue(IsHtmlUrl(url))

    def test_html_url(self):
        """
        Tests that a URL ending with html does register as valid.
        """
        url = u"http://wbsrch.com/tutorial.html"
        self.assertTrue(IsHtmlUrl(url))

    def test_slash_url(self):
        """
        Tests that a URL ending with / does register as valid.
        """
        url = u"http://wbsrch.com/tutorial/"
        self.assertTrue(IsHtmlUrl(url))

    def test_php_url(self):
        """
        Tests that a URL ending with php does register as valid.
        """
        url = u"http://wbsrch.com/tutorial.php"
        self.assertTrue(IsHtmlUrl(url))

    def test_md5_url(self):
        """
        Tests that a URL ending with md5 does register as valid.
        """
        url = u"http://wbsrch.com/tutorial.file.name.md5"
        self.assertFalse(IsHtmlUrl(url))

    def test_pl_url(self):
        """
        Tests that a URL ending with .pl does register as valid.
        """
        url = u"http://wbsrch.com/tutorial.pl"
        self.assertTrue(IsHtmlUrl(url))

    def test_js_url(self):
        """
        Tests that a URL starting with javascript: does not register as valid.
        """
        url = u"javascript:alert(0)"
        self.assertFalse(IsHtmlUrl(url))

    def test_mailto_url(self):
        """
        Tests that a URL starting with mailto: does not register as valid.
        """
        url = u"mailto:example@example.com"
        self.assertFalse(IsHtmlUrl(url))

    def test_exe_url(self):
        """
        Tests that a URL ending with exe does not register as valid.
        """
        url = u"http://wbsrch.com/run.exe"
        self.assertFalse(IsHtmlUrl(url))

    def test_xpi_url(self):
        url = u"http://wbsrch.com/addon.xpi"
        self.assertFalse(IsHtmlUrl(url))

    def test_pdf_url(self):
        """
        Tests that a URL ending with pdf does not register as valid.
        """
        url = u"http://wbsrch.com/tutorial.pdf"
        self.assertFalse(IsHtmlUrl(url))

    def test_gif_url(self):
        """
        Tests that a URL ending with gif does not register as valid.
        """
        url = u"http://wbsrch.com/tutorial.gif"
        self.assertFalse(IsHtmlUrl(url))

    def test_png_url(self):
        """
        Tests that a URL ending with png does not register as valid.
        """
        url = u"http://wbsrch.com/tutorial.png"
        self.assertFalse(IsHtmlUrl(url))

    def test_au_url(self):
        """
        Tests that a URL ending with au does register as valid.
        """
        url = u"http://somesite.au"
        self.assertTrue(IsHtmlUrl(url))

    def test_mpg_url(self):
        """
        Tests that a URL ending with mpg does not register as valid.
        """
        url = u"http://wbsrch.com/tutorial.mpg"
        self.assertFalse(IsHtmlUrl(url))

    def test_swf_url(self):
        """
        Tests that a URL ending with swf does not register as valid.
        """
        url = u"http://wbsrch.com/tutorial.swf"
        self.assertFalse(IsHtmlUrl(url))

    def test_apk_url(self):
        """
        Tests that a URL ending with apk does not register as valid.
        """
        url = u"http://wbsrch.com/tutorial.apk"
        self.assertFalse(IsHtmlUrl(url))

    def test_jpg_url(self):
        """
        Tests that a URL ending with JPG does not register as valid. Upper to test case-insensitive match.
        """
        url = u"http://wbsrch.com/tutorial.JPG"
        self.assertFalse(IsHtmlUrl(url))

    def test_jpeg_url(self):
        """
        Tests that a URL ending with Jpeg does not register as valid. Upper to test case-insensitive match.
        """
        url = u"http://wbsrch.com/tutorial.Jpeg"
        self.assertFalse(IsHtmlUrl(url))

    def test_long_https_jpeg_url(self):
        """
        Tests that a URL ending with Jpeg does not register as valid. Upper to test case-insensitive match.
        """
        url = u"https://wbsrch.com/site/images/tutorial.jpeg"
        self.assertFalse(IsHtmlUrl(url))

class BlockedDomainTestCase(TestCase):
    def setUp(self):
        site = BlockedSite()
        site.url = u'www.yandex.ru'
        site.reason = 8
        site.save()

    def test_root_url(self):
        url = u'http://www.yandex.ru'
        rooturl = GetRootUrl(url)
        blocked_domain = BlockedSite.objects.filter(url=rooturl)
        self.assertEqual(blocked_domain.count(), 1)

    def test_rootslash_url(self):
        url = u'http://www.yandex.ru/'
        rooturl = GetRootUrl(url)
        blocked_domain = BlockedSite.objects.filter(url=rooturl)
        self.assertEqual(blocked_domain.count(), 1)

    def test_full_url(self):
        url = u'http://www.yandex.ru/index/'
        rooturl = GetRootUrl(url)
        blocked_domain = BlockedSite.objects.filter(url=rooturl)
        self.assertEqual(blocked_domain.count(), 1)

    def test_subdomain_url(self):
        url = u'http://en.yandex.ru'
        rooturl = GetRootUrl(url)
        blocked_domain = BlockedSite.objects.filter(url=rooturl)
        self.assertEqual(blocked_domain.count(), 0)

    def test_safe_url(self):
        url = u'http://www.google.com'
        rooturl = GetRootUrl(url)
        blocked_domain = BlockedSite.objects.filter(url=rooturl)
        self.assertEqual(blocked_domain.count(), 0)

    def tearDown(self):
        site = BlockedSite.objects.get(url=u'www.yandex.ru')
        site.delete()

# Tests conditions for crawling and recrawling a url.
class CanCrawlUrlTestCase(TestCase):
    def setUp(self):
        site = BlockedSite()
        site.url = u'www.yandex.ru'
        site.reason = 8
        site.save()
        site = BlockedSite()
        site.url = u'morespamsite.com'
        site.reason = 7
        site.exclude_subdomains = True
        site.save()
        domain = DomainInfo()
        domain.url = u'www.spamsite.com'
        domain.max_urls = 1
        domain.save()
        domain = DomainInfo()
        domain.url = u'www.italiansite.it'
        domain.max_urls = 1
        domain.language_association = 'it'
        domain.save()
        domain = DomainInfo()
        domain.url = u'english.somesite.cn'
        domain.language_association = 'en'
        domain.save()
        domain = DomainInfo()
        domain.url = u'www.othersite.com'
        domain.max_urls = 1000
        domain.save()
        info = SiteInfo()
        info.rooturl = u'www.spamsite.com'
        info.url = u'http://www.spamsite.com/1/'
        info.save()
        info = SiteInfo()
        info.rooturl = u'www.spamsite.com'
        info.url = u'http://www.spamsite.com/2/'
        info.save()
        info = SiteInfo_it()
        info.rooturl = u'www.italiansite.it'
        info.url = u'http://www.italiansite.it/'
        info.save()
        domainext = DomainSuffix()
        domainext.extension = '.hr'
        domainext.default_language = 'hr'
        domainext.save()
        domainext = DomainSuffix()
        domainext.extension = '.cn'
        domainext.no_new_domain_urls = True
        domainext.save()

    def test_safe_url(self):
        url = u'http://wbsrch.com'
        self.assertTrue(CanCrawlUrl(url))

    def test_safe_recrawl_url(self):
        url = u'http://wbsrch.com'
        self.assertTrue(CanReCrawlUrl(url))

    def test_safe_short_url(self):
        url = u'wbsrch.com'
        self.assertTrue(CanCrawlUrl(url))

    def test_safe_recrawl_url2(self):
        url = u'wbsrch.com/admin/dir/siteinfo/'
        self.assertTrue(CanReCrawlUrl(url))

    def test_safe_recrawl_url3(self):
        url = u'http://somesite.au'
        self.assertTrue(CanReCrawlUrl(url))

    def test_bad_url(self):
        url = u'http://wbsrch.com/tutorial.mp3'
        self.assertFalse(CanCrawlUrl(url))

    def test_another_bad_url(self):
        url = u'https://wbsrch.com/images/en/tutorial.jpg'
        self.assertFalse(CanCrawlUrl(url))

    def test_bad_short_url(self):
        url = u'wbsrch.com/tutorial.mp3'
        self.assertFalse(CanCrawlUrl(url))

    def test_blocked_url(self):
        url = u'http://www.yandex.ru'
        self.assertFalse(CanCrawlUrl(url))

    def test_blocked_url2(self):
        url = u'http://morespamsite.com'
        self.assertFalse(CanCrawlUrl(url))

    def test_blocked_url3(self):
        url = u'http://spampage.morespamsite.com'
        self.assertFalse(CanCrawlUrl(url))

    def test_blocked_short_url(self):
        url = u'www.yandex.ru'
        self.assertFalse(CanCrawlUrl(url))

    def test_blocked_extension_url(self):
        url = u'www.taobao.cn'
        self.assertFalse(CanCrawlUrl(url))

    def test_blocked_extension_url(self):
        url = u'www.taobao.cn'
        self.assertTrue(CanReCrawlUrl(url))

    def test_blocked_extension_allowed_domain_url(self):
        url = u'http://english.somesite.cn/some_url.htm'
        self.assertTrue(CanCrawlUrl(url))

    def test_allowed_extension_url(self):
        url = u'www.croatia.hr'
        self.assertTrue(CanCrawlUrl(url))

    def test_maxxed_url(self):
        url = u'http://www.spamsite.com'
        self.assertFalse(CanCrawlUrl(url))

    def test_maxxed_recrawl_url(self):
        url = u'http://www.spamsite.com'
        self.assertTrue(CanReCrawlUrl(url))

    def test_maxxed_language_url(self):
        url = u'http://www.italiansite.it/url/'
        self.assertFalse(CanCrawlUrl(url))

    def test_unmaxxed_url(self):
        url = u'http://www.othersite.com'
        self.assertTrue(CanCrawlUrl(url))

    def test_maxxed_short_url(self):
        url = u'www.spamsite.com'
        self.assertFalse(CanCrawlUrl(url))

    def tearDown(self):
        for site in BlockedSite.objects.all():
            site.delete()
        domain = DomainInfo.objects.get(url=u'www.spamsite.com')
        domain.delete()
        url = SiteInfo.objects.get(url=u'http://www.spamsite.com/1/')
        url.delete()
        url = SiteInfo.objects.get(url=u'http://www.spamsite.com/2/')
        url.delete()

class NormalizeUrlTestCase(TestCase):
    def test_normal_url(self):
        url = u'http://wbsrch.com/tutorial.htm'
        self.assertEqual(NormalizeUrl(url), u'http://wbsrch.com/tutorial.htm')

    def test_normal_url2(self):
        url = u'http://wbsrch.com'
        self.assertEqual(NormalizeUrl(url), u'http://wbsrch.com')

    def test_normal_url2(self):
        url = u'http://wbsrch.com/'
        self.assertEqual(NormalizeUrl(url), u'http://wbsrch.com/')

    def test_jsession_url(self):
        url = u'http://farm.myswitzerland.com/on-the-farm/Airolojsessionid=94AFB92FD66F248EC3EF279B7A6732EF'
        self.assertEqual(NormalizeUrl(url), u'http://farm.myswitzerland.com/on-the-farm/Airolo')

    def test_jsession_url2(self):
        url = u'https://secure2.convio.net/fmnh/site/SPageServer/jsessionid=F1C5BEC5FD279BA9953C87FD37D5F89D.app274b?donate=now&pagename=api_donate'
        self.assertEqual(NormalizeUrl(url), u'https://secure2.convio.net/fmnh/site/SPageServer/?donate=now&pagename=api_donate')

    def test_jsession_url3(self):
        url = u'https://www.psiservice.com/psiweb/index.jsp;jsessionid=450B52BF0268B30DE854C552309E3E6A'
        self.assertEqual(NormalizeUrl(url), u'https://www.psiservice.com/psiweb/index.jsp')

    def test_jsession_url4(self):
        url = u'http://sage-ereference.com/publicstart;jsessionid=169E7071B011936163BDD68A0C95BD32?authRejection=true'
        self.assertEqual(NormalizeUrl(url), u'http://sage-ereference.com/publicstart?authRejection=true')

    def test_doubleslash_url(self):
        url = u'//wbsrch.com/tutorial.htm'
        self.assertEqual(NormalizeUrl(url), u'http://wbsrch.com/tutorial.htm')

    def test_another_normal_url(self):
        url = u'http://wbsrch.com/tutorial/'
        self.assertEqual(NormalizeUrl(url), u'http://wbsrch.com/tutorial/')

    def test_third_normal_url(self):
        url = u'http://wbsrch.com/tutorial'
        self.assertEqual(NormalizeUrl(url), u'http://wbsrch.com/tutorial')

    def test_query_url(self):
        url = u'http://wbsrch.com/search/?q=term&r=termtwo'
        self.assertEqual(NormalizeUrl(url), u'http://wbsrch.com/search/?q=term&r=termtwo')

    def test_another_query_url(self):
        url = u'http://wbsrch.com/index.php?q=term&r=termtwo'
        self.assertEqual(NormalizeUrl(url), u'http://wbsrch.com/index.php?q=term&r=termtwo')

    def test_sessionid_url(self):
        url = u'http://wbsrch.com/index.php?q=term&r=termtwo&PHPSESSID=1234567abc'
        self.assertEqual(NormalizeUrl(url), u'http://wbsrch.com/index.php?q=term&r=termtwo')

    def test_utm_url(self):
        url = u'http://wbsrch.com/index.php?q=term&r=termtwo&utm_source=abc&utm_medium=def&utm_campaign=456&utm_term=789&utm_content=123'
        self.assertEqual(NormalizeUrl(url), u'http://wbsrch.com/index.php?q=term&r=termtwo')

    def test_sessionid_lower_url(self):
        url = u'http://wbsrch.com/index.php?q=term&r=termtwo&jsessionid=1234567abc'
        self.assertEqual(NormalizeUrl(url), u'http://wbsrch.com/index.php?q=term&r=termtwo')

    def test_justsessionid_url(self):
        url = u'http://wbsrch.com/index.php?zenid=1234567abc'
        self.assertEqual(NormalizeUrl(url), u'http://wbsrch.com/index.php')

    def test_fragment_url(self):
        url = u'http://wbsrch.com/tutorial.htm#fragment'
        self.assertEqual(NormalizeUrl(url), u'http://wbsrch.com/tutorial.htm')

    def test_https_subdomain_url(self):
        url = u'https://el.wbsrch.com/tutorial.htm'
        self.assertEqual(NormalizeUrl(url), u'https://el.wbsrch.com/tutorial.htm')

    def test_port_url(self):
        url = u'https://wbsrch.com:8080/tutorial.htm'
        self.assertEqual(NormalizeUrl(url), u'https://wbsrch.com:8080/tutorial.htm')

    def test_capital_url(self):
        url = u'https://DE.WBSRCH.COM/tutorial.htm'

        self.assertEqual(NormalizeUrl(url), u'https://de.wbsrch.com/tutorial.htm')

    def test_capital_after_url(self):
        url = u'https://es.wbsrch.com/TUTORIAL_AND_WHATNOT.HTM'
        self.assertEqual(NormalizeUrl(url), u'https://es.wbsrch.com/TUTORIAL_AND_WHATNOT.HTM')

    def test_mixed_capital_url(self):
        url = u'https://fr.WBSRCH.com/TUTORIAL_and_WHATNOT.htm'
        self.assertEqual(NormalizeUrl(url), u'https://fr.wbsrch.com/TUTORIAL_and_WHATNOT.htm')

class MakeRealUrlTestCase(TestCase):
    def test_doubleslash_domain_url(self):
        url = u'//wbsrch.com/tutorial.htm'
        self.assertEqual(MakeRealUrl(url), u'http://wbsrch.com/tutorial.htm')

    def test_slash_url(self):
        url = u'/tutorial.htm'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://wbsrch.com/tutorial.htm')

    def test_slash_url2(self):
        url = u'/tutorial.html'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://wbsrch.com/tutorial.html')

    def test_slash_url3(self):
        url = u'/tutorial.php'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://wbsrch.com/tutorial.php')

    def test_slash_url4(self):
        url = u'//tutorial.php'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://wbsrch.com/tutorial.php')

    def test_colonslash_url4(self):
        url = u'://tutorial.php'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://wbsrch.com/tutorial.php')

    def test_slash_url5(self):
        url = u'/tutorial/tutorial.htm'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://wbsrch.com/tutorial/tutorial.htm')

    def test_doubleslash_url(self):
        url = u'//tutorial.htm'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://wbsrch.com/tutorial.htm')

    def test_doubleslash_url2(self):
        url = u'//tutorial/cheese/burgers/'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://wbsrch.com/tutorial/cheese/burgers/')

    def test_doubleslash_url3(self):
        url = u'//tutorial/'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://wbsrch.com/tutorial/')

    def test_doubleslash_domainurl(self):
        url = u'//wbsrch.com/tutorial/'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://wbsrch.com/tutorial/')

    def test_doubleslash_domainurl2(self):
        url = u'//wbsrch.com'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://wbsrch.com')

    def test_doubleslash_domainurl3(self):
        url = u'//wbsrch.com/tutorial.htm'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://wbsrch.com/tutorial.htm')

    def test_colondoubleslash_domainurl(self):
        url = u'://wbsrch.com/tutorial.htm'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://wbsrch.com/tutorial.htm')

    def test_doubleslash_domainurl4(self):
        url = u'//wbsrch.com/'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://wbsrch.com/')

    def test_doubleslash_domainurl5(self):
        url = u'//wbsrch.com/tutorial/cheese/crackers/'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://wbsrch.com/tutorial/cheese/crackers/')

    def test_doubleslash_domainurl6(self):
        url = u'//someothersite.com'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://someothersite.com')

    def test_doubleslash_domainurl7(self):
        url = u'//someothersite.com/tutorial.htm'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://someothersite.com/tutorial.htm')

    def test_normal_url(self):
        url = u'http://wbsrch.com/tutorial'
        self.assertEqual(MakeRealUrl(url), u'http://wbsrch.com/tutorial')

    def test_query_url(self):
        url = u'http://wbsrch.com/search/?q=term&r=termtwo'
        self.assertEqual(MakeRealUrl(url), u'http://wbsrch.com/search/?q=term&r=termtwo')

    def test_doubleslash_query_url(self):
        url = u'//wbsrch.com/index.php?q=term&r=termtwo'
        self.assertEqual(MakeRealUrl(url), u'http://wbsrch.com/index.php?q=term&r=termtwo')

    def test_sessionid_url(self):
        url = u'wbsrch.com/index.php?q=term&r=termtwo&PHPSESSID=1234567abc'
        self.assertEqual(MakeRealUrl(url), u'http://wbsrch.com/index.php?q=term&r=termtwo')

    def test_secure_utm_url(self):
        url = u'https://wbsrch.com/index.php?q=term&r=termtwo&utm_source=abc&utm_medium=def&utm_campaign=456&utm_term=789&utm_content=123'
        self.assertEqual(MakeRealUrl(url), u'https://wbsrch.com/index.php?q=term&r=termtwo')

    def test_javascript_url(self):
        url = u'javascript:void(0)'
        self.assertEqual(MakeRealUrl(url), u'javascript:void(0)')

    def test_mailto_url(self):
        url = u'mailto:bob@bob.com'
        self.assertEqual(MakeRealUrl(url), u'mailto:bob@bob.com')

    def test_fileurlwithsessionid_url(self):
        url = u'index.php?zenid=1234567abc'
        self.assertEqual(MakeRealUrl(url, u'wbsrch.com'), u'http://wbsrch.com/index.php')

    def test_fragment_url(self):
        url = u'wbsrch.com/tutorial.htm#fragment'
        self.assertEqual(MakeRealUrl(url), u'http://wbsrch.com/tutorial.htm')

    def test_https_subdomain_url(self):
        url = u'https://el.wbsrch.com/tutorial.htm'
        self.assertEqual(MakeRealUrl(url), u'https://el.wbsrch.com/tutorial.htm')

    def test_port_url(self):
        url = u'https://wbsrch.com:8080/tutorial.htm'
        self.assertEqual(MakeRealUrl(url), u'https://wbsrch.com:8080/tutorial.htm')

    def test_capital_url(self):
        url = u'https://DE.WBSRCH.COM/tutorial.htm'
        self.assertEqual(MakeRealUrl(url), u'https://de.wbsrch.com/tutorial.htm')

    def test_capital_after_url(self):
        url = u'//es.wbsrch.com/TUTORIAL_AND_WHATNOT.HTM'
        self.assertEqual(MakeRealUrl(url), u'http://es.wbsrch.com/TUTORIAL_AND_WHATNOT.HTM')

    def test_mixed_capital_url(self):
        url = u'fr.WBSRCH.com/TUTORIAL_and_WHATNOT.htm'
        self.assertEqual(MakeRealUrl(url), u'http://fr.wbsrch.com/TUTORIAL_and_WHATNOT.htm')

class InfixLanguageTestCase(TestCase):
    def test_english_infix(self):
        url = u'https://www.wbsrch.com/en/welcome.htm'
        self.assertEqual(u'en', GetInfixLanguage(url))

    def test_no_infix(self):
        url = u'https://wbsrch.com/'
        self.assertIsNone(GetInfixLanguage(url))

    def test_swahili_infix(self):
        url = u'https://wbsrch.com/swahili/web/site/'
        self.assertEqual(u'sw', GetInfixLanguage(url))

    def test_danish_infix(self):
        url = u'http://www.sbs.com.au/yourlanguage/danish/'
        self.assertEqual(u'da', GetInfixLanguage(url))

    def test_german_infix(self):
        url = u'http://www.sbs.com.au/yourlanguage/german/'
        self.assertEqual(u'de', GetInfixLanguage(url))

    def test_de_de_infix(self):
        url = u'http://www.example.com/de-de/index/'
        self.assertEqual(u'de', GetInfixLanguage(url))

    def test_fr_fr_infix(self):
        url = u'http://www.example.com/fr-fr/'
        self.assertEqual(u'fr', GetInfixLanguage(url))

    def test_fr_fr_uppercaseinfix(self):
        url = u'http://www.example.com/fr-FR/'
        self.assertEqual(u'fr', GetInfixLanguage(url))

    def test_fr_fr_uppercaseunderscoreinfix(self):
        url = u'http://www.example.com/fr_FR/'
        self.assertEqual(u'fr', GetInfixLanguage(url))

    def test_fr_fr_underscoreinfix(self):
        url = u'http://www.example.com/fr_fr/'
        self.assertEqual(u'fr', GetInfixLanguage(url))

    def test_sv_se_infix(self):
        url = u'http://www.example.com/sv-se/'
        self.assertEqual(u'sv', GetInfixLanguage(url))

    def test_sv_se_underscoreinfix(self):
        url = u'http://www.example.com/sv_se/'
        self.assertEqual(u'sv', GetInfixLanguage(url))

    def test_fr_ch_infix(self):
        url = u'http://www.example.com/fr-ch/index.htm'
        self.assertEqual(u'fr', GetInfixLanguage(url))

    def test_en_za_infix(self):
        url = u'http://www.example.com/en-za/site/index/'
        self.assertEqual(u'en', GetInfixLanguage(url))

    def test_es_es_infix(self):
        url = u'http://www.example.com/es-es/index.htm'
        self.assertEqual(u'es', GetInfixLanguage(url))

    def test_uppercase_infix(self):
        url = u'http://www.example.com/SW/index.htm'
        self.assertEqual(u'sw', GetInfixLanguage(url))

    def test_it_it_infix(self):
        url = u'http://www.example.com/it-it/index/page.htm'
        self.assertEqual(u'it', GetInfixLanguage(url))

    def test_langname_infix(self):
        url = u'http://www.example.com/italian/index/page.htm'
        self.assertEqual(u'it', GetInfixLanguage(url))

    def test_shortlangname_infix(self):
        url = u'http://www.example.com/por/index/page.htm'
        self.assertEqual(u'pt', GetInfixLanguage(url))

    def test_ru_infix(self):
        url = u'http://www.example.com/ru/index/page.htm'
        language = None
        try:
            GetInfixLanguage(url)
        except InvalidLanguageException, e:
            self.assertEqual(e.language, u'ru')

    def test_zh_cn_infix(self):
        url = u'http://www.example.com/zh-cn/index/page.htm'
        language = None
        try:
            GetInfixLanguage(url)
        except InvalidLanguageException, e:
            self.assertEqual(e.language, u'zh')

    def test_uk_uk_infix(self):
        url = u'http://www.example.com/uk-UA/index/page.htm'
        language = None
        try:
            GetInfixLanguage(url)
        except InvalidLanguageException, e:
            self.assertEqual(e.language, u'uk')

    def test_somali_infix(self):
        url = u'http://www.bbc.co.uk/somali/topics/video'
        self.assertEqual(u'so', GetInfixLanguage(url))

    def test_somali_infix_again(self):
        url = u'http://www.bbc.co.uk/somali'
        self.assertEqual(u'so', GetInfixLanguage(url))

    def test_hausa_infix(self):
        url = u'https://wbsrch.com/hausa'
        self.assertEqual(u'ha', GetInfixLanguage(url))

    def test_turkce__infix(self):
        url = u'https://wbsrch.com/turkce/index.htm'
        self.assertEqual(u'tr', GetInfixLanguage(url))

    def test_portuguese_infix(self):
        url = u'https://wbsrch.com/portuguese'
        self.assertEqual(u'pt', GetInfixLanguage(url))

    def test_invalid_infix(self):
        url = u'https://wbsrch.com/de-ca/welcome.htm'
        self.assertIsNone(GetInfixLanguage(url))

    def test_no_infix_with_prefix(self):
        url = u'https://de.wbsrch.com/welcome.htm'
        self.assertIsNone(GetInfixLanguage(url))

    def test_french_infix(self):
        url = u'https://www.wbsrch.com/fr/welcome/index.php'
        self.assertEqual(u'fr', GetInfixLanguage(url))

class PageLanguageTestCase(TestCase):
    def test_get_page_language(self):
        url = u'http://de.wbsrch.de/de/welcome.htm'
        html = u'<html lang="de"><head><title>Title</title><meta name="Content-Language" content="de"></head><body>Hallo, Deutschland.</body></html>'
        self.assertEqual(IdentifyPageLanguage(url, html)[0], 'de')

    def test_get_page_language_prefix(self):
        url = u'http://lv.wbsrch.com'
        html = u'<html><head><title>&nbsp;</title></head><body>&nbsp;</body></html>'
        self.assertEqual(IdentifyPageLanguage(url, html)[0], 'lv')

    def test_get_page_badlanguage_prefix(self):
        url = u'http://ja.wbsrch.com'
        html = u'<html><head><title>&nbsp;</title></head><body>&nbsp;</body></html>'
        self.assertEqual(IdentifyPageLanguage(url, html)[0], 'ja')

    def test_get_page_badlanguage_suffix(self):
        url = u'http://wbsrch.az'
        html = u'<html><head><title>&nbsp;</title></head><body>&nbsp;</body></html>'
        self.assertEqual(IdentifyPageLanguage(url, html)[0], 'az')

    def test_get_page_language_infix(self):
        url = u'http://wbsrch.com/sv/page/'
        html = u'<html><head><title>&nbsp;</title></head><body>&nbsp;</body></html>'
        self.assertEqual(IdentifyPageLanguage(url, html)[0], 'sv')

    def test_get_blocked_page_language_infix(self):
        url = u'http://wbsrch.com/ru/page/'
        html = u'<html><head><title>&nbsp;</title></head><body>&nbsp;</body></html>'
        self.assertEqual(IdentifyPageLanguage(url, html)[0], 'ru')

    def test_get_locale_language_infix(self):
        url = u'http://wbsrch.com/es-ar/page/'
        html = u'<html><head><title>&nbsp;</title></head><body>&nbsp;</body></html>'
        self.assertEqual(IdentifyPageLanguage(url, html)[0], 'es')

    def test_get_blocked_locale_language_infix(self):
        url = u'http://wbsrch.com/ar-eg/page/'
        html = u'<html><head><title>&nbsp;</title></head><body>&nbsp;</body></html>'
        self.assertEqual(IdentifyPageLanguage(url, html)[0], 'ar')

class DomainExtensionTestCase(TestCase):
   def test_de_extension(self):
       domain = 'http://website.de'
       self.assertEqual('.de', GetDomainExtension(domain))

   def test_com_extension(self):
       domain = 'example.com'
       self.assertEqual('.com', GetDomainExtension(domain))

   def test_subdomain_extension(self):
       domain = 'http://en.us.wbsrch.com'
       self.assertEqual('.com', GetDomainExtension(domain))

   def test_no_extension(self):
       domain = 'domain-name'
       self.assertEqual('domain-name', GetDomainExtension(domain))

class DomainExtensionLanguageTestCase(TestCase):
    def setUp(self):
        domain = DomainSuffix()
        domain.extension = '.hr'
        domain.default_language = 'hr'
        domain.save()

    def test_croatian_extension(self):
        domain = 'website.hr'
        self.assertEqual('hr', GetLanguageFromDomainExtension(domain))

    def test_dotcom_extension(self):
        domain = 'website.com'
        self.assertIsNone(GetLanguageFromDomainExtension(domain))

    def test_no_extension(self):
        domain = 'http://website'
        self.assertIsNone(GetLanguageFromDomainExtension(domain))

    def test_untagged_extension(self):
        domain = 'http://website.travel'
        self.assertIsNone(GetLanguageFromDomainExtension(domain))

    def test_subdomains_and_croatian_extension(self):
        domain = 'http://website.in.croatian.hr'
        self.assertEqual('hr', GetLanguageFromDomainExtension(domain))

    def tearDown(self):
        for domain in DomainSuffix.objects.all():
            domain.delete()

class LanguageModelTestCase(TestCase):
    def setUp(self):
        pass

    def test_de_index(self):
        model = GetIndexModelFromLanguage('de')
        self.assertEqual(model, IndexTerm_de)

    def test_en_US_index(self):
        model = GetIndexModelFromLanguage('en-US')
        self.assertEqual(model, IndexTerm)

    def test_en_index(self):
        model = GetIndexModelFromLanguage('en')
        self.assertEqual(model, IndexTerm)

    def test_empty_index(self):
        model = GetIndexModelFromLanguage(None)
        self.assertEqual(model, IndexTerm)

    def test_zh_index(self):
        self.assertRaises(InvalidLanguageException, GetIndexModelFromLanguage, 'zh')

    def test_de_pend(self):
        model = GetPendingIndexModelFromLanguage('de')
        self.assertEqual(model, PendingIndex_de)

    def test_en_US_pend(self):
        model = GetPendingIndexModelFromLanguage('en-US')
        self.assertEqual(model, PendingIndex)

    def test_en_pend(self):
        model = GetPendingIndexModelFromLanguage('en')
        self.assertEqual(model, PendingIndex)

    def test_empty_pend(self):
        model = GetPendingIndexModelFromLanguage(None)
        self.assertEqual(model, PendingIndex)

    def test_zh_pend(self):
        self.assertRaises(InvalidLanguageException, GetPendingIndexModelFromLanguage, 'zh')

    def test_de_url(self):
        model = GetSiteInfoModelFromLanguage('de')
        self.assertEqual(model, SiteInfo_de)

    def test_en_US_url(self):
        model = GetSiteInfoModelFromLanguage('en-US')
        self.assertEqual(model, SiteInfo)

    def test_en_url(self):
        model = GetSiteInfoModelFromLanguage('en')
        self.assertEqual(model, SiteInfo)

    def test_empty_url(self):
        model = GetSiteInfoModelFromLanguage(None)
        self.assertEqual(model, SiteInfo)

    def test_zh_url(self):
        self.assertRaises(InvalidLanguageException, GetSiteInfoModelFromLanguage, 'zh')

    def test_de_log(self):
        model = GetSearchLogModelFromLanguage('de')
        self.assertEqual(model, SearchLog_de)

    def test_en_US_log(self):
        model = GetSearchLogModelFromLanguage('en-US')
        self.assertEqual(model, SearchLog)

    def test_en_log(self):
        model = GetSearchLogModelFromLanguage('en')
        self.assertEqual(model, SearchLog)

    def test_empty_log(self):
        model = GetSearchLogModelFromLanguage(None)
        self.assertEqual(model, SearchLog)

    def test_zh_log(self):
        self.assertRaises(InvalidLanguageException, GetSearchLogModelFromLanguage, 'zh')

    def test_de_url(self):
        model = GetKeywordRankingModelFromLanguage('de')
        self.assertEqual(model, KeywordRanking_de)

    def test_en_US_url(self):
        model = GetKeywordRankingModelFromLanguage('en-US')
        self.assertEqual(model, KeywordRanking)

    def test_en_url(self):
        model = GetKeywordRankingModelFromLanguage('en')
        self.assertEqual(model, KeywordRanking)

    def test_empty_url(self):
        model = GetKeywordRankingModelFromLanguage(None)
        self.assertEqual(model, KeywordRanking)

    def tearDown(self):
        pass

class UpdateAlexaRankTestCase(TestCase):
    def setUp(self):
        domain = DomainInfo()
        domain.url = u'www.spamsite.com'
        domain.alexa_rank = 999
        domain.save()
        domain = DomainInfo()
        domain.url = u'spamsite.com'
        domain.alexa_rank = 998
        domain.save()
        domain = DomainInfo()
        domain.url = u'spamsite2.com'
        domain.alexa_rank = 997
        domain.save()
        domain = DomainInfo()
        domain.url = u'www.spamsite3.com'
        domain.alexa_rank = 996
        domain.save()
        domain = DomainInfo()
        domain.url = u'spamsite4.com'
        domain.alexa_rank = 995
        domain.save()
        domain = DomainInfo()
        domain.url = u'www.spamsite4.com'
        domain.alexa_rank = 994
        domain.save()
        domain = DomainInfo()
        domain.url = u'www.spamsite6.com'
        domain.alexa_rank = 993
        domain.save()

    def test_update_raw_url(self):
        url = u'spamsite2.com'
        rank = 100
        UpdateAlexaRank(url, rank)
        domain = DomainInfo.objects.get(url=url)
        self.assertEqual(domain.alexa_rank, rank)
        # TODO: Assert exception if we query www.spamsite2.com

    def test_update_www_url(self):
        url = u'www.spamsite3.com'
        rank = 200
        UpdateAlexaRank(url, rank)
        domain = DomainInfo.objects.get(url=url)
        self.assertEqual(domain.alexa_rank, rank)
        # TODO: Assert exception if we query spamsite3.com

    def test_update_www_url_and_base(self):
        url = u'www.spamsite.com'
        baseurl = u'spamsite.com'
        rank = 300
        UpdateAlexaRank(url, rank)
        domain = DomainInfo.objects.get(url=url)
        self.assertEqual(domain.alexa_rank, rank)
        domain = DomainInfo.objects.get(url=baseurl)
        self.assertEqual(domain.alexa_rank, rank)
        pass

    def test_update_base_url_and_www(self):
        url = u'spamsite4.com'
        wwwurl = u'www.spamsite4.com'
        rank = 400
        UpdateAlexaRank(url, rank)
        domain = DomainInfo.objects.get(url=url)
        self.assertEqual(domain.alexa_rank, rank)
        domain = DomainInfo.objects.get(url=wwwurl)
        self.assertEqual(domain.alexa_rank, rank)

    def test_add_new_url(self):
        url = u'spamsite5.com'
        rank = 500
        UpdateAlexaRank(url, rank)
        domain = DomainInfo.objects.get(url=url)
        self.assertEqual(domain.alexa_rank, rank)
        # TODO: Assert exception if we query www.spamsite5.com

    def test_add_new_url_existing_www(self):
        url = u'spamsite6.com'
        wwwurl = u'www.spamsite6.com'
        rank = 500
        UpdateAlexaRank(url, rank)
        domain = DomainInfo.objects.get(url=url)
        self.assertEqual(domain.alexa_rank, rank)
        domain = DomainInfo.objects.get(url=wwwurl)
        self.assertEqual(domain.alexa_rank, rank)

    def tearDown(self):
        for obj in DomainInfo.objects.all():
            obj.delete()

class RecrawlUrlTestCase(TestCase):
    def setUp(self):
        info = SiteInfo()
        info.rooturl = u'wbsrch.com'
        info.url = u'http://wbsrch.com/'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagecontents = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.save()
        info = SiteInfo()
        info.rooturl = u'wbsrch.com'
        info.url = u'http://wbsrch.com/search/'
        info.lastcrawled = timezone.now()
        info.pagecontents = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.save()
        info = SiteInfo()
        info.rooturl = u'wbsrch.com'
        info.url = u'http://wbsrch.com/changelog/'
        info.lastcrawled = timezone.now() - timedelta(days=5)
        info.pagecontents = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.save()
        info = SiteInfo()
        info.rooturl = u'wbsrch.com'
        info.url = u'http://wbsrch.com/privacy/'
        info.lastcrawled = timezone.now() - timedelta(days=3)
        info.pagecontents = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.save()
        info = SiteInfo()
        info.rooturl = u'wbsrch.com'
        info.url = u'http://wbsrch.com/policy/'
        info.lastcrawled = timezone.now() - timedelta(days=9)
        info.pagecontents = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.save()

    def test_nothing(self):
        pass

    def tearDown(self):
        for item in SiteInfo.objects.all():
            item.delete()

class MarkURLAsSpamTestCase(TestCase):
    def setUp(self):
        pass

    def test_spam_comment(self):
        spamhtml = '<strong><em><a href="http://michaelkorscanadaoutlet.drainducks.com">michael kors canada</a></em></strong>|<strong><em><a href="http://michaelkorscanadaoutlet.drainducks.com">michael kors canada</a></em></strong>|<strong><em><a href="http://michaelkorscanadaoutlet.drainducks.com">michael kors canada</a></em></strong>|<strong><em><a href="http://michaelkorscanadaoutlet.drainducks.com">michael kors canada</a></em></strong>|<strong><em><a href="http://michaelkorscanadaoutlet.drainducks.com">michael kors canada</a></em></strong>|<strong><em><a href="http://michaelkorscanadaoutlet.drainducks.com">michael kors canada</a></em></strong>|<strong><em><a href="http://michaelkorscanadaoutlet.drainducks.com">michael kors canada</a></em></strong>|<strong><em><a href="http://michaelkorscanadaoutlet.drainducks.com">michael kors canada</a></em></strong>|<strong><em><a href="http://michaelkorscanadaoutlet.drainducks.com">michael kors canada</a></em></strong>|<strong><em><a href="http://michaelkorscanadaoutlet.drainducks.com">michael kors canada</a></em></strong>'
        MarkURLContentsAsSpam(spamhtml)
        url = 'michaelkorscanadaoutlet.drainducks.com'
        domain = DomainInfo.objects.get(url=url)
        self.assertEqual(domain.rank_reason, 7)
        self.assertEqual(domain.rank_adjustment, -2)
        self.assertEqual(domain.notes, 'Spam link(s) posted by bot.')

    def test_spam_comment_ip(self):
        spamhtml = '<html><head><title>Spam</title></head><body>Spam!</body></html>'
        ip = '192.168.1.255'
        MarkURLContentsAsSpam(spamhtml,ip)
        address = IPAddress.objects.get(ip=ip)
        self.assertEqual(address.spam_commenter, True)

    def tearDown(self):
        for item in DomainInfo.objects.all():
            item.delete()
        for item in IPAddress.objects.all():
            item.delete()

# If these fail for lack of a corpus, do this at a Python shell prompt:
# To get corpus, and others.
# import nltk
# nltk.download()
# Get: langid, punkt, stopwords by typing 'd' and then entering the name one by one.
class NLTKTestCase(TestCase):
    def setUp(self):
        pass

    def testGerman1(self):
        result = NLTKLanguageDetect('Ich bin ein Berliner mit bier und kase fur die mitlied am donnerstag.')
        self.assertEqual(result, 'german')

    def testGerman2(self):
        result = NLTKLanguageDetect('Die frau ist blau am samstag und wir sind nacht ohne dich.')
        self.assertEqual(result, 'german')

    def testEnglish1(self):
        result = NLTKLanguageDetect('The cow jumped over the moon and the dish ran off with the spoon to get married in Las Vegas.')
        self.assertEqual(result, 'english')

    def testEnglish2(self):
        result = NLTKLanguageDetect('And now for something completely different, or completely the same. I do not know whether we are watching the show.')
        self.assertEqual(result, 'english')

    def testSpanish1(self):
        result = NLTKLanguageDetect('Conozco que usted comer por la comida, pero no necesito voy al cine con mucho gusto.')
        self.assertEqual(result, 'spanish')

    def testSpanish2(self):
        result = NLTKLanguageDetect('Me gusta cerveza todo los tiempos. Queso blanco es en mis pantalones y mi camiseta.')
        self.assertEqual(result, 'spanish')

    def tearDown(self):
        pass

class CrawlerTestCase(TestCase):
    htmlpage = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
              <html xmlns="http://www.w3.org/1999/xhtml">
              <head>
              <style type="text/css">
              @import url(/css/powells_main_20120416104528.min.css); 
              </style>
              <!-- This is a comment. -->
              <meta name="description" content="This is the content description." />
              <meta name="keywords" content="content, keywords" />
              <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
              <!-- This is a comment. -->
              <title>This is the page title.</title>
              <script type="text/javascript">
              var valuevar = 1;
              </script>
              <meta name="viewport" content="width=device-width, initial-scale=1.0" />
              </head>
              <body itemscope itemtype="http://schema.org/WebPage">
              <h1>This Is The First Head Tag</h1>
              <h1>This Is Not The First Head Tag</h1>
              <h2>This Is The First H2 Tag</h2>
              <h2>This Is Not The First Head Tag</h2>
              <h3>This Is The First H3 Tag</h3>
              <h3>This Is Not The First Head Tag</h3>
              <p>This is the page content.</p>
              </body>
              </html>"""

    def setUp(self):
        pass

    def testPopulateSiteInfo(self):
        info = SiteInfo()
        PopulateSiteInfoFromHtml(info, self.htmlpage)
        self.assertEqual(info.pagetitle, 'This is the page title.')
        self.assertEqual(info.pagedescription, 'This is the content description.')
        self.assertEqual(info.pagefirstheadtag, 'This Is The First Head Tag')
        self.assertEqual(info.pagefirsth2tag, 'This Is The First H2 Tag')
        self.assertEqual(info.pagefirsth3tag, 'This Is The First H3 Tag')
        self.assertEqual(info.pagekeywords, 'content, keywords')
        self.assertEqual(info.pagetext, 'This Is The First Head Tag This Is Not The First Head Tag This Is The First H2 Tag This Is Not The First Head Tag This Is The First H3 Tag This Is Not The First Head Tag This is the page content.')
        self.assertEqual(info.pagesize, 1062)

    def tearDown(self):
        pass

class IndexerTestCase(TestCase):

    def setUp(self):
        info = SiteInfo()
        info.rooturl = u'wbsrch.com'
        info.url = u'http://wbsrch.com/'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagecontents = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.pagedescription = 'wbsrch search engine'
        info.pagekeywords = 'wbsrch, search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.save()
        info = SiteInfo()
        info.rooturl = u'zetacentauri.com'
        info.url = u'https://zetacentauri.com/'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagecontents = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.pagekeywords = 'wbsrch, pants'
        info.save()
        info = SiteInfo()
        info.rooturl = u'zetacentauri.com'
        info.url = u'http://zetacentauri.com/'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagecontents = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.pagekeywords = 'wbsrch'
        info.save()
        info = SiteInfo()
        info.rooturl = u'zetacentauri.com'
        info.url = u'http://zetacentauri.com/page.htm'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagecontents = '<html><head><title>WbSrch</title></head><body><h1>WbSrch Search Engine</h1></body></html>'
        info.pagedescription = 'search engine'
        info.pagekeywords = 'search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.save()
        info = SiteInfo_de()
        info.rooturl = u'zetacentauri.com'
        info.url = u'http://zetacentauri.com/page.htm'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagecontents = '<html><head><title>WbSrch</title></head><body><h1>WbSrch Search Engine</h1></body></html>'
        info.pagedescription = 'search engine'
        info.pagekeywords = 'search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.save()
        info = SiteInfo_fr()
        info.rooturl = u'zeta-cen-tau.com'
        info.url = u'http://zeta-cen-tau.com/page.htm'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagecontents = '<html><head><title>WbSrch</title></head><body><h1>WbSrch Search Engine</h1></body></html>'
        info.pagedescription = 'search engine'
        info.pagekeywords = 'search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.save()
        info = SiteInfo_fr()
        info.rooturl = u'zeta-centaur.com'
        info.url = u'http://zeta-centaur.com/page.htm'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagecontents = '<html><head><title>WbSrch</title></head><body><h1>WbSrch Search Engine</h1></body></html>'
        info.pagedescription = 'search engine'
        info.pagekeywords = 'search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.save()
        info = SiteInfo_fr()
        info.rooturl = u'zetacentauri.com'
        info.url = u'http://zetacentauri.com/page.htm'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagecontents = '<html><head><title>WbSrch</title></head><body><h1>WbSrch Search Engine</h1></body></html>'
        info.pagedescription = 'search engine'
        info.pagekeywords = 'search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.save()
        info = SiteInfo_fr()
        info.rooturl = u'zetacentauri.com'
        info.url = u'http://zetacentauri.com/page_underscore.htm'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagecontents = '<html><head><title>WbSrch</title></head><body><h1>WbSrch Search Engine</h1></body></html>'
        info.pagedescription = 'search engine'
        info.pagekeywords = 'search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.save()
        info = SiteInfo_fr()
        info.rooturl = u'zetacentauri.com'
        info.url = u'http://zetacentauri.com/page_two_underscores.htm'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagecontents = '<html><head><title>WbSrch</title></head><body><h1>WbSrch Search Engine</h1></body></html>'
        info.pagedescription = 'search engine'
        info.pagekeywords = 'search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.save()
        info = SiteInfo()
        info.rooturl = u'216.151.3.15'
        info.url = u'http://216.151.3.15/xxy.z'
        info.lastcrawled = timezone.now() - timedelta(days=20)
        info.pagecontents = ' '
        info.pagedescription = ' '
        info.pagekeywords = ' '
        info.pagetitle = ' '
        info.save()

    def testIndexTerm(self):
        BuildIndexForTerm('wbsrch')
        term = IndexTerm.objects.get(keywords='wbsrch')
        self.assertEqual(term.num_results, 4)

    def testIndexGermanTerm(self):
        BuildIndexForTerm('wbsrch', lang='de')
        term = IndexTerm_de.objects.get(keywords='wbsrch')
        self.assertEqual(term.num_results, 1)

    def testIndexEmptyTerm(self):
        BuildIndexForTerm('aardvarkpants')
        term = None
        try:
            term = IndexTerm.objects.get(keywords='aardvarkpants')
        except:
            pass
        self.assertEqual(term, None)

    def testHTTPSBonus(self):
        httpurl = SiteInfo.objects.get(url=u'http://zetacentauri.com/')
        httprank = CalculateTermValue(httpurl, 'wbsrch')
        httpsurl = SiteInfo.objects.get(url=u'https://zetacentauri.com/')
        httpsrank = CalculateTermValue(httpsurl, 'wbsrch')
        self.assertTrue(httpsrank > httprank)

    def testHyphenPenalty(self):
        noh = SiteInfo_fr.objects.get(url=u'http://zetacentauri.com/page.htm')
        norank = CalculateTermValue(noh, 'zet', False, 'fr')
        oneh = SiteInfo_fr.objects.get(url=u'http://zeta-centaur.com/page.htm')
        onerank = CalculateTermValue(oneh, 'zet', False, 'fr')
        twoh = SiteInfo_fr.objects.get(url=u'http://zeta-cen-tau.com/page.htm')
        tworank = CalculateTermValue(twoh, 'zet', False, 'fr')
        self.assertGreater(norank, onerank)
        self.assertGreater(onerank, tworank)

    def testUnderscorePenalty(self):
        noh = SiteInfo_fr.objects.get(url=u'http://zetacentauri.com/page.htm')
        norank = CalculateTermValue(noh, 'zeta', False, 'fr')
        oneh = SiteInfo_fr.objects.get(url=u'http://zetacentauri.com/page_underscore.htm')
        onerank = CalculateTermValue(oneh, 'zeta', False, 'fr')
        twoh = SiteInfo_fr.objects.get(url=u'http://zetacentauri.com/page_two_underscores.htm')
        tworank = CalculateTermValue(twoh, 'zeta', False, 'fr')
        self.assertGreater(norank, onerank)
        self.assertGreater(onerank, tworank)

    def testIndexEmptyTermInPortugueseWithAvaialbleTermInEnglish(self):
        BuildIndexForTerm('wbsrch', lang='pt')
        term = None
        try:
            term = IndexTerm_pt.objects.get(keywords='wbsrch')
        except:
            pass
        self.assertEqual(term, None)

    def testMultiWordIndexTerm(self):
        BuildIndexForTerm('search engine')
        term = IndexTerm.objects.get(keywords='search engine')
        self.assertEqual(term.num_results, 2)

    def tearDown(self):
        for item in SiteInfo.objects.all():
            item.delete()
        for item in SiteInfo_de.objects.all():
            item.delete()
        for item in IndexTerm.objects.all():
            item.delete()
        for item in IndexTerm_de.objects.all():
            item.delete()

# This tests not only searching for indexed and non-indexed terms, but also the correct
# behavior of partially-indexed phrases and queueing terms for indexing.
class SearchTestCase(TestCase):
    def setUp(self):
        term = IndexTerm()
        term.keywords = "pants"
        term.page_rankings = '{}'
        term.num_results = 1
        term.search_results = "[['pants.com', {'score': 10.0, ;urls': [{'url': 'http://www.pants.com', 'score': 10, 'id': 12 }]}]]"
        term.save()
        term = IndexTerm()
        term.keywords = "chicken monkey"
        term.page_rankings = '{}'
        term.num_results = 1
        term.search_results = "[['chickenmonkey.com', {'score': 30.0, ;urls': [{'url': 'http://chickenmonkey.com', 'score': 30, 'id': 2 }]}]]"
        term.save()
        term = IndexTerm()
        term.keywords = "taco"
        term.page_rankings = '{}'
        term.num_results = 3
        term.search_results = """[
                                  ['tacos.com', {'score': 12.0, ;urls': [{'url': 'http://www.tacos.com', 'score': 12, 'id': 22 }]}],
                                  ['pants.com', {'score': 9.0, ;urls': [{'url': 'http://www.freetacos.com', 'score': 9, 'id': 32 }]}],
                                  ['pants.com', {'score': 4.0, ;urls': [{'url': 'http://www.burrito.com', 'score': 4, 'id': 42 }]}]
                                 ]"""
        term.save()
        term = IndexTerm_de()
        term.keywords = "buch"
        term.page_rankings = '{}'
        term.num_results = 1
        term.search_results = '{}'
        term.save()
        info = SiteInfo()
        info.rooturl = u'wbsrch.com'
        info.url = u'http://wbsrch.com/'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagecontents = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.pagedescription = 'wbsrch search engine'
        info.pagekeywords = 'wbsrch, search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.save()
        info = SiteInfo()
        info.rooturl = u'horsemonkey.com'
        info.url = u'http://horsemonkey.com/'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagecontents = '<html><head><title>Horse Monkey</title></head><body><h1>Horse Monkey</h1></body></html>'
        info.pagedescription = 'horse monkey'
        info.pagekeywords = 'horse monkey'
        info.pagetitle = 'Horse Monkey'
        info.save()
        info = SiteInfo_de()
        info.rooturl = u'zimmer.de'
        info.url = u'http://zimmer.de/'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagecontents = '<html><head><title>Zimmer</title></head><body><h1>Zimmer</h1></body></html>'
        info.pagedescription = 'zimmer'
        info.pagekeywords = 'zimmer'
        info.pagetitle = 'zimmer'
        info.save()

    def testTrySearchIndexed(self):
        test_term = TrySearchTerm('pants', 'en')
        self.assertEqual(test_term.num_results, 1)
        self.assertEqual(PendingIndex.objects.filter(keywords='pants').count(), 0)

    def testTrySearchTwoWordPhraseIndexed(self):
        test_term = TrySearchTerm('chicken monkey', 'en')
        self.assertEqual(test_term.num_results, 1)
        self.assertEqual(PendingIndex.objects.filter(keywords='chicken monkey').count(), 0)

    def testTrySearchNotIndexed(self):
        test_term = TrySearchTerm('nopants', 'en')
        self.assertEqual(test_term, None)
        pending_index = PendingIndex.objects.get(keywords='nopants')
        self.assertEqual(pending_index.keywords, 'nopants')

    # If "pants" is indexed but neither "candy" nor "pants candy" are indexed,
    # both "candy" and "pants candy" should be added to the indexing queue
    # and the search result should return the single result for "pants".
    # We're also letting it imply that the serch term is English.
    def trySearchTwoWordsOneNotIndexed(self):
        test_term = TrySearchTerm('pants candy')
        self.assertEqual(test_term, None)
        pending_index = PendingIndex.objects.get(keywords='pants candy')
        self.assertEqual(pending_index.keywords, 'pants candy')
        pending_index = PendingIndex.objects.get(keywords='candy')
        self.assertEqual(pending_index.keywords, 'candy')

    # If "pants" and "taco" are indexed but not "pants taco", then "pants taco"
    # should be queued for indexing and not "pants" or "taco".
    def trySearchTwoWordsBothIndexed(self):
        test_term = TrySearchTerm('pants taco', 'en')
        self.assertEqual(test_term, None)
        pending_index = PendingIndex.objects.get(keywords='pants taco')
        self.assertEqual(pending_index.keywords, 'pants taco')
        self.assertEqual(PendingIndex.objects.filter(keywords='pants').count(), 0)
        self.assertEqual(PendingIndex.objects.filter(keywords='taco').count(), 0)

    # If neither word is indexed, the phrase and both individual words should
    # be queued for indexing.
    # 
    # Since there is a URL that has "horse monkey" all throughout the title and
    # text, there should be placeholder indexes for all three terms that have a
    # single result.
    #
    # We're also letting it imply that the search term is English.
    def trySearchTwoWordsNoneIndexed(self):
        test_term = TrySearchTerm('horse monkey')
        self.assertEqual(test_term, None)
        pending_index = PendingIndex.objects.get(keywords='horse monkey')
        self.assertEqual(pending_index.keywords, 'horse monkey')
        pending_index = PendingIndex.objects.get(keywords='horse')
        self.assertEqual(pending_index.keywords, 'horse')
        pending_index = PendingIndex.objects.get(keywords='monkey')
        self.assertEqual(pending_index.keywords, 'monkey')
        index_term = IndexTerm.objects.get(keywords='horse')
        self.assertEqual(index_term.num_results, 1)
        index_term = IndexTerm.objects.get(keywords='monkey')
        self.assertEqual(index_term.num_results, 1)
        index_term = IndexTerm.objects.get(keywords='horse monkey')
        self.assertEqual(index_term.num_results, 1)

    # Test same as above, but in German and with 3 words.
    # All 3 plus hte phrase should queue for indexing, and one phrase,
    # "zimmer', should pre-index because it has URL results. The others
    # should not.
    def trySearchThreeGermanWordsNoneIndexed(self):
        test_term = TrySearchTerm('zimmer tur nacht', 'de')
        self.assertEqual(test_term, None)
        pending_index = PendingIndex_de.objects.get(keywords='zimmer tur nacht')
        self.assertEqual(pending_index.keywords, 'zimmer tur nacht')
        pending_index = PendingIndex_de.objects.get(keywords='zimmer')
        self.assertEqual(pending_index.keywords, 'zimmer')
        pending_index = PendingIndex_de.objects.get(keywords='tur')
        self.assertEqual(pending_index.keywords, 'tur')
        pending_index = PendingIndex_de.objects.get(keywords='nacht')
        self.assertEqual(pending_index.keywords, 'nacht')
        index_term = IndexTerm_de.objects.get(keywords='zimmer tur nacht')
        self.assertEqual(index_term.num_results, 1)
        index_term = IndexTerm_de.objects.get(keywords='zimmer')
        self.assertEqual(index_term.num_results, 1)
        self.assertEqual(PendingIndex_de.objects.filter(keywords='tur').count(), 0)
        self.assertEqual(PendingIndex_de.objects.filter(keywords='nacht').count(), 0)

    def testTryDESearchIndexed(self):
        test_term = TrySearchTerm('buch', 'de')
        self.assertEqual(test_term.num_results, 1)

    def testTryDESearchNotIndexed(self):
        test_term = TrySearchTerm('boot', 'de')
        self.assertEqual(test_term, None)
        pending_index = PendingIndex_de.objects.get(keywords='boot')
        self.assertEqual(pending_index.keywords, 'boot')

    def testCreatePlaceholderIndex(self):
        test_term = CreatePlaceholderIndexTerm('WbSrch', 'en')
        self.assertEqual(test_term.num_results, 1)
        pending_index = PendingIndex.objects.get(keywords='wbsrch')
        self.assertEqual(pending_index.keywords, 'wbsrch')
        index_term = IndexTerm.objects.get(keywords='wbsrch')
        self.assertEqual(index_term.keywords, 'wbsrch')

    def testCreatePlaceholderIndexEmptyResult(self):
        test_term = CreatePlaceholderIndexTerm('queso', 'es')
        self.assertEqual(test_term.num_results, 0)
        pending_index = PendingIndex_es.objects.get(keywords='queso')
        self.assertEqual(pending_index.keywords, 'queso')
        try:
            index_term = IndexTerm_es.objects.get(keywords='queso')
        except ObjectDoesNotExist:
            index_term = None
        self.assertEqual(index_term, None)

    def testCreatePlaceholderIndexAlreadyExists(self):
        test_term = CreatePlaceholderIndexTerm('pants', 'en')
        self.assertEqual(test_term.num_results, 1)
        try:
            pending_index = PendingIndex.objects.get(keywords='pants')
        except ObjectDoesNotExist:
            pending_index = None
        self.assertEqual(pending_index, None)

    def testSearchTermNormalization(self):
        AddPendingTerm('xxa"', 'en')
        AddPendingTerm('"xxb', 'en')
        AddPendingTerm("xxc'", 'en')
        AddPendingTerm("'xxd", 'en')
        AddPendingTerm('xxe', 'en')
        xxa = PendingIndex.objects.filter(keywords='xxa').count()
        xxb = PendingIndex.objects.filter(keywords='xxa').count()
        xxc = PendingIndex.objects.filter(keywords='xxa').count()
        xxd = PendingIndex.objects.filter(keywords='xxa').count()
        xxe = PendingIndex.objects.filter(keywords='xxa').count()
        self.assertEqual(xxa, 1)
        self.assertEqual(xxb, 1)
        self.assertEqual(xxc, 1)
        self.assertEqual(xxd, 1)
        self.assertEqual(xxe, 1)

    def testRequestBlocking(self):
        bad = BadQuery()
        bad.keywords = u'11111'
        bad.save()
        response = self.client.get(u'/search/?q=11111')
        self.assertEqual(response.status_code, 403)
        response = self.client.get(u'/search/?q=111')
        self.assertEqual(response.status_code, 200)

    def testTermBlocking(self):
        bad = BadQuery()
        bad.keywords = u'underwear'
        bad.save()
        pending_count = PendingIndex.objects.count()
        AddPendingTerm(u'underwear')
        AddPendingTerm(u'sleep(3)')
        new_pending_count = PendingIndex.objects.count()
        self.assertEqual(pending_count, new_pending_count)

    def testBannedSearch(self):
        response = self.client.get(u'/search/?q=sleep(3)')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/search/?q=sleep(3)')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/search/?q=sleep')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(u'/search/?q=sleep')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/search/?q=chosen result: bad stuff')
        self.assertEqual(response.status_code, 403)
        response = self.client.get(u'/search/?q=chosen result: bad stuff')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/search/?q=99999999999999999999')
        self.assertEqual(response.status_code, 403)
        response = self.client.get(u'/search/?q=99999999999999999999')
        self.assertEqual(response.status_code, 403)
        response = self.client.get('/search/?q=9999')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(u'/search/?q=9999')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(u"/search/?q=input output99999' and(select 1 from(select count(*),concat((select (select (select distinct concat(0x7e,0x27,'ololo',0x27,0x7e) from information_schema.schemata limit 1)) from information_schema.tables")
        self.assertEqual(response.status_code, 403)
        response = self.client.get("/search/?q=input output99999' and(select 1 from(select count(*),concat((select (select (select distinct concat(0x7e,0x27,'ololo',0x27,0x7e) from information_schema.schemata limit 1)) from information_schema.tables")
        self.assertEqual(response.status_code, 403)

    def tearDown(self):
        for item in PendingIndex.objects.all():
            item.delete()
        for item in PendingIndex_de.objects.all():
            item.delete()
        for item in IndexTerm.objects.all():
            item.delete()
        for item in IndexTerm_de.objects.all():
            item.delete()
        for item in SiteInfo.objects.all():
            item.delete()
        for item in BadQuery.objects.all():
            item.delete()

class URLErrorTestCase(TestCase):
    def setUp(self):
        pass

    def testAddError(self):
        url = SiteInfo()
        url.rooturl = u'wbsrch.com'
        url.url = u'http://wbsrch.com/'
        url.lastcrawled = timezone.now() - timedelta(days=40)
        url.save()
        AddError(url, '502', 'Bad Gateway')
        AddError(url, '503', 'Service Unavailable')
        self.assertEqual(url.num_errors, 2)

    def testClearErrors(self):
        url = SiteInfo()
        url.rooturl = u'wbsrch.com'
        url.url = u'http://wbsrch.com/someurl/'
        url.lastcrawled = timezone.now() - timedelta(days=40)
        url.num_errors = 1
        url.error_info = '2014-02-06, 502, Bad Gateway\n'
        ClearErrors(url)
        self.assertEqual(url.num_errors, 0)
        self.assertEqual(url.error_info, '')

    def testDeleteAtMaxErrors(self):
        url = SiteInfo()
        url.rooturl = u'wbsrch.com'
        url.url = u'http://wbsrch.com/someotherurl/'
        url.lastcrawled = timezone.now() - timedelta(days=40)
        url.num_errors = 4
        url.error_info = '2014-02-06, 502, Bad Gateway\n2014-02-07, 502, Bad Gateway\n2014-02-08, 502, Bad Gateway\n2014-02-09, 502, Bad Gateway\n'
        url.save()
        AddError(url, '503', 'Service Unavailable')
        foundurls = SiteInfo.objects.filter(url=u'http://wbsrch.com/someotherurl/')
        self.assertEqual(foundurls.count(), 0)

    def tearDown(self):
        for url in SiteInfo.objects.all():
            url.delete()

class IndexUtilsTestCase(TestCase):
    def setUp(self):
        pending = PendingIndex()
        pending.keywords = 'hippo'
        pending.save()
        pendingel = PendingIndex_el()
        pendingel.keywords = 'zeus'
        pendingel.save()
        pendingel = PendingIndex_el()
        pendingel.keywords = 'athena'
        pendingel.save()
        term = IndexTerm()
        term.keywords = "sal"
        term.page_rankings = '{}'
        term.num_results = 1
        term.search_results = "[['sal.com', {'score': 30.0, ;urls': [{'url': 'http://www.sal.com', 'score': 20, 'id': 32 }]}]]"
        term.save()
        term = IndexTerm_fi()
        term.keywords = "salmiak"
        term.page_rankings = '{}'
        term.num_results = 1
        term.search_results = "[['salmiak.com', {'score': 10.0, ;urls': [{'url': 'http://www.salmiak.com', 'score': 10, 'id': 22 }]}]]"
        term.save()
        term = IndexTerm_fi()
        term.keywords = "lakerol"
        term.page_rankings = '{}'
        term.num_results = 1
        term.search_results = "[['salmiak.com', {'score': 5.0, ;urls': [{'url': 'http://www.salmiak.com', 'score': 10, 'id': 12 }]}]]"
        term.save()

    def testGetPendingIndexes(self):
        pending = GetPendingIndexes(12)
        self.assertEqual(len(pending), 1)

    def testGetPendingGreekIndexes(self):
        pending = GetPendingIndexes(12, language=u'el', offset=0)
        self.assertEqual(len(pending), 2)

    def testGetReindexes(self):
        reindex = GetReindexes(5)
        self.assertEqual(len(reindex), 1)

    def testGetFinnishReindexes(self):
        reindex = GetReindexes(5, offset=0, language=u'fi')
        self.assertEqual(len(reindex), 2)

    def removeFromPendingTestCase(self):
        RemoveFromPending('hippo')
        found = PendingIndex.objects.filter(keywords='hippo').count()
        self.assertEqual(found, 0)

    def removeFromGreekPendingTestCase(self):
        RemoveFromPending('zeus', u'el')
        found = PendingIndex_el.objects.filter(keywords='zeus').count()
        self.assertEqual(found, 0)

    def tearDown(self):
        for item in PendingIndex.objects.all():
            item.delete()
        for item in PendingIndex_el.objects.all():
            item.delete()
        for item in IndexTerm_fi.objects.all():
            item.delete()
        for item in IndexTerm.objects.all():
            item.delete()

class ViewsTestCase(TestCase):
    def setUp(self):
        log = SearchLog()
        log.keywords = 'fish'
        log.result_count = 6
        log.search_time = 0.03
        log.save()

    def testIndex(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def testPolicy(self):
        response = self.client.get('/policy/')
        self.assertEqual(response.status_code, 200)

    def testPrivacy(self):
        response = self.client.get('/privacy/')
        self.assertEqual(response.status_code, 200)

    def testPhilosophy(self):
        response = self.client.get('/philosophy/')
        self.assertEqual(response.status_code, 200)

    def testFAQ(self):
        response = self.client.get('/faq/')
        self.assertEqual(response.status_code, 200)

    def testDMCA(self):
        response = self.client.get('/dmca/')
        self.assertEqual(response.status_code, 200)

    def testHowto(self):
        response = self.client.get('/howto/')
        self.assertEqual(response.status_code, 200)

    def testCriteria(self):
        response = self.client.get('/criteria/')
        self.assertEqual(response.status_code, 200)

    def testTerms(self):
        response = self.client.get('/terms/')
        self.assertEqual(response.status_code, 200)

    def testChangelog(self):
        response = self.client.get('/changelog/')
        self.assertEqual(response.status_code, 200)

    def testIndexStats(self):
        response = self.client.get('/index-stats/')
        self.assertEqual(response.status_code, 200)

    def testAdminPanel(self):
        response = self.client.get('/adminpanel/')
        self.assertEqual(response.status_code, 302)

    def testAdminPanelOldest(self):
        response = self.client.get('/adminpanel/oldestcrawls/')
        self.assertEqual(response.status_code, 302)

    def testAdminPanelUnclass(self):
        response = self.client.get('/adminpanel/unclassified/')
        self.assertEqual(response.status_code, 302)

    def testAdminPanelTop(self):
        response = self.client.get('/adminpanel/topsites/')
        self.assertEqual(response.status_code, 302)

    def testSearchCheese(self):
        response = self.client.get('/search/?q=cheese')
        self.assertEqual(response.status_code, 200)
        logs = SearchLog.objects.all().count()
        self.assertEqual(logs, 2)

    def testSearchCheese(self):
        response = self.client.get('/search/?q=cheese&domain=cheese.com')
        self.assertEqual(response.status_code, 200)

    def testExtremelyLongQuery(self):
        response = self.client.get('/search/?q=cheeseisthebestthingintheentireworldicannotgetenoughofitandiwantmoreandmoreandmoreandmorebutpleasedontthinkthatisallieatsometimesthereareburritosorburgersorhotdogsorfalafelsorporkchopsorvariousandsundryotherthingsunderneathmysliceofcheeseandiwouldnthaveitanyotherway')
        self.assertEqual(response.status_code, 200)

    def testExtremelyLongDomainQuery(self):
        response = self.client.get('/search/?q=cheeseisthebestthingintheentireworldicannotgetenoughofitandiwantmoreandmoreandmoreandmorebutpleasedontthinkthatisallieatsometimesthereareburritosorburgersorhotdogsorfalafelsorporkchopsorvariousandsundryotherthingsunderneathmysliceofcheeseandiwouldnthaveitanyotherway&domain=cheese.com')
        self.assertEqual(response.status_code, 200)

    def testPopularSearches(self):
        response = self.client.get('/popular-searches/')
        self.assertEqual(response.status_code, 200)

    def testPopularSearches(self):
        response = self.client.get('/popular-searches/2011/03/')
        self.assertEqual(response.status_code, 404)

    def testDomain(self):
        response = self.client.get('/domain/')
        self.assertEqual(response.status_code, 200)

    def testSearchDomain(self):
        response = self.client.get('/domain/?q=zetacentauri.com')
        self.assertEqual(response.status_code, 200)

    # Still need to test:
    #def domainrank(request):
    #def adminpanel_doctype(request):
    # Popular searches with an actual search history month/year combo:
    #def popular_searches(request, year=None, month=None):

    def tearDown(self):
        for item in SearchLog.objects.all():
            item.delete()

class BlockedSiteTestCase(TestCase):
    def setUp(self):
        info = SiteInfo()
        info.rooturl = u'spamsite.com'
        info.url = u'http://spamsite.com/1/'
        info.save()
        info = SiteInfo_cs()
        info.rooturl = u'spamsite.cz'
        info.url = u'http://spamsite.cz/1/'
        info.save()       
        info = SiteInfo_cs()
        info.rooturl = u'spamsite.cz'
        info.url = u'http://spamsite.cz/2/'
        info.save()       
        info = SiteInfo_cs()
        info.rooturl = u'notaspamsite.cz'
        info.url = u'http://notaspamsite.cz/1/'
        info.save()
        domain = DomainInfo()
        domain.url = u'spamsite.cz'
        domain.language_association = u'cs'
        domain.save()

    def testExcludeUrl(self):
        exclude = BlockedSite()
        exclude.url = u'spamsite.com'
        exclude.save()
        self.assertEqual(SiteInfo.objects.all().count(), 0)

    def testExcludeCzechUrl(self):
        exclude = BlockedSite()
        exclude.url = u'spamsite.cz'
        exclude.save()
        self.assertEqual(SiteInfo_cs.objects.all().count(), 1)

    def tearDown(self):
        for item in BlockedSite.objects.all():
            item.delete()
        for item in SiteInfo_cs.objects.all():
            item.delete()

class ModelStringsTestCase(TestCase):
    def setUp(self):
        pass

    def testSetting(self):
        s = Setting()
        print s

    def testChangeLogItem(self):
        i = ChangelogItem()
        print i    

    def testBlockedSite(self):
        e = BlockedSite()
        print e

    def testDomainInfo(self):
        e = DomainInfo()
        print e

    def testDomainExtension(self):
        e = DomainSuffix()
        print e

    def testPendingUrl(self):
        e = CrawlableUrl()
        print e

    def testSiteInfo(self):
        e = SiteInfo()
        print e

    def testSearchLog(self):
        e = SearchLog()
        print e

    def testPendingIndex(self):
        e = PendingIndex()
        print e

    def testIndexTerm(self):
        e = IndexTerm()
        print e

    def testIPAddress(self):
        e = IPAddress()
        print e

    def tearDown(self):
        pass

class IndexStatsTestCase(TestCase):
    def setUp(self):
        info = SiteInfo()
        info.rooturl = u'spamsite.com'
        info.url = u'http://spamsite.com/1/'
        info.save()
        info = SiteInfo_cs()
        info.rooturl = u'spamsite.cz'
        info.url = u'http://spamsite.cz/1/'
        info.save()       
        pending = PendingIndex()
        pending.keywords = 'hippo'
        pending.save()
        pendingel = PendingIndex_el()
        pendingel.keywords = 'zeus'
        pendingel.save()
        pendingel = PendingIndex_el()
        pendingel.keywords = 'athena'
        pendingel.save()
        term = IndexTerm()
        term.keywords = "sal"
        term.page_rankings = '{}'
        term.num_results = 1
        term.search_results = "[['sal.com', {'score': 30.0, ;urls': [{'url': 'http://www.sal.com', 'score': 20, 'id': 32 }]}]]"
        term.save()
        term = IndexTerm_fi()
        term.keywords = "lakerol"
        term.page_rankings = '{}'
        term.num_results = 1
        term.search_results = "[['salmiak.com', {'score': 5.0, ;urls': [{'url': 'http://www.salmiak.com', 'score': 10, 'id': 12 }]}]]"
        term.save()
        esite = BlockedSite()
        esite.url = 'http://porn.com'
        esite.save()

    def generateIndexStats(self):
        stats = GenerateIndexStats(False)
        self.assertIsNone(stats.pk)
        stats.save()
        self.assertNotEqual(stats.pk, None)
        self.assertEqual(stats.num_excluded, 1)
        self.assertEqual(stats.total_urls, 2)
        self.assertEqual(stats.total_indexes, 2)
        self.assertEqual(stats.total_pendingindexes, 3)

    def tearDown(self):
        for item in SiteInfo.objects.all():
            item.delete()
        for item in SiteInfo_cs.objects.all():
            item.delete()
        for item in PendingIndex.objects.all():
            item.delete()
        for item in PendingIndex_el.objects.all():
            item.delete()
        for item in IndexTerm.objects.all():
            item.delete()
        for item in IndexTerm_fi.objects.all():
            item.delete()
        for item in BlockedSite.objects.all():
            item.delete()
        for item in IndexStats.objects.all():
            item.delete()

class MoveSiteTestCase(TestCase):

    def setUp(self):
        info = SiteInfo()
        info.rooturl = u'example.com'
        info.url = u'http://example.com/1/'
        info.lastcrawled = timezone.now()
        info.save()
        info = SiteInfo()
        info.rooturl = u'exampletwo.com'
        info.url = u'http://exampletwo.com/1/'
        info.lastcrawled = timezone.now()
        info.save()
        info = SiteInfo()
        info.rooturl = u'examplethree.com'
        info.url = u'http://examplethree.com/1/'
        info.lastcrawled = timezone.now()
        info.save()
        info = SiteInfo()
        info.rooturl = u'examplefour.com'
        info.url = u'http://examplefour.com/1/'
        info.lastcrawled = timezone.now()
        info.save()
        info = SiteInfo()
        info.rooturl = u'examplefour.com'
        info.url = u'http://examplefour.com/2/'
        info.lastcrawled = timezone.now()
        info.save()
        info = SiteInfo_cs()
        info.rooturl = u'example.cz'
        info.url = u'http://example.cz/1/'
        info.lastcrawled = timezone.now()
        info.save()       
        domain = DomainInfo()
        domain.url = u'example.com'
        domain.language_association = 'en'
        domain.save()
        domain = DomainInfo()
        domain.url = u'exampletwo.com'
        domain.language_association = ''
        domain.save()
        domain = DomainInfo()
        domain.url = u'example.cz'
        domain.language_association = 'cz'
        domain.save()

    def testMoveToPL(self):
        """
        Move a site info from the US index to the Polish index and verify
        that it's tagged with the correct language and that only the
        selected URL is moved, not both URLs for that domain.
        """
        info = SiteInfo.objects.get(url=u'http://examplefour.com/1/')
        MoveSiteTo(info, 'pl')
        polishurls = SiteInfo_pl.objects.all().count()
        self.assertEqual(polishurls, 1)
        domain = DomainInfo.objects.get(url='examplefour.com')
        self.assertEqual(domain.language_association, 'pl')
        englishurls = SiteInfo.objects.filter(rooturl=u'examplefour.com').count()
        self.assertEqual(englishurls, 1)

    def testMoveToIT(self):
        """
        Move a site with a blank language association and be sure that it is filled in.
        """
        info = SiteInfo.objects.get(url=u'http://exampletwo.com/1/')
        MoveSiteTo(info, 'it')
        italianurls = SiteInfo_it.objects.all().count()
        self.assertEqual(italianurls, 1)
        domain = DomainInfo.objects.get(url='exampletwo.com')
        self.assertEqual(domain.language_association, 'it')
        englishurls = SiteInfo.objects.filter(rooturl=u'exampletwo.com').count()
        self.assertEqual(englishurls, 0)

    def testMoveToFR(self):
        """
        Move a site with an existing language association and be sure that it doesn't change.
        """
        info = SiteInfo.objects.get(url=u'http://example.com/1/')
        MoveSiteTo(info, 'fr')
        frenchurls = SiteInfo_fr.objects.all().count()
        self.assertEqual(frenchurls, 1)
        domain = DomainInfo.objects.get(url='example.com')
        self.assertEqual(domain.language_association, 'en')
        englishurls = SiteInfo.objects.filter(rooturl=u'example.com').count()
        self.assertEqual(englishurls, 0)

    def testMoveFromCZ(self):
        """
        Move a site with an existing language association into the English site pool.
        Make sure the language association doesn't change.
        """
        info = SiteInfo_cs.objects.get(url=u'http://example.cz/1/')
        MoveSiteTo(info, 'en')
        englishurls = SiteInfo.objects.filter(rooturl=u'example.cz').count()
        self.assertEqual(englishurls, 1)
        domain = DomainInfo.objects.get(url='example.cz')
        self.assertEqual(domain.language_association, 'cz')
        czechurls = SiteInfo_cs.objects.filter(rooturl=u'example.cz').count()
        self.assertEqual(czechurls, 0)

    def tearDown(self):
        for item in DomainInfo.objects.all():
            item.delete()
        for item in SiteInfo.objects.all():
            item.delete()
        for item in SiteInfo_it.objects.all():
            item.delete()
        for item in SiteInfo_pl.objects.all():
            item.delete()
        for item in SiteInfo_fr.objects.all():
            item.delete()
        for item in SiteInfo_cs.objects.all():
            item.delete()

class PornBlockTestCase(TestCase):
    def setUp(self):
        info = SiteInfo()
        info.rooturl = u'notporn.com'
        info.url = u'http://notporn.com/1/'
        info.save()
        info = SiteInfo()
        info.rooturl = u'notporn.com'
        info.url = u'http://notporn.com/2/'
        info.save()
        info = SiteInfo()
        info.rooturl = u'pornsite.com'
        info.url = u'http://pornsite.com/1/'
        info.save()
        info = SiteInfo()
        info.rooturl = u'pornsite.com'
        info.url = u'http://pornsite.com/2/'
        info.save()
        info = SiteInfo()
        info.rooturl = u'ass.pornsite2.com'
        info.url = u'http://ass.pornsite2.com/2/'
        info.save()
        info = SiteInfo()
        info.rooturl = u'pornsite2.com'
        info.url = u'http://pornsite2.com/2/'
        info.save()
        info = SiteInfo()
        info.rooturl = u'pornsite3.com'
        info.url = u'http://pornsite3.com/2/'
        info.save()
        info = SiteInfo()
        info.rooturl = u'ass.pornsite.com'
        info.url = u'http://ass.pornsite.com/1/'
        info.save()
        info = SiteInfo()
        info.rooturl = u'ass.pornsite.com'
        info.url = u'http://ass.pornsite.com/2/'
        info.save()
        info = SiteInfo_it()
        info.rooturl = u'pornsite.it'
        info.url = u'http://pornsite.it/1/'
        info.save()
        info = SiteInfo_it()
        info.rooturl = u'pornsite.it'
        info.url = u'http://pornsite.it/2/'
        info.save()
        info = SiteInfo_it()
        info.rooturl = u'ass.pornsite.it'
        info.url = u'http://ass.pornsite.it/2/'
        info.save()
        domain = DomainInfo()
        domain.url = u'notporn.com'
        domain.is_unblockable = True
        domain.save()
        domain = DomainInfo()
        domain.url = u'pornsite3.com'
        domain.is_unblockable = False
        domain.language_association = u'en'
        domain.save()
        domain = DomainInfo()
        domain.url = u'pornsite.it'
        domain.language_association = u'it'
        domain.save()
        domain = DomainInfo()
        domain.url = u'ass.pornsite.it'
        domain.language_association = u'it'
        domain.save()

    def testPornBlockChild(self):
            """
            Checks that all of the urls and parent urls are deleted and the domains blocked
            when you pornblock a child URL.
            """
            site = SiteInfo.objects.get(url=u'http://ass.pornsite.com/2/')
            PornBlock(site)
            assurls = SiteInfo.objects.filter(rooturl=u'ass.pornsite.com').count()
            pornurls = SiteInfo.objects.filter(rooturl=u'pornsite.com').count()
            assexclusion = BlockedSite.objects.filter(url=u'ass.pornsite.com')
            pornexclusion = BlockedSite.objects.filter(url=u'pornsite.com')
            self.assertEqual(assurls, 0)
            self.assertEqual(pornurls, 0)
            self.assertEqual(assexclusion.count(), 1)
            self.assertEqual(pornexclusion.count(), 1)
            self.assertEqual(pornexclusion[0].exclude_subdomains, True)

    def testPornBlockParent(self):
            """
            Checks to be sure that child domain URLs are unaffected when the parent is blocked.
            """
            site = SiteInfo.objects.get(url=u'http://pornsite2.com/2/')
            PornBlock(site)
            assurls = SiteInfo.objects.filter(rooturl=u'ass.pornsite2.com').count()
            pornurls = SiteInfo.objects.filter(rooturl=u'pornsite2.com').count()
            assexclusion = BlockedSite.objects.get(url=u'ass.pornsite2.com')
            pornexclusion = BlockedSite.objects.filter(url=u'pornsite2.com')
            self.assertEqual(assurls, 1)
            self.assertEqual(pornurls, 0)
            self.assertEqual(assexclusion.count(), 0)
            self.assertEqual(pornexclusion.count(), 1)
            self.assertEqual(pornexclusion[0].exclude_subdomains, True)

    def testPornBlockParent(self):
            site = SiteInfo.objects.get(url=u'http://pornsite3.com/2/')
            PornBlock(site)
            pornurls = SiteInfo.objects.filter(rooturl=u'pornsite3.com').count()
            pornexclusion = BlockedSite.objects.filter(url=u'pornsite3.com')
            domain = DomainInfo.objects.get(url=u'pornsite3.com')
            self.assertEqual(pornurls, 0)
            self.assertEqual(pornexclusion.count(), 1)
            self.assertEqual(pornexclusion[0].exclude_subdomains, True)

    def testPornBlockItalian(self):
            site = SiteInfo_it.objects.get(url=u'http://ass.pornsite.it/2/')
            PornBlock(site)
            assurls = SiteInfo_it.objects.filter(rooturl=u'ass.pornsite.it').count()
            pornurls = SiteInfo_it.objects.filter(rooturl=u'pornsite.it').count()
            assexclusion = BlockedSite.objects.filter(url=u'ass.pornsite.it')
            pornexclusion = BlockedSite.objects.filter(url=u'pornsite.it')
            self.assertEqual(assurls, 0)
            self.assertEqual(pornurls, 0)
            self.assertEqual(assexclusion.count(), 1)
            self.assertEqual(pornexclusion.count(), 1)
            self.assertEqual(pornexclusion[0].exclude_subdomains, True)

    def testPornBlockNotporn(self):
            site = SiteInfo.objects.get(url=u'http://notporn.com/2/')
            PornBlock(site)
            pornurls = SiteInfo.objects.filter(rooturl=u'notporn.com').count()
            pornexclusion = BlockedSite.objects.filter(url=u'notporn.com')
            self.assertEqual(pornurls, 1)
            self.assertEqual(pornexclusion.count(), 0)

    def tearDown(self):
            for info in SiteInfo.objects.all():
                info.delete()
            for info in SiteInfo_it.objects.all():
                info.delete()
            for info in DomainInfo.objects.all():
                info.delete()

class WhoisTestCase(TestCase):
    def testDomainAge(self):
        ages = GetDomainAge(u'zetacentauri.com')
        print ages
        self.assertNotEqual(ages, None)
