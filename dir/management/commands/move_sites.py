# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from optparse import make_option
from dir.models import SiteInfo, DomainInfo, SiteInfoAfterZ, BlockedSite
from dir.utils import MoveSiteTo, GetSiteInfoModelFromLanguage, RemoveURLsForDomain
import dateutil.parser

class Command(BaseCommand):
    help = """
    Checks all of the sites with the specified extension to see whether they should be moved to the target language.
    Unlike the admin command, this is domain-language-aware, so pages from domains tagged as a specific language or 
    as an infix or url parameter language will only be moved if they fit those rules.
    """
    option_list = BaseCommand.option_list + (
        make_option('-s', '--source', action='store', default='en', dest='source', help='Source language to use (default=en)'),
        make_option('-e', '--extension', action='store', dest='extension', help='Check domains with this extension.'),
        make_option('-l', '--language', action='store', dest='language', help='Move domain pages to this language.'),
        make_option('-m', '--max', default=10, action='store', type='int', dest='max', help='Max number of domains to process. (default=10)'),
        make_option('-n', '--domaininfo', default=True, action='store_false', dest='domaininfo', help='Do not create DomainInfo records for domains that lack them. (default=Yes)'),
        make_option('-b', '--block', default=False, action='store_true', dest='block', help='Do not move sites. Block after Z sites with this extension instead. (default=No)'),
    )

    def handle(self, *args, **options):
        extension = options.get('extension', None)
        sourcelang = options.get('source', 'en')
        lang = options.get('language', None)
        createinfo = options.get('domaininfo', True)
        block = options.get('block', False)
        max = options.get('max', None)
        if not lang and not block:
            raise ValueError('Target language must be provided')
        if not extension:
            raise ValueError('Extension is required.')
        if block:
            site_model = SiteInfoAfterZ
        else:
            site_model = GetSiteInfoModelFromLanguage(sourcelang)
        items = site_model.objects.filter(rooturl__endswith=extension).values('rooturl').distinct().order_by('rooturl')
        print('Num domains to check: {0}'.format(items.count()))
        processed = 0
        pagesmoved = 0
        domainsmoved = 0
        for item in items:
            processed = processed + 1
            if max and (processed > max):
                break
            if block:
                try:
                    domain = DomainInfo.objects.get(url=item['rooturl'])
                    if domain.is_unblockable:
                        continue
                except ObjectDoesNotExist:
                    # Always create domain info if the domain doesn't exist yet.
                    domain = DomainInfo()
                    domain.url = item['rooturl']
                    domain.save()
                print('Blocking {0}'.format(item['rooturl']))
                try:
                    existing = BlockedSite.objects.get(url=item['rooturl'])
                    # If the domain is already blocked, the URL must have been added erroneously.
                    # in that case, just delete it.
                    RemoveURLsForDomain(item.rooturl)
                except ObjectDoesNotExist:
                    site = BlockedSite()
                    site.url = item['rooturl']
                    site.reason = 8
                    site.save()
                    domainsmoved = domainsmoved + 1
                continue
            try:
                di = DomainInfo.objects.get(url = item['rooturl'])
                if di.uses_language_subdirs or di.uses_langid:
                    print('Domain {0} uses a language categorization scheme but we do not handle those yet. Skipping.'.format(item['rooturl']))
                    continue
                elif di.language_association and (di.language_association != lang):
                    if di.language_association != 'en' and lang != 'en':
                        # Moving one language's items to another's table
                        print('Language association changed to {0}'.format(lang))
                        di.language_association = lang
                        di.save()
                    else:
                        continue
            except ObjectDoesNotExist:
                if createinfo:
                    di = DomainInfo()
                    di.url = item['rooturl']
                    print('Added domain entry for {0}'.format(di.url))
                    di.save()
            pages = site_model.objects.filter(rooturl=item['rooturl'])
            domainpages = 0
            for page in pages:
                MoveSiteTo(page, lang, True)
                pagesmoved = pagesmoved + 1
                domainpages = domainpages + 1
            print('Moved {0} pages for {1} to {2}'.format(domainpages, item['rooturl'], lang))
            domainsmoved = domainsmoved + 1
        print('Processed {0} domains and moved {1} domains totaling {2} pages to {3}'.format(processed, domainsmoved, pagesmoved, lang))
