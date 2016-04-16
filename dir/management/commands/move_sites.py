# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from optparse import make_option
from dir.models import SiteInfo, DomainInfo
from dir.utils import MoveSiteTo
import dateutil.parser

class Command(BaseCommand):
    help = """
    Checks all of the sites with the specified extension to see whether they should be moved to the target language.
    Unlike the admin command, this is domain-language-aware, so pages from domains tagged as a specific language or 
    as an infix or url parameter language will only be moved if they fit those rules.
    """
    option_list = BaseCommand.option_list + (
        make_option('-e', '--extension', action='store', dest='extension', help='Check domains with this extension.'),
        make_option('-l', '--language', action='store', dest='language', help='Move domain pages to this language.'),
        make_option('-m', '--max', default=10, action='store', type='int', dest='max', help='Max number of domains to process. (default=10)'),
        make_option('-n', '--domaininfo', default=True, action='store_false', dest='domaininfo', help='Do not create DomainInfo records for domains that lack them. (default=Yes)'),
    )

    def handle(self, *args, **options):
        extension = options.get('extension', None)
        lang = options.get('language', None)
        createinfo = options.get('domaininfo', True)
        max = options.get('max', None)
        if not lang:
            raise ValueError('Target language must be provided')
        if not extension:
            raise ValueError('Extension is required.')
        items = SiteInfo.objects.filter(rooturl__endswith=extension).values('rooturl').distinct().order_by('rooturl')
        print u'Num domains to check: {0}'.format(items.count())
        processed = 0
        pagesmoved = 0
        domainsmoved = 0
        for item in items:
            processed = processed + 1
            if max and (processed > max):
                break
            try:
                di = DomainInfo.objects.get(url = item['rooturl'])
                if di.language_association and (di.language_association != lang):
                    continue
                elif di.language_association or di.uses_language_subdirs or di.uses_langid:
                    print 'Domain {0} uses a language categorization scheme but we do not handle those yet. Skipping.'.format(item['rooturl'])
                    continue
            except ObjectDoesNotExist:
                if createinfo:
                    di = DomainInfo()
                    di.url = item['rooturl']
                    print u'Added domain entry for {0}'.format(di.url)
                    di.save()
            pages = SiteInfo.objects.filter(rooturl=item['rooturl'])
            domainpages = 0
            for page in pages:
                MoveSiteTo(page, lang, True)
                pagesmoved = pagesmoved + 1
                domainpages = domainpages + 1
            print u'Moved {0} pages for {1} to {2}'.format(domainpages, item['rooturl'], lang)
            domainsmoved = domainsmoved + 1
        print u'Processed {0} domains and moved {1} domains totaling {2} pages to {3}'.format(processed, domainsmoved, pagesmoved, lang)
