# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from zetaweb import settings
from optparse import make_option
from dir.models import PendingIndex, IndexTerm, DomainInfo
from dir.utils import GetIndexModelFromLanguage, GetSiteInfoModelFromLanguage
from dir.views import language_list
import dateutil.parser
import pytz

class Command(BaseCommand):
    help = """
    Shows the oldest indexes and/or the oldest index items. Or shows the oldest crawled URLs.
    """
    option_list = BaseCommand.option_list + (
        make_option('-d', '--date', default=None, action='store', type='string', dest='date', help='Date to show old index or url counts from (default=do not show).'),
        make_option('-o', '--oldest', default=False, action='store_true', dest='oldest', help='Show oldest indexes (dfault=False).'),
        make_option('-a', '--averageage', default=False, action='store_true', dest='averageage', help='Show average age, takes a long time (dfault=False).'),
        make_option('-s', '--showempty', default=False, action='store_true', dest='showempty', help='Show empty index counts (use with -d).'),
        make_option('-u', '--urls', default=False, action='store_true', dest='showurls', help='Show oldest urls by language.'),
    )

    def handle(self, *args, **options):
        sdate = None
        datestr = options.get('date', None)
        showempty = options.get('showempty', False)
        msgs1 = []
        msgs2 = []
        msgs3 = []
        total_items = 0
        if datestr:
            sdate = dateutil.parser.parse(datestr)
            sdate = pytz.timezone(settings.TIME_ZONE).localize(sdate)
        for language in language_list:
            index_model = GetIndexModelFromLanguage(language)
            site_model = GetSiteInfoModelFromLanguage(language)
            if options['averageage']:
                items = index_model.objects.all().values('date_indexed')
                numitems = 0
                totalage = 0
                nowtime = timezone.now().date()
                for item in items:
                    dateindexed = item['date_indexed'].date()
                    numitems = numitems + 1
                    indexage = (nowtime - dateindexed).days
                    totalage += indexage
                averageage = totalage / numitems
                if sdate:
                    minage = (nowtime - sdate.date()).days
                    if averageage < minage:
                        continue
                msgs3.append(u'Average index age is {0} days for language {1}'.format(averageage, language))
            if options['oldest']:
                items = index_model.objects.order_by('date_indexed')[0:1]
                for item in items:
                    msgs1.append(u'{0} oldest index is on {1} for keyword {2} with {3} results'.format(language, item.date_indexed, item.keywords, item.num_results))
            if options['showurls']:
                items = site_model.objects.order_by('lastcrawled')[0:1]
                for item in items:
                    try:
                        di = DomainInfo.objects.get(url=item.rooturl)
                        msgs1.append(u'{0} oldest url is on {1} for url id {2} (Lang {3} I{4} Q{5} L{6}) - {7}'.format(language, item.lastcrawled, 
                            item.id, di.language_association, di.uses_language_subdirs, di.uses_language_query_parameter, di.uses_langid, item.url))
                    except ObjectDoesNotExist:
                        msgs1.append(u'{0} oldest url is on {1} for url id {2} - {3}'.format(language, item.lastcrawled, item.id, item.url))
            if sdate:
                if not options['showurls']:
                    num_items = index_model.objects.filter(date_indexed__lt=sdate).count()
                    total_items += num_items
                    if num_items > 0 or showempty:
                        msgs2.append(u'{0} has {1} indexes before {2}'.format(language, num_items, sdate))
                else:
                    num_items = site_model.objects.filter(lastcrawled__lt=sdate).count()
                    total_items += num_items
                    if num_items > 0 or showempty:
                        msgs2.append(u'{0} has {1} pages last crawled before {2}'.format(language, num_items, sdate))
        # Do this so things are grouped.
        for message in msgs1:
            print message
        for message in msgs2:
            print message
        for message in msgs3:
            print message
        if sdate:
            print u'{0} old indexes total.'.format(total_items)
