# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from dir.models import QueryParameter, DomainInfo, PageLink, SiteInfo
from dir.utils import GetSiteInfoModelFromLanguage, NormalizeUrl
from pytz.exceptions import AmbiguousTimeError
import time


class Command(BaseCommand):
    help = "Processes URL parameter rules for domains with specifically tagged URL parameters to ensure their URLs are clean."

    def add_arguments(self, parser):
        parser.add_argument('-u', '--urls', default=5000000, action='store', type=int, dest='urls', help='Max number of URLs to process. (default=5000000)')
        parser.add_argument('-s', '--sleep', default=1, action='store', type=int, dest='sleep', help='Time to sleep between domain queries. (default=1)')
        parser.add_argument('-o', '--offset', default=0, action='store', type=int, dest='offset', help='Domain slice offset - distance from beginning to start. (ignored if alphastart is set)')
        parser.add_argument('-d', '--domain', default=None, action='store', dest='domain', help='Only check a specific domain.')
        parser.add_argument('-a', '--alphastart', default=None, action='store', dest='alphastart', help='Alphabetic start point for everything processing.')

    def handle(self, *args, **options):
        print(options)
        domain = options.get('domain', None)
        force = options.get('domain', None)
        offset = options.get('offset', None)
        maxurls = options['urls']
        numurls = 0
        domains = []
        if not domain:
            alphastart = options.get('alphastart', None)
            if alphastart:
                records = SiteInfo.objects.filter(rooturl__gt=alphastart).distinct('rooturl').values('rooturl').order_by('rooturl')
            else:
                if offset:
                    records = SiteInfo.objects.distinct('rooturl').values('rooturl').order_by('rooturl')[offset:]
                else:
                    records = SiteInfo.objects.distinct('rooturl').values('rooturl').order_by('rooturl')
            print('{0} domains found.'.format(records.count()))
            for record in records:
                domains.append(record['rooturl'])
        elif domain:
            domains.append(domain)
        for dom in domains:
            try:
                di = DomainInfo.objects.get(url=dom)
                site_model = GetSiteInfoModelFromLanguage(di.language_association)
            except Exception:
                site_model = GetSiteInfoModelFromLanguage('en')
            urls = site_model.objects.filter(rooturl=dom)
            # print('{0} urls found.'.format(urls.count()))
            for url in urls:
                num_links_updated = 0
                num_links_deleted = 0
                try:
                    normed = NormalizeUrl(url.url, post_crawl_replacement=True)
                except UnicodeEncodeError:
                    print('URL has a unicode encode error and is not valid. Deleting.')
                    try:
                        print('OFFENDING URL IS: {0}'.format(url.url))
                    except Exception:
                        pass
                    links = PageLink.objects.filter(url_source=url.url)
                    for link in links:
                        link.delete()
                        num_links_deleted = num_links_deleted + 1
                    url.delete()
                    numurls = numurls + 1
                    continue
                if normed != url.url:
                    print('{0} IS NOW {1}'.format(url.url, normed))
                    try:
                        site_model.objects.get(url=normed)
                        print('DUPLICATE URL FOUND. DELETING.')
                        url.delete()
                    except ObjectDoesNotExist:
                        links = PageLink.objects.filter(url_source=url.url)
                        for link in links:
                            try:
                                PageLink.objects.get(url_source=normed, url_destination=link.url_destination)
                                link.delete()
                                num_links_deleted = num_links_deleted + 1
                            except ObjectDoesNotExist:
                                link.url_source = normed
                                link.save()
                                num_links_updated = num_links_updated + 1
                        url.url = normed
                        try:
                            url.save()
                        except AmbiguousTimeError:
                            print('AmbiguousTimeError saving url {0}, not saved'.format(url.url))
                    if num_links_updated > 0 or num_links_deleted > 0:
                        print('{0} URL LINKS UPDATED AND {1} DLETED'.format(num_links_updated, num_links_deleted))
                numurls = numurls + 1
                if numurls > maxurls:
                    break
            if numurls > maxurls:
                break
        time.sleep(options['sleep'])

