
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from dir.models import language_list, DomainInfo, BlockedSite, PageLink, PageIFrame, PageJavaScript
from dir.utils import GetSiteInfoModelFromLanguage, GetKeywordRankingModelFromLanguage


class Command(BaseCommand):
    help = """
    This utility function goes trhough all of the root URLs for crawled pages
    and removes :443 and the like from existing pages.

    Now that the root url parser doesn't keep : suffixes, this may never need
    to be run again.
    """
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for language in language_list:
            # Pages
            site_model = GetSiteInfoModelFromLanguage(language)
            print('Processing {0} pages.'.format(language))
            infos = site_model.objects.filter(rooturl__icontains=':')
            count = 0
            for info in infos:
                root = info.rooturl.split(':')[0]
                print('Changing {0} to {1}'.format(info.rooturl, root))
                info.rooturl = root
                info.save()
                count += 1
            print('{0} root urls fixed in {1} pages.'.format(count, language))

            # Keyword rankingss
            keyword_model = GetKeywordRankingModelFromLanguage(language)
            print('Processing {0} keyword rankings.'.format(language))
            ranks = keyword_model.objects.filter(rooturl__icontains=':')
            count = 0
            for rank in ranks:
                root = rank.rooturl.split(':')[0]
                print('Changing {0} to {1}'.format(rank.rooturl, root))
                rank.rooturl = root
                rank.save()
                count += 1
            print('{0} root urls fixed in {1} keyword rankings.'.format(count, language))

        # Domain info
        print('Processing domain info.')
        infos = DomainInfo.objects.filter(url__icontains=':')
        count = 0
        for info in infos:
            root = info.url.split(':')[0]
            existing = DomainInfo.objects.filter(url=root).first()
            if existing:
                print('Clean version of {0} already exists. Deleting.'.format(info.url))
                info.delete()
                continue
            print('Changing {0} to {1}'.format(info.url, root))
            info.url = root
            info.save()
            count += 1
        print('{0} root urls fixed in domain info.'.format(count))

        # Blocked sites
        print('Processing blocked sites.')
        infos = BlockedSite.objects.filter(url__icontains=':')
        count = 0
        for info in infos:
            root = info.url.split(':')[0]
            existing = BlockedSite.objects.filter(url=root).first()
            if existing:
                print('Clean version of {0} already exists. Deleting.'.format(info.url))
                info.delete()
                continue
            print('Changing {0} to {1}'.format(info.url, root))
            info.url = root
            info.save()
            count += 1
        print('{0} root urls fixed in blocked sites.'.format(count))

        # Page links
        print('Processing page links.')
        links = PageLink.objects.filter(rooturl_source__icontains=':')
        count = 0
        for link in links:
            root = link.rooturl_source.split(':')[0]
            print('Changing {0} rooturl_source to {1}'.format(link.rooturl_source, root))
            link.rooturl_source = root
            link.save()
            count += 1
        print('{0} rooturl_sources fixed in page links.'.format(count))
        links = PageLink.objects.filter(rooturl_destination__icontains=':')
        count = 0
        for link in links:
            root = link.rooturl_destination.split(':')[0]
            print('Changing {0} rooturl_destination to {1}'.format(link.rooturl_destination, root))
            link.rooturl_destination = root
            link.save()
            count += 1
        print('{0} rooturl_destinations fixed in page links.'.format(count))

        # Page iframes
        print('Processing page iframes.')
        links = PageIFrame.objects.filter(rooturl_source__icontains=':')
        count = 0
        for link in links:
            root = link.rooturl_source.split(':')[0]
            print('Changing {0} rooturl_source to {1}'.format(link.rooturl_source, root))
            link.rooturl_source = root
            link.save()
            count += 1
        print('{0} rooturl_sources fixed in page iframes.'.format(count))
        links = PageIFrame.objects.filter(rooturl_destination__icontains=':')
        count = 0
        for link in links:
            root = link.rooturl_destination.split(':')[0]
            print('Changing {0} rooturl_destination to {1}'.format(link.rooturl_destination, root))
            link.rooturl_destination = root
            link.save()
            count += 1
        print('{0} rooturl_destinations fixed in page iframes.'.format(count))

        # Page javascripts
        print('Processing page javascripts.')
        links = PageJavaScript.objects.filter(rooturl_source__icontains=':')
        count = 0
        for link in links:
            root = link.rooturl_source.split(':')[0]
            print('Changing {0} rooturl_source to {1}'.format(link.rooturl_source, root))
            link.rooturl_source = root
            link.save()
            count += 1
        print('{0} rooturl_sources fixed in page javascripts.'.format(count))
        links = PageJavaScript.objects.filter(rooturl_destination__icontains=':')
        count = 0
        for link in links:
            root = link.rooturl_destination.split(':')[0]
            print('Changing {0} rooturl_destination to {1}'.format(link.rooturl_destination, root))
            link.rooturl_destination = root
            link.save()
            count += 1
        print('{0} rooturl_destinations fixed in page javascripts.'.format(count))
