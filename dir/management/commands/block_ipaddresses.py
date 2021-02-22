
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from dir.models import DomainInfo, language_list, PageLink, PageIFrame, PageJavaScript, CrawlableUrl
from dir.utils import IsIPAddress, GetSiteInfoModelFromLanguage


class Command(BaseCommand):
    help = """
    This utility command goes through all pages and domains, deleting any that are a raw
    IP address. Now that the crawler rejects those, it may never be necessary to run this
    function. It was created as a cleanup utilty when the crawler was changed to exclude those.
    """
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for language in language_list:
            site_model = GetSiteInfoModelFromLanguage(language)
            print('Processing {0} pages'.format(language))
            infos = site_model.objects.filter(rooturl__lt='3')
            count = 0
            for info in infos:
                if IsIPAddress(info.rooturl):
                    print('{0} SiteInfo needs to be deleted.'.format(info.url))
                    count += 1
                    info.delete()
            print('{0} IP adddress urls deleted'.format(count))

        print('Processing domains')
        infos = DomainInfo.objects.filter(url__lt='3')
        count = 0
        for info in infos:
            if IsIPAddress(info.url):
                print('{0} DomainInfo needs to be deleted.'.format(info.url))
                count += 1
                info.delete()
        print('{0} IP adddress domains deleted'.format(count))

        print('Processng page javascript.')
        urls = PageJavaScript.objects.filter(rooturl_source__lt='3')
        count = 0
        for url in urls:
            if IsIPAddress(url.rooturl_source):
                print('Source {0} PageJavaScript needs to be deleted.'.format(url.url_source))
                count += 1
                url.delete()
        print('{0} page javascript deleted.'.format(count))

        print('Processing page iframes.')
        urls = PageIFrame.objects.filter(rooturl_source__lt='3')
        count = 0
        for url in urls:
            if IsIPAddress(url.rooturl_source):
                print('Source {0} PageIFrame needs to be deleted.'.format(url.url_source))
                count += 1
                url.delete()
        print('{0} page iframes deleted.'.format(count))

        print('Processing page links.')
        urls = PageLink.objects.filter(rooturl_source__lt='3')
        count = 0
        for url in urls:
            if IsIPAddress(url.rooturl_source):
                print('Source {0} PageLink needs to be deleted.'.format(url.url_source))
                count += 1
                url.delete()
        print('{0} page links deleted.'.format(count))

        print('Processing pending urls.')
        urls = CrawlableUrl.objects.filter(rooturl__lt='3')
        count = 0
        for url in urls:
            if IsIPAddress(url.rooturl):
                print('{0} CrawlableURL needs to be deleted.'.format(url.url))
                count += 1
                url.delete()
        print('{0} pending urls deleted.'.format(count))
