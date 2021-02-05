# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from dir.models import DomainInfo, language_list, SiteInfo
from dir.utils import MoveSiteTo


class Command(BaseCommand):
    help = """
    This command enforces language associations on all URLs in the database.

    Domains with a language tag could have made it into the main site_info table
    from a sync_crawls import or some other way. The puts things where they belong.
    """
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
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
