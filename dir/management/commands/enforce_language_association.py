# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from dir.models import DomainInfo, language_list, SiteInfo
from dir.utils import MoveSiteTo, GetSiteInfoModelFromLanguage


class Command(BaseCommand):
    help = """
    This command enforces language associations on all URLs in the database.

    Domains with a language tag could have made it into the main site_info table
    from a sync_crawls import or some other way. The puts things where they belong.
    """

    def add_arguments(self, parser):
        parser.add_argument('-c', '--cleanup', default=False, action='store_true', dest='cleanup', help='Delete all non-English pages from language indexes if they are not tagged that language.')

    def handle(self, *args, **options):
        if options['cleanup']:
            loglines = []
            for language in language_list:
                if language == 'en':
                    continue
                deleted = 0
                bad_domains = 0
                good_domains = 0
                print('Processing language {0}'.format(language))
                site_model = GetSiteInfoModelFromLanguage(language)
                domains_to_check = site_model.objects.values_list('rooturl', flat=True).distinct().order_by('rooturl')
                for domain in domains_to_check:
                    info = DomainInfo.objects.filter(url=domain).first()
                    if not info or info.language_association != language:
                        print('{0} is not {1}. Deleting.'.format(domain, language))
                        count = site_model.objects.filter(rooturl=domain).count()
                        print('Deleting {0} pages.'.format(count))
                        deleted += count
                        bad_domains += 1
                        site_model.objects.filter(rooturl=domain).delete()
                    else:
                        print('{0} is good.'.format(domain))
                        good_domains += 1
                logline = '{0}: {1} domains were good and {2} were not. {3} pages were deleted.'.format(language, good_domains, bad_domains, deleted)
                loglines.append(logline)
                print(logline)
            for line in loglines:
                print(line)
            return
        domain_data = DomainInfo.objects.filter(language_association__in=language_list).exclude(language_association='en').order_by('url').values('url', 'language_association')
        print('Need to process {0} domains.'.format(len(domain_data)))
        count = 0
        pages_moved = 0
        for domain in domain_data:
            # print(domain)
            # {'url': '0000000000000.de', 'language_association': 'de'}
            pages = SiteInfo.objects.filter(rooturl=domain['url'])
            found = pages.count()
            if found:
                print('Need to move {0} pages to {1} for {2}'.format(found, domain['language_association'], domain['url']))
                for page in pages:
                    MoveSiteTo(page, domain['language_association'])
                    pages_moved += 1
            count += 1
            if count % 10000 == 0:
                print('Processed {0} domains.'.format(count))
        print('Processed {0} domains and moved {1} pages.'.format(count, pages_moved))
