# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from optparse import make_option
from dir.models import QueryParameter, DomainInfo, PageLink, SiteInfo
from dir.utils import GetSiteInfoModelFromLanguage, NormalizeUrl
from pytz.exceptions import AmbiguousTimeError
import time

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-m', '--max', default=5, action='store', type='int', dest='max', help='Max number of domains to update. (default=5)'),
        make_option('-u', '--urls', default=100000, action='store', type='int', dest='urls', help='Max number of URLs to process. (default=100000)'),
        make_option('-s', '--sleep', default=1, action='store', type='int', dest='sleep', help='Time to sleep between domain queries. (default=1)'),
        make_option('-o', '--offset', default=0, action='store', type='int', dest='offset', help='Domain slice offset - distance from beginning to start. (default=0)'),
        make_option('-d', '--domain', default=None, action='store', type='string', dest='domain', help='Only check a specific domain.'),
        make_option('-f', '--force', default=False, action='store_true', dest='force', help='Check the domain regardless of rules.'),
        make_option('-e', '--everything', default=False, action='store_true', dest='everything', help='Check URL tags on everything.'),
        make_option('-a', '--alphastart', default=None, action='store', dest='alphastart', help='Alphabetic start point for everything processing.'),
    )

    def handle(self, *args, **options):
        domain = options.get('domain', None)
        force = options.get('domain', None)
        if domain:
            params = QueryParameter.objects.filter(domain=domain)
        else:
            params = QueryParameter.objects.all()[options['offset']:(options['max']+options['offset'])]
        maxurls = options['urls']
        numurls = 0
        domains = []
        if options.get('everything', None):
            alphastart = options.get('alphastart', None)
            if alphastart:
                records = SiteInfo.objects.filter(rooturl__gt=alphastart).distinct('rooturl').values('rooturl').order_by('rooturl')
            else:
                records = SiteInfo.objects.distinct('rooturl').values('rooturl').order_by('rooturl')
            print u'{0} domains found.'.format(records.count())
            rcount = 0
            for record in records:
                #print record['rooturl']
                domains.append(record['rooturl'])
        elif force and domain:
            domains.append(domain)
        for param in params:
            if not param.domain in domains:
                domains.append(param.domain)
        for dom in domains:
            try:
                di = DomainInfo.objects.get(url=dom)
                site_model = GetSiteInfoModelFromLanguage(di.language_association)
            except:
                site_model = GetSiteInfoModelFromLanguage('en')
            print u'Updating {0} with data from {1}'.format(dom, site_model)
            urls = site_model.objects.filter(rooturl=dom)
            print u'{0} urls found.'.format(urls.count())
            for url in urls:
                num_links_updated = 0
                num_links_deleted = 0
                try:
                    normed = NormalizeUrl(url.url, post_crawl_replacement=True)
                except UnicodeEncodeError:
                    print u'URL has a unicode encode error and is not valid. Deleting.'
                    try:
                        print u'OFFENDING URL IS: {0}'.format(url.url)
                    except:
                        pass
                    links = PageLink.objects.filter(url_source=url.url)
                    for link in links:
                        link.delete()
                        num_links_deleted = num_links_deleted + 1
                    url.delete()
                    numurls = numurls + 1
                    continue
                if normed != url.url:
                    print u'{0} IS NOW {1}'.format(url.url, normed)
                    try:
                        existing = site_model.objects.get(url=normed)
                        print u'DUPLICATE URL FOUND. DELETING.'
                        url.delete()
                    except ObjectDoesNotExist:
                        links = PageLink.objects.filter(url_source=url.url)
                        for link in links:
                            try:
                                existing = PageLink.objects.get(url_source=normed, url_destination=link.url_destination)
                                link.delete()
                                num_links_deleted = num_links_deleted + 1
                            except ObjectDoesNotExist:
                                link.url_source = normed
                                link.save()
                                num_links_update = num_links_updated + 1
                        url.url = normed
                        try:
                            url.save()
                        except AmbiguousTimeError, e:
                            print u'AmbiguousTimeError saving url {0}, not saved'.format(url.url)
                    if num_links_updated > 0 or num_links_deleted > 0:
                        print u'{0} URL LINKS UPDATED AND {1} DLETED'.format(num_links_updated, num_links_deleted)
                numurls = numurls + 1
                if numurls > maxurls:
                    break
            if numurls > maxurls:
                break
        time.sleep(options['sleep'])
