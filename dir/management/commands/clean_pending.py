# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from optparse import make_option
from dir.models import *
from dir.utils import *
from dir.crawler import AddPendingLink
import robotexclusionrulesparser 
from django.utils import timezone

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-m', '--maxurls', default=10, action='store', type='int', dest='maxurls', help='Max number of URLs to clean. (default=10)'),
        make_option('-o', '--offset', default=0, action='store', type='int', dest='offset', help='Record offset for pending clean.'),
        make_option('-d', '--detailed', default=False, action='store_true', dest='detailed', help='Print details of whether we kept or nuked each URL.'),
        make_option('-j', '--justbadrandoms', default=False, action='store_true', dest='justbadrandoms', help='Only process records with a bad random id.'),
    )

    def handle(self, *args, **options):
        start = timezone.now()
        ok = 0
        deleted = 0
        changed = 0
        duplicate = 0
        malformed = 0
        blockedbyrobots = 0
        randfixed = 0
        processed = 0
        max = 50000
        if options.has_key('maxurls'):
            max = int(options['maxurls'])
        offset = 0
        if options.has_key('offset'):
            offset = int(options['offset'])
        detailed = options['detailed']
        print u'Cleaning urls with a max of ' + str(max) + u' and offset ' + str(offset) + u'.'
        if options['justbadrandoms']:
            pending = PendingUrl.objects.filter(randval=1123022592)
        else:
            pending = PendingUrl.objects.all()
        rerp = robotexclusionrulesparser.RobotExclusionRulesParser()
        pending = pending[offset:offset+max]
        for link in pending:
            processed = processed + 1
            if processed % 10000 == 0:
                elapsed = timezone.now() - start
                print 'Processed {0} URLs in {1} seconds.'.format(processed, elapsed.total_seconds())
            try:
                normed = NormalizeUrl(link.url, pre_crawl_replacement=True)
            except UnicodeEncodeError:
                link.delete()
                malformed = malformed + 1
                continue
            if normed != link.url:
                if detailed:
                    try:
                        print u'{0} changed to {1}'.format(link.url, normed)
                    except:
                        pass
                link.delete()
                try:
                    pending = CrawlableUrl.objects.get(url=normed)
                    duplicate += 1
                except ObjectDoesNotExist:
                    pending = CrawlableUrl()
                    pending.url = normed
                    pending.rooturl = GetRootUrl(pending.url)
                    try:
                        pending.save()
                        changed += 1
                    except IntegrityError:
                       # The only reason we would get an integrity error is if we
                       # violate the unique key constraint of the database. If we
                       # did that, it means that the URL is already in there and we
                       # can safely delete it.
                       connection._rollback()
                       duplicate += 1
                continue
            if CanCrawlUrl(link.url):
                try:
                    if detailed:
                        print link.url + u' OK'
                except:
                    pass
                rooturl = GetRootUrl(link.url)
                try:
                    domain = DomainInfo.objects.get(url=rooturl)
                except ObjectDoesNotExist:
                    ok = ok + 1
                    if link.randval == 1123022592:
                        randfixed = randfixed + 1
                    pending = CrawlableUrl()
                    pending.url = link.url
                    pending.rooturl = rooturl
                    try:
                        pending.save()
                    except IntegrityError:
                        # The only reason we would get an integrity error is if we
                        # violate the unique key constraint of the database. If we
                        # did that, it means that the URL is already in there and we
                        # can safely delete it.
                        connection._rollback()
                        duplicate += 1
                    link.delete()
                    #print 'Random is now {0}'.format(link.randval)
                    continue
                if domain.robots_last_updated and domain.robots_txt and len(domain.robots_txt) > 0:
                    rerp.parse(domain.robots_txt)
                    if rerp.is_allowed('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', link.url):
                        ok = ok + 1
                        pending = CrawlableUrl()
                        pending.url = link.url
                        pending.rooturl = rooturl
                        try:
                            pending.save()
                            changed += 1
                        except IntegrityError:
                            # The only reason we would get an integrity error is if we
                            # violate the unique key constraint of the database. If we
                            # did that, it means that the URL is already in there and we
                            # can safely delete it.
                            connection._rollback()
                            duplicate += 1
                        link.delete()
                    else:
                        #try:
                        #    print link.url + u' DELETED DUE TO ROBOTS.TXT'
                        #except:
                        #    pass
                        link.delete()
                        deleted = deleted + 1
                        blockedbyrobots = blockedbyrobots + 1
                else:
                    ok = ok + 1
                    if link.randval == 1123022592:
                        randfixed = randfixed + 1
                    pending = CrawlableUrl()
                    pending.url = link.url
                    pending.rooturl = rooturl
                    try:
                        pending.save()
                        changed += 1
                    except IntegrityError:
                        # The only reason we would get an integrity error is if we
                        # violate the unique key constraint of the database. If we
                        # did that, it means that the URL is already in there and we
                        # can safely delete it.
                        connection._rollback()
                        duplicate += 1
                    link.delete()
                    #print 'Random is now {0}'.format(link.randval)
            else:
                try:
                    if detailed:
                        print link.url + u' DELETED'
                except:
                    pass
                link.delete()
                deleted = deleted + 1
        print u'Deleted {0} and moved {1} urls, {2} changed and moved, {3} deleted duplicate, {4} deleted malformed, {5} randfixed and moved. Of those deleted, {6} were deleted due to robots.txt'.format(deleted, ok, changed, duplicate, malformed, randfixed, blockedbyrobots)
