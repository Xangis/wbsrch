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
from dir.models import *
from dir.exceptions import *
from dir.utils import *
from dir.crawler import *
from dir.indexer import *
from dir.language import *
from dir.domain import *
from zetaweb.settings import *
from datetime import timedelta


class GetRootUrlTestCase(TestCase):

    def test_url_with_period(self):
        """
        Tests that a URL with a period at the end has the period stripped.
        """
        url = GetRootUrl(u'http://zetacentauri.com.')
        self.assertEqual(url, 'zetacentauri.com')

    def test_url_with_period_and_suffix(self):
        """
        Tests that a URL with a period at the end has the period stripped when there is data after the period.
        """
        url = GetRootUrl(u'http://zetacentauri.com./software/')
        self.assertEqual(url, 'zetacentauri.com')

    def test_url_case(self):
        """
        Tests that a URL with mixed cases gets a lowercase root URL.
        """
        url = GetRootUrl(u'http://ZetaCenTaUri.coM')
        self.assertEqual(url, 'zetacentauri.com')

    def test_url_with_https(self):
        """
        Tests that a URL with https gets a proper root URL.
        """
        url = GetRootUrl(u'https://zetacentauri.com')
        self.assertEqual(url, 'zetacentauri.com')

    def test_url_with_colon(self):
        """
        Tests that a URL containing a colon (port 8080) gets the proper root URL without the colon.
        """
        url = GetRootUrl(u'https://zetacentauri.com:8080')
        self.assertEqual(url, 'zetacentauri.com')

    def test_url_with_colon_eighty(self):
        """
        Tests that a URL containing a colon (port 80) gets the proper root URL without the colon.
        """
        url = GetRootUrl(u'https://zetacentauri.com:80')
        self.assertEqual(url, 'zetacentauri.com')

    def test_url_with_subdomain(self):
        """
        Tests that a URL with a subdomain works.
        """
        url = GetRootUrl(u'https://www.zetacentauri.com:80')
        self.assertEqual(url, 'www.zetacentauri.com')

    def test_url_with_subdomain2(self):
        """
        Tests that a URL with a subdomain works.
        """
        url = GetRootUrl(u'://www.zetacentauri.com')
        self.assertEqual(url, 'www.zetacentauri.com')

    def test_url_with_subdomain3(self):
        """
        Tests that a URL with a subdomain works (2).
        """
        url = GetRootUrl(u'https://another.subdomain.zetacentauri.com')
        self.assertEqual(url, 'another.subdomain.zetacentauri.com')


class GetRootDomainTestCase(TestCase):

    def test_url_with_period(self):
        """
        Tests that a URL with a period at the end has the period stripped.
        """
        url = GetRootDomain(u'http://zetacentauri.com.')
        self.assertEqual(url, 'zetacentauri.com')

    def test_url_with_period_and_suffix(self):
        """
        Tests that a URL with a period at the end has the period stripped when there is data after the period.
        """
        url = GetRootDomain(u'http://zetacentauri.com./software/')
        self.assertEqual(url, 'zetacentauri.com')

    def test_url_case(self):
        """
        Tests that a URL with mixed cases gets a lowercase root URL.
        """
        url = GetRootDomain(u'http://ZetaCenTaUri.coM')
        self.assertEqual(url, 'zetacentauri.com')

    def test_ip_case(self):
        url = GetRootDomain(u'http://192.168.0.1')
        self.assertEqual(url, '192.168.0.1')

    def test_ip_folder_case(self):
        url = GetRootDomain(u'http://216.151.3.15/index-stats/index.htm')
        self.assertEqual(url, '216.151.3.15')

    def test_url_with_https(self):
        """
        Tests that a URL with https gets a proper root URL.
        """
        url = GetRootDomain(u'https://zetacentauri.com')
        self.assertEqual(url, 'zetacentauri.com')

    def test_url_with_colon(self):
        """
        Tests that a URL containing a colon (port 8080) gets the proper root URL without the colon.
        """
        url = GetRootDomain(u'https://zetacentauri.com:8080')
        self.assertEqual(url, 'zetacentauri.com')

    def test_url_with_colon_eighty(self):
        """
        Tests that a URL containing a colon (port 80) gets the proper root URL without the colon.
        """
        url = GetRootDomain(u'https://zetacentauri.com:80')
        self.assertEqual(url, 'zetacentauri.com')

    def test_url_with_subdomain(self):
        """
        Tests that a URL with a subdomain works.
        """
        url = GetRootDomain(u'https://www.zetacentauri.com:80')
        self.assertEqual(url, 'zetacentauri.com')

    def test_url_with_subdomain2(self):
        """
        Tests that a URL with a subdomain works (2).
        """
        url = GetRootDomain(u'https://another.subdomain.zetacentauri.com')
        self.assertEqual(url, 'zetacentauri.com')

    def test_url_with_subdomain3(self):
        """
        Tests that a URL with a subdomain works (2).
        """
        url = GetRootDomain(u'https://another.subdomain.zetacentauri.com/software/whatever/something.htm')
        self.assertEqual(url, 'zetacentauri.com')


class IsValidHtmlUrlTestCase(TestCase):
    def test_mp3_url(self):
        """
        Tests that a URL ending with MP3 does not register as valid.
        """
        url = "http://wbsrch.com/tutorial.mp3"
        self.assertFalse(IsHtmlUrl(url))

    def test_wav_url(self):
        """
        Tests that a URL ending with wav does not register as valid.
        """
        url = "http://wbsrch.com/tutorial.wav"
        self.assertFalse(IsHtmlUrl(url))

    def test_htm_url(self):
        """
        Tests that a URL ending with htm does register as valid.
        """
        url = "http://wbsrch.com/tutorial.htm"
        self.assertTrue(IsHtmlUrl(url))

    def test_aspx_url(self):
        """
        Tests that a URL ending with aspx does register as valid.
        """
        url = "http://wbsrch.com/tutorial.aspx"
        self.assertTrue(IsHtmlUrl(url))

    def test_html_url(self):
        """
        Tests that a URL ending with html does register as valid.
        """
        url = "http://wbsrch.com/tutorial.html"
        self.assertTrue(IsHtmlUrl(url))

    def test_slash_url(self):
        """
        Tests that a URL ending with / does register as valid.
        """
        url = "http://wbsrch.com/tutorial/"
        self.assertTrue(IsHtmlUrl(url))

    def test_php_url(self):
        """
        Tests that a URL ending with php does register as valid.
        """
        url = "http://wbsrch.com/tutorial.php"
        self.assertTrue(IsHtmlUrl(url))

    def test_md5_url(self):
        """
        Tests that a URL ending with md5 does register as valid.
        """
        url = "http://wbsrch.com/tutorial.file.name.md5"
        self.assertFalse(IsHtmlUrl(url))

    def test_pl_url(self):
        """
        Tests that a URL ending with .pl does register as valid.
        """
        url = "http://wbsrch.com/tutorial.pl"
        self.assertTrue(IsHtmlUrl(url))

    def test_js_url(self):
        """
        Tests that a URL starting with javascript: does not register as valid.
        """
        url = "javascript:alert(0)"
        self.assertFalse(IsHtmlUrl(url))

    def test_mailto_url(self):
        """
        Tests that a URL starting with mailto: does not register as valid.
        """
        url = "mailto:example@example.com"
        self.assertFalse(IsHtmlUrl(url))

    def test_exe_url(self):
        """
        Tests that a URL ending with exe does not register as valid.
        """
        url = "http://wbsrch.com/run.exe"
        self.assertFalse(IsHtmlUrl(url))

    def test_zip_domain(self):
        """
        Tests that a URL ending with zip does not register as valid.
        """
        url = "http://wbsrch.zip"
        self.assertTrue(IsHtmlUrl(url))

    def test_zip_domain2(self):
        """
        Tests that a URL ending with ip does not register as valid.
        """
        url = "http://wbsrch.zip/wbsrch.zip"
        self.assertFalse(IsHtmlUrl(url))

    def test_mov_domain(self):
        """
        Tests that a URL ending with mov does not register as valid.
        """
        url = "http://wbsrch.mov/"
        self.assertTrue(IsHtmlUrl(url))

    def test_mov_url(self):
        """
        Tests that a URL ending with mov does not register as valid.
        """
        url = "http://wbsrch.com/wbsrch.mov"
        self.assertFalse(IsHtmlUrl(url))

    def test_mov_url2(self):
        """
        Tests that a URL ending with mov does not register as valid.
        """
        url = "http://wbsrch.com/wbsrch.mov?t=30s"
        self.assertFalse(IsHtmlUrl(url))

    def test_xpi_url(self):
        url = "http://wbsrch.com/addon.xpi"
        self.assertFalse(IsHtmlUrl(url))

    def test_pdf_url(self):
        """
        Tests that a URL ending with pdf does not register as valid.
        """
        url = "http://wbsrch.com/tutorial.pdf"
        self.assertFalse(IsHtmlUrl(url))

    def test_gif_url(self):
        """
        Tests that a URL ending with gif does not register as valid.
        """
        url = "http://wbsrch.com/tutorial.gif"
        self.assertFalse(IsHtmlUrl(url))

    def test_png_url(self):
        """
        Tests that a URL ending with png does not register as valid.
        """
        url = "http://wbsrch.com/tutorial.png"
        self.assertFalse(IsHtmlUrl(url))

    def test_au_url(self):
        """
        Tests that a URL ending with au does register as valid.
        """
        url = "http://somesite.au"
        self.assertTrue(IsHtmlUrl(url))

    def test_mpg_url(self):
        """
        Tests that a URL ending with mpg does not register as valid.
        """
        url = "http://wbsrch.com/tutorial.mpg"
        self.assertFalse(IsHtmlUrl(url))

    def test_swf_url(self):
        """
        Tests that a URL ending with swf does not register as valid.
        """
        url = "http://wbsrch.com/tutorial.swf"
        self.assertFalse(IsHtmlUrl(url))

    def test_apk_url(self):
        """
        Tests that a URL ending with apk does not register as valid.
        """
        url = "http://wbsrch.com/tutorial.apk"
        self.assertFalse(IsHtmlUrl(url))

    def test_jpg_url(self):
        """
        Tests that a URL ending with JPG does not register as valid. Upper to test case-insensitive match.
        """
        url = "http://wbsrch.com/tutorial.JPG"
        self.assertFalse(IsHtmlUrl(url))

    def test_jpeg_url(self):
        """
        Tests that a URL ending with Jpeg does not register as valid. Upper to test case-insensitive match.
        """
        url = "http://wbsrch.com/tutorial.Jpeg"
        self.assertFalse(IsHtmlUrl(url))

    def test_long_https_jpeg_url(self):
        """
        Tests that a URL ending with Jpeg does not register as valid. Upper to test case-insensitive match.
        """
        url = "https://wbsrch.com/site/images/tutorial.jpeg"
        self.assertFalse(IsHtmlUrl(url))


class BlockedDomainTestCase(TestCase):
    def setUp(self):
        site = BlockedSite()
        site.url = 'www.yandex.ru'
        site.reason = 8
        site.save()

    def test_root_url(self):
        url = 'http://www.yandex.ru'
        rooturl = GetRootUrl(url)
        blocked_domain = BlockedSite.objects.filter(url=rooturl)
        self.assertEqual(blocked_domain.count(), 1)

    def test_rootslash_url(self):
        url = 'http://www.yandex.ru/'
        rooturl = GetRootUrl(url)
        blocked_domain = BlockedSite.objects.filter(url=rooturl)
        self.assertEqual(blocked_domain.count(), 1)

    def test_full_url(self):
        url = 'http://www.yandex.ru/index/'
        rooturl = GetRootUrl(url)
        blocked_domain = BlockedSite.objects.filter(url=rooturl)
        self.assertEqual(blocked_domain.count(), 1)

    def test_subdomain_url(self):
        url = 'http://en.yandex.ru'
        rooturl = GetRootUrl(url)
        blocked_domain = BlockedSite.objects.filter(url=rooturl)
        self.assertEqual(blocked_domain.count(), 0)

    def test_safe_url(self):
        url = 'http://www.google.com'
        rooturl = GetRootUrl(url)
        blocked_domain = BlockedSite.objects.filter(url=rooturl)
        self.assertEqual(blocked_domain.count(), 0)

    def tearDown(self):
        BlockedSite.objects.all().delete()


# Tests conditions for crawling and recrawling a url.
class CanCrawlUrlTestCase(TestCase):
    def setUp(self):
        site = BlockedSite()
        site.url = 'www.yandex.ru'
        site.reason = 8
        site.save()
        site = BlockedSite()
        site.url = 'morespamsite.com'
        site.reason = 7
        site.exclude_subdomains = True
        site.save()
        domain = DomainInfo()
        domain.url = 'www.spamsite.com'
        domain.save()
        domain = DomainInfo()
        domain.url = 'www.italiansite.it'
        domain.language_association = 'it'
        domain.save()
        domain = DomainInfo()
        domain.url = 'english.somesite.cn'
        domain.language_association = 'en'
        domain.save()
        domain = DomainInfo()
        domain.url = 'www.othersite.com'
        domain.save()
        info = SiteInfo()
        info.rooturl = 'www.spamsite.com'
        info.url = 'http://www.spamsite.com/1/'
        info.save()
        info = SiteInfo()
        info.rooturl = 'www.spamsite.com'
        info.url = 'http://www.spamsite.com/2/'
        info.save()
        info = SiteInfo_it()
        info.rooturl = 'www.italiansite.it'
        info.url = 'http://www.italiansite.it/'
        info.save()
        domainext = DomainSuffix()
        domainext.extension = '.hr'
        domainext.default_language = 'hr'
        domainext.save()
        domainext = DomainSuffix()
        domainext.extension = '.cn'
        domainext.save()

    def test_safe_url(self):
        url = 'http://wbsrch.com'
        self.assertTrue(CanCrawlUrl(url))

    def test_safe_recrawl_url(self):
        url = 'http://wbsrch.com'
        self.assertTrue(CanReCrawlUrl(url))

    def test_safe_short_url(self):
        url = 'wbsrch.com'
        self.assertTrue(CanCrawlUrl(url))

    def test_safe_recrawl_url2(self):
        url = 'wbsrch.com/admin/dir/siteinfo/'
        self.assertTrue(CanReCrawlUrl(url))

    def test_safe_recrawl_url3(self):
        url = 'http://somesite.au'
        self.assertTrue(CanReCrawlUrl(url))

    def test_bad_url1(self):
        url = 'http://wbsrch.com/tutorial.mp3'
        self.assertFalse(CanCrawlUrl(url))

    def test_bad_url2(self):
        url = 'wbsrch'
        self.assertFalse(CanCrawlUrl(url))

    def test_bad_url3(self):
        url = 'https://wbsrch'
        self.assertFalse(CanCrawlUrl(url))

    def test_another_bad_url(self):
        url = 'https://wbsrch.com/images/en/tutorial.jpg'
        self.assertFalse(CanCrawlUrl(url))

    def test_bad_short_url(self):
        url = 'wbsrch.com/tutorial.mp3'
        self.assertFalse(CanCrawlUrl(url))

    def test_blocked_url(self):
        url = 'http://www.yandex.ru'
        self.assertFalse(CanCrawlUrl(url))

    def test_blocked_url2(self):
        url = 'http://morespamsite.com'
        self.assertFalse(CanCrawlUrl(url))

    def test_blocked_url3(self):
        url = 'http://spampage.morespamsite.com'
        self.assertFalse(CanCrawlUrl(url))

    def test_blocked_short_url(self):
        url = 'www.yandex.ru'
        self.assertFalse(CanCrawlUrl(url))

    def test_blocked_extension_url(self):
        url = 'www.taobao.cn'
        self.assertFalse(CanCrawlUrl(url))

    def test_blocked_extension_url2(self):
        url = 'www.taobao.cn'
        self.assertTrue(CanReCrawlUrl(url))

    def test_blocked_extension_allowed_domain_url(self):
        url = 'http://english.somesite.cn/some_url.htm'
        self.assertTrue(CanCrawlUrl(url))

    def test_allowed_extension_url(self):
        url = 'www.croatia.hr'
        self.assertTrue(CanCrawlUrl(url))

    def test_invalid_domain(self):
        url = 'https://localhost:443'
        self.assertFalse(CanCrawlUrl(url))

    def test_invalid_domain2(self):
        url = 'http://localhost'
        self.assertFalse(CanCrawlUrl(url))

    def test_invalid_domain3(self):
        url = 'localhost'
        self.assertFalse(CanCrawlUrl(url))

    def test_valid_iplike1(self):
        url = 'http://192.168.tacos.com'
        self.assertTrue(CanCrawlUrl(url))

    def test_valid_iplike2(self):
        url = 'https://127.0.0.com'
        self.assertTrue(CanCrawlUrl(url))

    def test_valid_iplike3(self):
        url = 'https://127.0.0.1.domain.com'
        self.assertTrue(CanCrawlUrl(url))

    def test_valid_iplike4(self):
        url = '192.168.0.com'
        self.assertTrue(CanCrawlUrl(url))

    def test_invalid_ip1(self):
        url = 'http://192.168.0.1'
        self.assertFalse(CanCrawlUrl(url))

    def test_invalid_ip2(self):
        url = '10.0.0.1'
        self.assertFalse(CanCrawlUrl(url))

    def test_invalid_ip3(self):
        url = 'https://172.16.10.5:8080'
        self.assertFalse(CanCrawlUrl(url))

    def test_ftp_url(self):
        url = 'ftp://user:pass@example.com/home'
        self.assertFalse(CanCrawlUrl(url))

    def test_ftp_url2(self):
        url = 'ftp://user:pass@example.com:22/home'
        self.assertFalse(CanCrawlUrl(url))

    def test_sftp_url(self):
        url = 'sftp://example.com/home/'
        self.assertFalse(CanCrawlUrl(url))

    def test_mailto_url(self):
        url = 'mailto:bob@bob.com'
        self.assertFalse(CanCrawlUrl(url))

    def tearDown(self):
        BlockedSite.objects.all().delete()
        DomainSuffix.objects.all().delete()
        DomainInfo.objects.all().delete()
        SiteInfo.objects.all().delete()
        SiteInfo_it.objects.all().delete()


class NormalizeUrlTestCase(TestCase):
    def test_normal_url(self):
        url = 'http://wbsrch.com/tutorial.htm'
        self.assertEqual(NormalizeUrl(url), 'http://wbsrch.com/tutorial.htm')

    def test_normal_url2(self):
        url = 'http://wbsrch.com'
        self.assertEqual(NormalizeUrl(url), 'http://wbsrch.com')

    def test_normal_url3(self):
        url = 'http://wbsrch.com/'
        self.assertEqual(NormalizeUrl(url), 'http://wbsrch.com/')

    def test_jsession_url(self):
        url = 'http://farm.myswitzerland.com/on-the-farm/Airolojsessionid=94AFB92FD66F248EC3EF279B7A6732EF'
        self.assertEqual(NormalizeUrl(url), 'http://farm.myswitzerland.com/on-the-farm/Airolo')

    def test_jsession_url2(self):
        url = 'https://secure2.convio.net/fmnh/site/SPageServer/jsessionid=F1C5BEC5FD279BA9953C87FD37D5F89D.app274b?donate=now&pagename=api_donate'
        self.assertEqual(NormalizeUrl(url), 'https://secure2.convio.net/fmnh/site/SPageServer/?donate=now&pagename=api_donate')

    def test_jsession_url3(self):
        url = 'https://www.psiservice.com/psiweb/index.jsp;jsessionid=450B52BF0268B30DE854C552309E3E6A'
        self.assertEqual(NormalizeUrl(url), 'https://www.psiservice.com/psiweb/index.jsp')

    def test_jsession_url4(self):
        url = 'http://sage-ereference.com/publicstart;jsessionid=169E7071B011936163BDD68A0C95BD32?authRejection=true'
        self.assertEqual(NormalizeUrl(url), 'http://sage-ereference.com/publicstart?authRejection=true')

    def test_doubleslash_url(self):
        url = '//wbsrch.com/tutorial.htm'
        self.assertEqual(NormalizeUrl(url), 'http://wbsrch.com/tutorial.htm')

    def test_another_normal_url(self):
        url = 'http://wbsrch.com/tutorial/'
        self.assertEqual(NormalizeUrl(url), 'http://wbsrch.com/tutorial/')

    def test_third_normal_url(self):
        url = 'http://wbsrch.com/tutorial'
        self.assertEqual(NormalizeUrl(url), 'http://wbsrch.com/tutorial')

    def test_query_url(self):
        url = 'http://wbsrch.com/search/?q=term&r=termtwo'
        self.assertEqual(NormalizeUrl(url), 'http://wbsrch.com/search/?q=term&r=termtwo')

    def test_another_query_url(self):
        url = 'http://wbsrch.com/index.php?q=term&r=termtwo'
        self.assertEqual(NormalizeUrl(url), 'http://wbsrch.com/index.php?q=term&r=termtwo')

    def test_sessionid_url(self):
        url = 'http://wbsrch.com/index.php?q=term&r=termtwo&PHPSESSID=1234567abc'
        self.assertEqual(NormalizeUrl(url), 'http://wbsrch.com/index.php?q=term&r=termtwo')

    def test_utm_url(self):
        url = 'http://wbsrch.com/index.php?q=term&r=termtwo&utm_source=abc&utm_medium=def&utm_campaign=456&utm_term=789&utm_content=123'
        self.assertEqual(NormalizeUrl(url), 'http://wbsrch.com/index.php?q=term&r=termtwo')

    def test_sub1_url(self):
        url = 'http://ww16.skateboarder.fashion/?sub1=20210212-1625-0541-b345-64c8e2e71c44'
        self.assertEqual(NormalizeUrl(url), 'http://ww16.skateboarder.fashion/')

    def test_sessionid_lower_url(self):
        url = 'http://wbsrch.com/index.php?q=term&r=termtwo&jsessionid=1234567abc'
        self.assertEqual(NormalizeUrl(url), 'http://wbsrch.com/index.php?q=term&r=termtwo')

    def test_justsessionid_url(self):
        url = 'http://wbsrch.com/index.php?zenid=1234567abc'
        self.assertEqual(NormalizeUrl(url), 'http://wbsrch.com/index.php')

    def test_fragment_url(self):
        url = 'http://wbsrch.com/tutorial.htm#fragment'
        self.assertEqual(NormalizeUrl(url), 'http://wbsrch.com/tutorial.htm')

    def test_https_subdomain_url(self):
        url = 'https://el.wbsrch.com/tutorial.htm'
        self.assertEqual(NormalizeUrl(url), 'https://el.wbsrch.com/tutorial.htm')

    def test_port_url(self):
        url = 'https://wbsrch.com:8080/tutorial.htm'
        self.assertEqual(NormalizeUrl(url), 'https://wbsrch.com:8080/tutorial.htm')

    def test_capital_url(self):
        url = 'https://DE.WBSRCH.COM/tutorial.htm'

        self.assertEqual(NormalizeUrl(url), 'https://de.wbsrch.com/tutorial.htm')

    def test_capital_after_url(self):
        url = 'https://es.wbsrch.com/TUTORIAL_AND_WHATNOT.HTM'
        self.assertEqual(NormalizeUrl(url), 'https://es.wbsrch.com/TUTORIAL_AND_WHATNOT.HTM')

    def test_mixed_capital_url(self):
        url = 'https://fr.WBSRCH.com/TUTORIAL_and_WHATNOT.htm'
        self.assertEqual(NormalizeUrl(url), 'https://fr.wbsrch.com/TUTORIAL_and_WHATNOT.htm')


class MakeRealUrlTestCase(TestCase):
    def test_doubleslash_domain_url(self):
        url = '//wbsrch.com/tutorial.htm'
        self.assertEqual(MakeRealUrl(url), 'http://wbsrch.com/tutorial.htm')

    def test_slash_url(self):
        url = '/tutorial.htm'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://wbsrch.com/tutorial.htm')

    def test_slash_url2(self):
        url = '/tutorial.html'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://wbsrch.com/tutorial.html')

    def test_slash_url3(self):
        url = '/tutorial.php'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://wbsrch.com/tutorial.php')

    def test_colonslash_url6(self):
        url = '://tutorial.site/tutorial.php'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://tutorial.site/tutorial.php')

    def test_colonslash_url7(self):
        url = '//tutorial.site/tutorial/'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://tutorial.site/tutorial/')

    def test_slash_url5(self):
        url = '/tutorial/tutorial.htm'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://wbsrch.com/tutorial/tutorial.htm')

    def test_doubleslash_domainurl(self):
        url = '//wbsrch.com/tutorial/'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://wbsrch.com/tutorial/')

    def test_justdomain_nohttp(self):
        # Pass in domain to make it work.
        url = 'wbsrch.com/tutorial/'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://wbsrch.com/tutorial/')

    def test_justdomain_nohttp2(self):
        url = 'wbsrch.com/tutorial/'
        self.assertEqual(MakeRealUrl(url), 'http://wbsrch.com/tutorial/')

    def test_justdomain_nohttp3(self):
        url = 'browser.wbsrch.com/tutorial/tutorial.htm'
        self.assertEqual(MakeRealUrl(url), 'http://browser.wbsrch.com/tutorial/tutorial.htm')

    def test_doubleslash_domainurl2(self):
        url = '//wbsrch.com'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://wbsrch.com')

    def test_nakeddomain(self):
        url = 'wbsrch.com'
        self.assertEqual(MakeRealUrl(url, None), 'http://wbsrch.com')

    def test_nakeddomain2(self):
        url = 'browser.wbsrch.com'
        self.assertEqual(MakeRealUrl(url), 'http://browser.wbsrch.com')

    def test_doubleslash_domainurl3(self):
        url = '//wbsrch.com/tutorial.htm'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://wbsrch.com/tutorial.htm')

    def test_colondoubleslash_domainurl(self):
        url = '://wbsrch.com/tutorial.htm'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://wbsrch.com/tutorial.htm')

    def test_doubleslash_domainurl4(self):
        url = '//wbsrch.com/'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://wbsrch.com/')

    def test_doubleslash_domainurl5(self):
        url = '//wbsrch.com/tutorial/cheese/crackers/'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://wbsrch.com/tutorial/cheese/crackers/')

    def test_doubleslash_domainurl6(self):
        url = '//someothersite.com'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://someothersite.com')

    def test_doubleslash_domainurl7(self):
        url = '//someothersite.com/tutorial.htm'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://someothersite.com/tutorial.htm')

    def test_doubleslash_domainurl8(self):
        url = '//someothersite.com?name=me'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://someothersite.com?name=me')

    def test_noslash_domainurl1(self):
        url = 'tutorial.htm'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://wbsrch.com/tutorial.htm')

    def test_noslash_domainurl2(self):
        url = 'tutorial?name=me'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://wbsrch.com/tutorial?name=me')

    def test_noslash_domainurl3(self):
        url = 'pages/tutorial?name=me'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://wbsrch.com/pages/tutorial?name=me')

    def test_noslash_domainurl4(self):
        url = 'tutorial?name=me'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com', secure=True), 'https://wbsrch.com/tutorial?name=me')

    def test_noslash_domainurl5(self):
        url = 'pages/tutorial?name=me'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com', True), 'https://wbsrch.com/pages/tutorial?name=me')

    def test_slash_domainurl_b(self):
        url = '/pages/tutorial?name=me'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com', True), 'https://wbsrch.com/pages/tutorial?name=me')

    def test_normal_url(self):
        url = 'http://wbsrch.com/tutorial'
        self.assertEqual(MakeRealUrl(url), 'http://wbsrch.com/tutorial')

    def test_query_url(self):
        url = 'http://wbsrch.com/search/?q=term&r=termtwo'
        self.assertEqual(MakeRealUrl(url), 'http://wbsrch.com/search/?q=term&r=termtwo')

    def test_doubleslash_query_url(self):
        url = '//wbsrch.com/index.php?q=term&r=termtwo'
        self.assertEqual(MakeRealUrl(url), 'http://wbsrch.com/index.php?q=term&r=termtwo')

    def test_sessionid_url(self):
        url = 'wbsrch.com/index.php?q=term&r=termtwo&PHPSESSID=1234567abc'
        self.assertEqual(MakeRealUrl(url), 'http://wbsrch.com/index.php?q=term&r=termtwo')

    def test_secure_utm_url(self):
        url = 'https://wbsrch.com/index.php?q=term&r=termtwo&utm_source=abc&utm_medium=def&utm_campaign=456&utm_term=789&utm_content=123'
        self.assertEqual(MakeRealUrl(url), 'https://wbsrch.com/index.php?q=term&r=termtwo')

    def test_javascript_url(self):
        url = 'javascript:void(0)'
        self.assertEqual(MakeRealUrl(url), 'javascript:void(0)')

    def test_mailto_url(self):
        url = 'mailto:bob@bob.com'
        self.assertEqual(MakeRealUrl(url), 'mailto:bob@bob.com')

    def test_fileurlwithsessionid_url(self):
        url = 'index.php?zenid=1234567abc'
        self.assertEqual(MakeRealUrl(url, 'wbsrch.com'), 'http://wbsrch.com/index.php')

    def test_fragment_url(self):
        url = 'wbsrch.com/tutorial.htm#fragment'
        self.assertEqual(MakeRealUrl(url), 'http://wbsrch.com/tutorial.htm')

    def test_https_subdomain_url(self):
        url = 'https://el.wbsrch.com/tutorial.htm'
        self.assertEqual(MakeRealUrl(url), 'https://el.wbsrch.com/tutorial.htm')

    def test_port_url(self):
        url = 'https://wbsrch.com:8080/tutorial.htm'
        self.assertEqual(MakeRealUrl(url), 'https://wbsrch.com:8080/tutorial.htm')

    def test_capital_url(self):
        url = 'https://DE.WBSRCH.COM/tutorial.htm'
        self.assertEqual(MakeRealUrl(url), 'https://de.wbsrch.com/tutorial.htm')

    def test_capital_after_url(self):
        url = '//es.wbsrch.com/TUTORIAL_AND_WHATNOT.HTM'
        self.assertEqual(MakeRealUrl(url), 'http://es.wbsrch.com/TUTORIAL_AND_WHATNOT.HTM')

    def test_mixed_capital_url(self):
        url = 'fr.WBSRCH.com/TUTORIAL_and_WHATNOT.htm'
        self.assertEqual(MakeRealUrl(url), 'http://fr.wbsrch.com/TUTORIAL_and_WHATNOT.htm')


class PageLanguageTestCase(TestCase):
    def test_get_page_language(self):
        url = 'http://de.wbsrch.de/de/welcome.htm'
        html = '<html lang="de"><head><title>Title</title><meta name="Content-Language" content="de"></head><body>Hallo, Deutschland.</body></html>'
        self.assertEqual(IdentifyPageLanguage(url, html)[0], 'de')

    def test_get_page_language_prefix(self):
        url = 'http://lv.wbsrch.com'
        html = '<html><head><title>&nbsp;</title></head><body>&nbsp;</body></html>'
        self.assertEqual(IdentifyPageLanguage(url, html)[0], 'lv')

    def test_get_page_badlanguage_prefix(self):
        url = 'http://ja.wbsrch.com'
        html = '<html><head><title>&nbsp;</title></head><body>&nbsp;</body></html>'
        self.assertEqual(IdentifyPageLanguage(url, html)[0], 'ja')

    def test_get_page_badlanguage_suffix(self):
        url = 'http://wbsrch.az'
        html = '<html><head><title>&nbsp;</title></head><body>&nbsp;</body></html>'
        self.assertEqual(IdentifyPageLanguage(url, html)[0], 'az')

    def test_get_page_language_infix(self):
        url = 'http://wbsrch.com/sv/page/'
        html = '<html><head><title>&nbsp;</title></head><body>&nbsp;</body></html>'
        self.assertEqual(IdentifyPageLanguage(url, html)[0], 'sv')

    def test_get_blocked_page_language_infix(self):
        url = 'http://wbsrch.com/ru/page/'
        html = '<html><head><title>&nbsp;</title></head><body>&nbsp;</body></html>'
        try:
            IdentifyPageLanguage(url, html)
        except InvalidLanguageException as e:
            self.assertEqual(str(e), 'ru')

    def test_get_locale_language_infix(self):
        url = 'http://wbsrch.com/es-ar/page/'
        html = '<html><head><title>&nbsp;</title></head><body>&nbsp;</body></html>'
        self.assertEqual(IdentifyPageLanguage(url, html)[0], 'es')

    def test_get_blocked_locale_language_infix(self):
        url = 'http://wbsrch.com/ar-eg/page/'
        html = '<html><head><title>&nbsp;</title></head><body>&nbsp;</body></html>'
        try:
            IdentifyPageLanguage(url, html)
        except InvalidLanguageException as e:
            self.assertEqual(str(e), 'ar')


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

    def test_de_keywodr(self):
        model = GetKeywordRankingModelFromLanguage('de')
        self.assertEqual(model, KeywordRanking_de)

    def test_en_US_keyword(self):
        model = GetKeywordRankingModelFromLanguage('en-US')
        self.assertEqual(model, KeywordRanking)

    def test_en_keyword(self):
        model = GetKeywordRankingModelFromLanguage('en')
        self.assertEqual(model, KeywordRanking)

    def test_empty_keyword(self):
        model = GetKeywordRankingModelFromLanguage(None)
        self.assertEqual(model, KeywordRanking)

    def tearDown(self):
        pass


class UpdateAlexaRankTestCase(TestCase):
    def setUp(self):
        domain = DomainInfo()
        domain.url = 'www.spamsite.com'
        domain.alexa_rank = 999
        domain.save()
        domain = DomainInfo()
        domain.url = 'spamsite.com'
        domain.alexa_rank = 998
        domain.save()
        domain = DomainInfo()
        domain.url = 'spamsite2.com'
        domain.alexa_rank = 997
        domain.save()
        domain = DomainInfo()
        domain.url = 'www.spamsite3.com'
        domain.alexa_rank = 996
        domain.save()
        domain = DomainInfo()
        domain.url = 'spamsite4.com'
        domain.alexa_rank = 995
        domain.save()
        domain = DomainInfo()
        domain.url = 'www.spamsite4.com'
        domain.alexa_rank = 994
        domain.save()
        domain = DomainInfo()
        domain.url = 'www.spamsite6.com'
        domain.alexa_rank = 993
        domain.save()

    def test_update_raw_url(self):
        url = 'spamsite2.com'
        rank = 100
        UpdateAlexaRank(url, rank)
        domain = DomainInfo.objects.get(url=url)
        self.assertEqual(domain.alexa_rank, rank)
        # TODO: Assert exception if we query www.spamsite2.com

    def test_update_www_url(self):
        url = 'www.spamsite3.com'
        rank = 200
        UpdateAlexaRank(url, rank)
        domain = DomainInfo.objects.get(url=url)
        self.assertEqual(domain.alexa_rank, rank)
        # TODO: Assert exception if we query spamsite3.com

    def test_update_www_url_and_base(self):
        url = 'www.spamsite.com'
        baseurl = 'spamsite.com'
        rank = 300
        UpdateAlexaRank(url, rank)
        domain = DomainInfo.objects.get(url=url)
        self.assertEqual(domain.alexa_rank, rank)
        domain = DomainInfo.objects.get(url=baseurl)
        self.assertEqual(domain.alexa_rank, rank)
        pass

    def test_update_base_url_and_www(self):
        url = 'spamsite4.com'
        wwwurl = 'www.spamsite4.com'
        rank = 400
        UpdateAlexaRank(url, rank)
        domain = DomainInfo.objects.get(url=url)
        self.assertEqual(domain.alexa_rank, rank)
        domain = DomainInfo.objects.get(url=wwwurl)
        self.assertEqual(domain.alexa_rank, rank)

    def test_add_new_url(self):
        url = 'spamsite5.com'
        rank = 500
        UpdateAlexaRank(url, rank)
        domain = DomainInfo.objects.get(url=url)
        self.assertEqual(domain.alexa_rank, rank)
        # TODO: Assert exception if we query www.spamsite5.com

    def test_add_new_url_existing_www(self):
        url = 'spamsite6.com'
        wwwurl = 'www.spamsite6.com'
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
        info.rooturl = 'wbsrch.com'
        info.url = 'http://wbsrch.com/'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagetext = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.save()
        info = SiteInfo()
        info.rooturl = 'wbsrch.com'
        info.url = 'http://wbsrch.com/search/'
        info.lastcrawled = timezone.now()
        info.pagetext = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.save()
        info = SiteInfo()
        info.rooturl = 'wbsrch.com'
        info.url = 'http://wbsrch.com/changelog/'
        info.lastcrawled = timezone.now() - timedelta(days=5)
        info.pagetext = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.save()
        info = SiteInfo()
        info.rooturl = 'wbsrch.com'
        info.url = 'http://wbsrch.com/privacy/'
        info.lastcrawled = timezone.now() - timedelta(days=3)
        info.pagetext = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.save()
        info = SiteInfo()
        info.rooturl = 'wbsrch.com'
        info.url = 'http://wbsrch.com/policy/'
        info.lastcrawled = timezone.now() - timedelta(days=9)
        info.pagetext = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
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
        MarkURLContentsAsSpam(spamhtml, ip)
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
        self.assertEqual(info.pagesize, 1061)

    def tearDown(self):
        pass


class IndexerTestCase(TestCase):

    def setUp(self):
        info = SiteInfo()
        info.rooturl = 'wbsrch.com'
        info.url = 'http://wbsrch.com/'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagetext = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.pagedescription = 'wbsrch search engine'
        info.pagekeywords = 'wbsrch, search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.pagesize = len(info.pagetext)
        info.save()
        info = SiteInfo()
        info.rooturl = 'zetacentauri.com'
        info.url = 'https://zetacentauri.com/'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagetext = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.pagekeywords = 'wbsrch, pants'
        info.pagesize = len(info.pagetext)
        info.save()
        info = SiteInfo()
        info.rooturl = 'zetacentauri.com'
        info.url = 'http://zetacentauri.com/'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagetext = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.pagekeywords = 'wbsrch'
        info.pagesize = len(info.pagetext)
        info.save()
        info = SiteInfo()
        info.rooturl = 'zetacentauri.com'
        info.url = 'http://zetacentauri.com/page.htm'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagetext = '<html><head><title>WbSrch</title></head><body><h1>WbSrch Search Engine</h1></body></html>'
        info.pagedescription = 'search engine'
        info.pagekeywords = 'search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.pagesize = len(info.pagetext)
        info.save()
        info = SiteInfo_de()
        info.rooturl = 'zetacentauri.com'
        info.url = 'http://zetacentauri.com/page.htm'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagetext = '<html><head><title>WbSrch</title></head><body><h1>WbSrch Search Engine</h1></body></html>'
        info.pagedescription = 'search engine'
        info.pagekeywords = 'search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.pagesize = len(info.pagetext)
        info.save()
        info = SiteInfo_fr()
        info.rooturl = 'zeta-cen-tau.com'
        info.url = 'http://zeta-cen-tau.com/pa-e.htm'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagetext = '<html><head><title>WbSrch</title></head><body><h1>WbSrch Search Engine</h1></body></html>'
        info.pagedescription = 'search engine'
        info.pagekeywords = 'search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.pagesize = len(info.pagetext)
        info.save()
        info = SiteInfo_fr()
        info.rooturl = 'zeta-centaur.com'
        info.url = 'http://zeta-centaur.com/page.htm'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagetext = '<html><head><title>WbSrch</title></head><body><h1>WbSrch Search Engine</h1></body></html>'
        info.pagedescription = 'search engine'
        info.pagekeywords = 'search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.pagesize = len(info.pagetext)
        info.save()
        info = SiteInfo_fr()
        info.rooturl = 'zetacentauri.com'
        info.url = 'http://zetacentauri.com/page.htm'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagetext = '<html><head><title>WbSrch</title></head><body><h1>WbSrch Search Engine</h1></body></html>'
        info.pagedescription = 'search engine'
        info.pagekeywords = 'search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.pagesize = len(info.pagetext)
        info.save()
        info = SiteInfo_fr()
        info.rooturl = 'zetacentauri.com'
        info.url = 'http://zetacentauri.com/page_underscore.htm'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagetext = '<html><head><title>WbSrch</title></head><body><h1>WbSrch Search Engine</h1></body></html>'
        info.pagedescription = 'search engine'
        info.pagekeywords = 'search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.pagesize = len(info.pagetext)
        info.save()
        info = SiteInfo_fr()
        info.rooturl = 'zetacentauri.com'
        info.url = 'http://zetacentauri.com/page_two_underscores.htm'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagetext = '<html><head><title>WbSrch</title></head><body><h1>WbSrch Search Engine</h1></body></html>'
        info.pagedescription = 'search engine'
        info.pagekeywords = 'search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.pagesize = len(info.pagetext)
        info.save()
        info = SiteInfo()
        info.rooturl = '216.151.3.15'
        info.url = 'http://216.151.3.15/xxy.z'
        info.lastcrawled = timezone.now() - timedelta(days=20)
        info.pagetext = ' '
        info.pagedescription = ' '
        info.pagekeywords = ' '
        info.pagetitle = ' '
        info.pagesize = len(info.pagetext)
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
        except ObjectDoesNotExist:
            pass
        self.assertEqual(term, None)

    def testHTTPSBonus(self):
        httpurl = SiteInfo.objects.get(url=u'http://zetacentauri.com/')
        httprank = CalculateTermValue(httpurl, 'wbsrch')
        httpsurl = SiteInfo.objects.get(url=u'https://zetacentauri.com/')
        httpsrank = CalculateTermValue(httpsurl, 'wbsrch')
        self.assertTrue(httpsrank > httprank)

    def testHyphenPenalty(self):
        """
        Hyphen penalty is not calculated in CalculateTermValue, but rather in
        GetIndexModifiersForDomain
        """
        noh = SiteInfo_fr.objects.get(url=u'http://zetacentauri.com/page.htm')
        norank = GetIndexModifiersForDomain(noh.rooturl, 'fr')
        oneh = SiteInfo_fr.objects.get(url=u'http://zeta-centaur.com/page.htm')
        onerank = GetIndexModifiersForDomain(oneh.rooturl, 'fr', verbose=True)
        threeh = SiteInfo_fr.objects.get(url=u'http://zeta-cen-tau.com/pa-e.htm')
        threerank = GetIndexModifiersForDomain(threeh.rooturl, 'fr')
        self.assertGreater(onerank[1], threerank[1])
        self.assertGreater(norank[1], onerank[1])

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
        except ObjectDoesNotExist:
            pass
        self.assertEqual(term, None)

    def testMultiWordIndexTerm(self):
        BuildIndexForTerm('search engine')
        term = IndexTerm.objects.get(keywords='search engine')
        self.assertEqual(term.num_results, 2)

    def tearDown(self):
        SiteInfo.objects.all().delete()
        SiteInfo_de.objects.all().delete()
        SiteInfo_fr.objects.all().delete()
        IndexTerm.objects.all().delete()
        IndexTerm_de.objects.all().delete()


# This tests not only searching for indexed and non-indexed terms, but also the correct
# behavior of partially-indexed phrases and queueing terms for indexing.
class SearchTestCase(TestCase):
    def setUp(self):
        # Dumb stopgap fix.
        IndexTerm.objects.all().delete()
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
        info.rooturl = 'wbsrch.com'
        info.url = 'http://wbsrch.com/'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagetext = '<html><head><title>WbSrch</title></head><body><h1>WbSrch</h1></body></html>'
        info.pagedescription = 'wbsrch search engine'
        info.pagekeywords = 'wbsrch, search, engine'
        info.pagetitle = 'WbSrch Search Engine'
        info.save()
        info = SiteInfo()
        info.rooturl = 'horsemonkey.com'
        info.url = 'http://horsemonkey.com/'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagetext = '<html><head><title>Horse Monkey</title></head><body><h1>Horse Monkey</h1></body></html>'
        info.pagedescription = 'horse monkey'
        info.pagekeywords = 'horse monkey'
        info.pagetitle = 'Horse Monkey'
        info.save()
        info = SiteInfo_de()
        info.rooturl = 'zimmer.de'
        info.url = 'http://zimmer.de/'
        info.lastcrawled = timezone.now() - timedelta(days=40)
        info.pagetext = '<html><head><title>Zimmer</title></head><body><h1>Zimmer</h1></body></html>'
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
        PendingIndex.objects.all().delete()
        PendingIndex_de.objects.all().delete()
        IndexTerm.objects.all().delete()
        IndexTerm_de.objects.all().delete()
        SiteInfo.objects.all().delete()
        BadQuery.objects.all().delete()


class CleanSearchTextTestCase(TestCase):
    def setUp(self):
        pass

    def testCleanSearchText1(self):
        text = CleanSearchText("test")
        self.assertEqual(text, "test")

    def testCleanSearchText2(self):
        text = CleanSearchText("test ")
        self.assertEqual(text, "test")

    def testCleanSearchText3(self):
        text = CleanSearchText(" test")
        self.assertEqual(text, "test")

    def testCleanSearchText4(self):
        text = CleanSearchText("test-")
        self.assertEqual(text, "test")

    def testCleanSearchText5(self):
        text = CleanSearchText("test'")
        self.assertEqual(text, "test")

    def testCleanSearchText6(self):
        text = CleanSearchText("test,")
        self.assertEqual(text, "test")

    def testCleanSearchText7(self):
        text = CleanSearchText("     test   ")
        self.assertEqual(text, "test")

    def testCleanSearchText8(self):
        text = CleanSearchText("test   test")
        self.assertEqual(text, "test test")

    def testCleanSearchText9(self):
        text = CleanSearchText("test   test    ")
        self.assertEqual(text, "test test")

    def testCleanSearchText10(self):
        text = CleanSearchText("'test")
        self.assertEqual(text, "test")

    def testCleanSearchText11(self):
        text = CleanSearchText("test   test    ")
        self.assertEqual(text, "test test")

    def testCleanSearchText12(self):
        text = CleanSearchText('"test')
        self.assertEqual(text, "test")

    def testCleanSearchText13(self):
        text = CleanSearchText('TEST')
        self.assertEqual(text, "test")

    def testCleanSearchText14(self):
        text = CleanSearchText('tESt')
        self.assertEqual(text, "test")

    def testCleanSearchText15(self):
        text = CleanSearchText('tESt\\')
        self.assertEqual(text, "test")

    def testCleanSearchText16(self):
        text = CleanSearchText('tESt/')
        self.assertEqual(text, "test")

    def testCleanSearchText17(self):
        text = CleanSearchText('test%20test ')
        self.assertEqual(text, "test test")

    def testCleanSearchText18(self):
        text = CleanSearchText('%20test%20test%20')
        self.assertEqual(text, "test test")

    def testCleanSearchText19(self):
        text = CleanSearchText('@}----')
        self.assertEqual(text, "@}----")

    def testCleanSearchText20(self):
        text = CleanSearchText('(test')
        self.assertEqual(text, "test")

    def testCleanSearchText21(self):
        text = CleanSearchText('"test)')
        self.assertEqual(text, "test")

    def testCleanSearchText22(self):
        text = CleanSearchText('(test)')
        self.assertEqual(text, "(test)")

    def testCleanSearchText23(self):
        text = CleanSearchText('void(0)')
        self.assertEqual(text, "void(0)")

    def testCleanSearchText24(self):
        text = CleanSearchText('empty()')
        self.assertEqual(text, "empty()")


class URLErrorTestCase(TestCase):
    def setUp(self):
        pass

    def testAddError(self):
        url = SiteInfo()
        url.rooturl = 'wbsrch.com'
        url.url = 'http://wbsrch.com/'
        url.lastcrawled = timezone.now() - timedelta(days=40)
        url.save()
        AddError(url, '502', 'Bad Gateway')
        AddError(url, '503', 'Service Unavailable')
        self.assertEqual(url.num_errors, 2)

    def testClearErrors(self):
        url = SiteInfo()
        url.rooturl = 'wbsrch.com'
        url.url = 'http://wbsrch.com/someurl/'
        url.lastcrawled = timezone.now() - timedelta(days=40)
        url.num_errors = 1
        url.error_info = '2014-02-06, 502, Bad Gateway\n'
        ClearErrors(url)
        self.assertEqual(url.num_errors, 0)
        self.assertEqual(url.error_info, '')

    def testDeleteAtMaxErrors(self):
        url = SiteInfo()
        url.rooturl = 'wbsrch.com'
        url.url = 'http://wbsrch.com/someotherurl/'
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
        RemoveFromPending('zeus', 'el')
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
        dom = DomainInfo()
        dom.url = 'zetacentauri.com'
        dom.save()

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
        self.assertEqual(logs, 1)

    def testSearchCheese2(self):
        response = self.client.get('/search/?q=cheese&domain=cheese.com')
        self.assertEqual(response.status_code, 200)

    def testExtremelyLongQuery(self):
        response = self.client.get('/search/?q=cheeseisthebestthingintheentireworldicannotgetenoughofitandiwantmoreandmoreandmoreandmorebutpleasedontthinkthatisallieatsometimesthereareburritosorburgersorhotdogsorfalafelsorporkchopsorvariousandsundryotherthingsunderneathmysliceofcheeseandiwouldnthaveitanyotherway')
        self.assertEqual(response.status_code, 200)

    def testExtremelyLongDomainQuery(self):
        response = self.client.get('/search/?q=cheeseisthebestthingintheentireworldicannotgetenoughofitandiwantmoreandmoreandmoreandmorebutpleasedontthinkthatisallieatsometimesthereareburritosorburgersorhotdogsorfalafelsorporkchopsorvariousandsundryotherthingsunderneathmysliceofcheeseandiwouldnthaveitanyotherway&domain=cheese.com')
        self.assertEqual(response.status_code, 200)

    def testPopularSearches(self):
        # Popular searches page has been removed.
        response = self.client.get('/popular-searches/')
        self.assertEqual(response.status_code, 404)

    def testPopularSearches2(self):
        response = self.client.get('/popular-searches/2011/03/')
        self.assertEqual(response.status_code, 404)

    def testDomain(self):
        response = self.client.get('/domain/')
        self.assertEqual(response.status_code, 200)

    def testSearchDomain(self):
        response = self.client.get('/domain/?q=zetacentauri.com')
        self.assertEqual(response.status_code, 200)

    def testSearchNoDomain(self):
        response = self.client.get('/domain/?q=asdfkasasdfjasdflaksdf.net')
        self.assertEqual(response.status_code, 404)

    # Still need to test:
    # def domainrank(request):
    # def adminpanel_doctype(request):
    # Popular searches with an actual search history month/year combo:
    # def popular_searches(request, year=None, month=None):

    def tearDown(self):
        SearchLog.objects.all().delete()
        DomainInfo.objects.all().delete()


class BlockedSiteTestCase(TestCase):
    def setUp(self):
        info = SiteInfo()
        info.rooturl = 'spamsite.com'
        info.url = 'http://spamsite.com/1/'
        info.save()
        info = SiteInfo_cs()
        info.rooturl = 'spamsite.cz'
        info.url = 'http://spamsite.cz/1/'
        info.save()
        info = SiteInfo_cs()
        info.rooturl = 'spamsite.cz'
        info.url = 'http://spamsite.cz/2/'
        info.save()
        info = SiteInfo_cs()
        info.rooturl = 'notaspamsite.cz'
        info.url = 'http://notaspamsite.cz/1/'
        info.save()
        domain = DomainInfo()
        domain.url = 'spamsite.cz'
        domain.language_association = u'cs'
        domain.save()

    def testExcludeUrl(self):
        exclude = BlockedSite()
        exclude.url = 'spamsite.com'
        exclude.save()
        self.assertEqual(SiteInfo.objects.all().count(), 0)

    def testExcludeCzechUrl(self):
        exclude = BlockedSite()
        exclude.url = 'spamsite.cz'
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
        print(s)

    def testChangeLogItem(self):
        i = ChangelogItem()
        print(i)

    def testBlockedSite(self):
        e = BlockedSite()
        print(e)

    def testDomainInfo(self):
        e = DomainInfo()
        print(e)

    def testDomainExtension(self):
        e = DomainSuffix()
        print(e)

    def testPendingUrl(self):
        e = CrawlableUrl()
        print(e)

    def testSiteInfo(self):
        e = SiteInfo()
        print(e)

    def testSearchLog(self):
        e = SearchLog()
        print(e)

    def testPendingIndex(self):
        e = PendingIndex()
        print(e)

    def testIndexTerm(self):
        e = IndexTerm()
        print(e)

    def testIPAddress(self):
        e = IPAddress()
        print(e)

    def tearDown(self):
        pass


class IndexStatsTestCase(TestCase):
    def setUp(self):
        info = SiteInfo()
        info.rooturl = 'spamsite.com'
        info.url = 'http://spamsite.com/1/'
        info.save()
        info = SiteInfo_cs()
        info.rooturl = 'spamsite.cz'
        info.url = 'http://spamsite.cz/1/'
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
        info.rooturl = 'example.com'
        info.url = 'http://example.com/1/'
        info.lastcrawled = timezone.now()
        info.save()
        info = SiteInfo()
        info.rooturl = 'exampletwo.com'
        info.url = 'http://exampletwo.com/1/'
        info.lastcrawled = timezone.now()
        info.save()
        info = SiteInfo()
        info.rooturl = 'examplethree.com'
        info.url = 'http://examplethree.com/1/'
        info.lastcrawled = timezone.now()
        info.save()
        info = SiteInfo()
        info.rooturl = 'examplefour.com'
        info.url = 'http://examplefour.com/1/'
        info.lastcrawled = timezone.now()
        info.save()
        info = SiteInfo()
        info.rooturl = 'examplefour.com'
        info.url = 'http://examplefour.com/2/'
        info.lastcrawled = timezone.now()
        info.save()
        info = SiteInfo_cs()
        info.rooturl = 'example.cz'
        info.url = 'http://example.cz/1/'
        info.lastcrawled = timezone.now()
        info.save()
        domain = DomainInfo()
        domain.url = 'example.com'
        domain.language_association = 'en'
        domain.save()
        domain = DomainInfo()
        domain.url = 'exampletwo.com'
        domain.language_association = ''
        domain.save()
        domain = DomainInfo()
        domain.url = 'example.cz'
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
        self.assertEqual(domain.language_association, 'fr')
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
        self.assertEqual(domain.language_association, 'en')
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
        info.rooturl = 'notporn.com'
        info.url = 'http://notporn.com/1/'
        info.save()
        info = SiteInfo()
        info.rooturl = 'notporn.com'
        info.url = 'http://notporn.com/2/'
        info.save()
        info = SiteInfo()
        info.rooturl = 'pornsite.com'
        info.url = 'http://pornsite.com/1/'
        info.save()
        info = SiteInfo()
        info.rooturl = 'pornsite.com'
        info.url = 'http://pornsite.com/2/'
        info.save()
        info = SiteInfo()
        info.rooturl = 'ass.pornsite2.com'
        info.url = 'http://ass.pornsite2.com/2/'
        info.save()
        info = SiteInfo()
        info.rooturl = 'pornsite2.com'
        info.url = 'http://pornsite2.com/2/'
        info.save()
        info = SiteInfo()
        info.rooturl = 'pornsite3.com'
        info.url = 'http://pornsite3.com/2/'
        info.save()
        info = SiteInfo()
        info.rooturl = 'ass.pornsite.com'
        info.url = 'http://ass.pornsite.com/1/'
        info.save()
        info = SiteInfo()
        info.rooturl = 'ass.pornsite.com'
        info.url = 'http://ass.pornsite.com/2/'
        info.save()
        info = SiteInfo_it()
        info.rooturl = 'pornsite.it'
        info.url = 'http://pornsite.it/1/'
        info.save()
        info = SiteInfo_it()
        info.rooturl = 'pornsite.it'
        info.url = 'http://pornsite.it/2/'
        info.save()
        info = SiteInfo_it()
        info.rooturl = 'ass.pornsite.it'
        info.url = 'http://ass.pornsite.it/2/'
        info.save()
        domain = DomainInfo()
        domain.url = 'notporn.com'
        domain.is_unblockable = True
        domain.save()
        domain = DomainInfo()
        domain.url = 'pornsite3.com'
        domain.is_unblockable = False
        domain.language_association = 'en'
        domain.save()
        domain = DomainInfo()
        domain.url = 'pornsite.it'
        domain.language_association = u'it'
        domain.save()
        domain = DomainInfo()
        domain.url = 'ass.pornsite.it'
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
        assexclusion = BlockedSite.objects.filter(url=u'ass.pornsite2.com')
        pornexclusion = BlockedSite.objects.filter(url=u'pornsite2.com')
        self.assertEqual(assurls, 1)
        self.assertEqual(pornurls, 0)
        self.assertEqual(assexclusion.count(), 0)
        self.assertEqual(pornexclusion.count(), 1)
        self.assertEqual(pornexclusion[0].exclude_subdomains, True)

    def testPornBlockParent2(self):
        site = SiteInfo.objects.get(url=u'http://pornsite3.com/2/')
        PornBlock(site)
        pornurls = SiteInfo.objects.filter(rooturl=u'pornsite3.com').count()
        pornexclusion = BlockedSite.objects.filter(url=u'pornsite3.com')
        DomainInfo.objects.get(url=u'pornsite3.com')
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
        print(ages)
        self.assertNotEqual(ages, None)


class ReverseWWWTestCase(TestCase):
    def testroot(self):
        self.assertEqual(ReverseWWW(u'example.com'), 'www.example.com')

    def testwww(self):
        self.assertEqual(ReverseWWW(u'example.com'), 'www.example.com')

    def testrootonlytld(self):
        self.assertEqual(ReverseWWW(u'example.com', True), 'www.example.com')

    def testrootonlywwwtld(self):
        self.assertEqual(ReverseWWW(u'www.example.com', True), 'example.com')

    def testrootonlysecondleveltld(self):
        self.assertEqual(ReverseWWW(u'example.co.uk', True), 'www.example.co.uk')

    def testrootonlysecondlevel(self):
        self.assertEqual(ReverseWWW(u'my.example.com', True), None)


class GetDomainExtensionAdjustmentTextCase(TestCase):
    def testcom(self):
        self.assertEqual(GetDomainExtensionRankAdjustment('.com', 'en'), 3)

    def testcom2(self):
        self.assertEqual(GetDomainExtensionRankAdjustment('example.com', None), 3)

    def testcom3(self):
        self.assertEqual(GetDomainExtensionRankAdjustment('website.example.com', 'en'), 3)

    def testcn(self):
        self.assertEqual(GetDomainExtensionRankAdjustment('.cn', 'en'), -6)

    def testru(self):
        self.assertEqual(GetDomainExtensionRankAdjustment('ru', 'en'), -6)

    def testxxx(self):
        self.assertEqual(GetDomainExtensionRankAdjustment('xxx', 'en'), -50)

    def testunknown(self):
        self.assertEqual(GetDomainExtensionRankAdjustment('example.unknowndomainextension', 'en'), -3)

    def testcasaen(self):
        self.assertEqual(GetDomainExtensionRankAdjustment('mi.casa', 'en'), -1)

    def testcasaes(self):
        self.assertEqual(GetDomainExtensionRankAdjustment('mi.casa', 'es'), 1)


class RemoveExtraSpacesTestCase(TestCase):
    def spacetest1(self):
        self.assertEqual(RemoveExtraSpaces('test'), 'test')

    def spacetest2(self):
        self.assertEqual(RemoveExtraSpaces(' test '), 'test')

    def spacetest3(self):
        self.assertEqual(RemoveExtraSpaces('te   st'), 'te st')

    def spacetest4(self):
        self.assertEqual(RemoveExtraSpaces('\ttest\n'), 'test')

    def spacetest5(self):
        self.assertEqual(RemoveExtraSpaces('te \n st'), 'te st')

    def spacetest6(self):
        self.assertEqual(RemoveExtraSpaces('t  e  s \n\r\n\r   t'), 't e s t')

    def spacetest7(self):
        self.assertEqual(RemoveExtraSpaces('\n\n\n\n\ntest'), 'test')

    def spacetest8(self):
        self.assertEqual(RemoveExtraSpaces('test       \n\n\n\n\t\r\n\t\r'), 'test')


class IsDomainParkedTestCase(TestCase):
    def setUp(self):
        site1 = SiteInfo()
        site1.rooturl = 'example.com'
        site1.pagetitle = 'This website is for sale'
        site1.pagetext = 'ya wanna buy it?'
        site1.url = 'http://example.com/1/'
        site1.save()
        site2 = SiteInfo()
        site2.rooturl = 'example.com'
        site2.pagetitle = ''
        site2.pagetext = 'The Sponsored Listings displayed above are served automatically by a third party.'
        site2.url = 'http://example.com/2/'
        site2.save()
        site3 = SiteInfo()
        site3.rooturl = 'example.com'
        site3.pagetitle = 'Free pants'
        site3.pagetext = 'just click here for free pants'
        site3.url = 'http://example.com/3/'
        site3.save()
        site4 = SiteInfo()
        site4.rooturl = 'example.com'
        site4.pagetitle = 'This domain is not for sale'
        site4.pagetext = 'Do not click here to buy it'
        site4.url = 'http://example.com/4/'
        site4.save()
        site5 = SiteInfo()
        site5.rooturl = 'example.com'
        site5.pagetitle = ''
        site5.pagetext = ''
        site5.url = 'https://example.com/5/'
        site5.save()
        site6 = SiteInfo()
        site6.rooturl = 'example.com'
        site6.pagetitle = 'Expired - domain expired'
        site6.pagetext = ''
        site6.url = 'https://example.com/6/'
        site6.save()

    def parktest1(self):
        site = SiteInfo.objects.get(url='http://example.com/1/')
        self.assertEqual(IsDomainParked(site), True)

    def parktest2(self):
        site = SiteInfo.objects.get(url='http://example.com/2/')
        self.assertEqual(IsDomainParked(site), True)

    def parktest3(self):
        site = SiteInfo.objects.get(url='http://example.com/3/')
        self.assertEqual(IsDomainParked(site), False)

    def parktest4(self):
        site = SiteInfo.objects.get(url='http://example.com/4/')
        self.assertEqual(IsDomainParked(site), False)

    def parktest5(self):
        site = SiteInfo.objects.get(url='https://example.com/5/')
        self.assertEqual(IsDomainParked(site), False)

    def parktest6(self):
        site = SiteInfo.objects.get(url='https://example.com/6/')
        self.assertEqual(IsDomainParked(site), True)

    def tearDown(self):
        SiteInfo.objects.all().delete()


class HasNoContentTestCase(TestCase):
    def setUp(self):
        site1 = SiteInfo()
        site1.rooturl = 'example.com'
        site1.pagetitle = 'Account Suspended'
        site1.pagetext = 'Please contact support to reactivate your account.'
        site1.url = 'http://example.com/1/'
        site1.save()
        site2 = SiteInfo()
        site2.rooturl = 'example.com'
        site2.pagetitle = 'Coming Soon'
        site2.pagetext = 'Coming Soon'
        site2.url = 'http://example.com/2/'
        site2.save()
        site3 = SiteInfo()
        site3.rooturl = 'example.com'
        site3.pagetitle = 'Free pants'
        site3.pagetext = 'just click here for free pants'
        site3.url = 'http://example.com/3/'
        site3.save()
        site4 = SiteInfo()
        site4.rooturl = 'example.com'
        site4.pagetitle = 'This domain is not for sale'
        site4.pagetext = 'Do not click here to buy it'
        site4.url = 'http://example.com/4/'
        site4.save()
        site5 = SiteInfo()
        site5.rooturl = 'example.com'
        site5.pagetitle = ''
        site5.pagetext = ''
        site5.url = 'https://example.com/5/'
        site5.save()
        site6 = SiteInfo()
        site6.rooturl = 'example.com'
        site6.pagetitle = '502 Bad Gateway'
        site6.pagetext = ''
        site6.url = 'https://example.com/6/'
        site6.save()

    def parktest1(self):
        site = SiteInfo.objects.get(url='http://example.com/1/')
        self.assertEqual(IsDomainParked(site), True)

    def parktest2(self):
        site = SiteInfo.objects.get(url='http://example.com/2/')
        self.assertEqual(IsDomainParked(site), True)

    def parktest3(self):
        site = SiteInfo.objects.get(url='http://example.com/3/')
        self.assertEqual(IsDomainParked(site), False)

    def parktest4(self):
        site = SiteInfo.objects.get(url='http://example.com/4/')
        self.assertEqual(IsDomainParked(site), False)

    def parktest5(self):
        site = SiteInfo.objects.get(url='https://example.com/5/')
        self.assertEqual(IsDomainParked(site), False)

    def parktest6(self):
        site = SiteInfo.objects.get(url='https://example.com/6/')
        self.assertEqual(IsDomainParked(site), True)

    def tearDown(self):
        SiteInfo.objects.all().delete()
