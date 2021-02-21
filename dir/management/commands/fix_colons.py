
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from dir.models import language_list
from dir.utils import GetSiteInfoModelFromLanguage


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
            site_model = GetSiteInfoModelFromLanguage(language)
            print('Processing {0}'.format(language))
            infos = site_model.objects.filter(rooturl__icontains=':')
            count = 0
            for info in infos:
                root = info.rooturl.split(':')[0]
                print('Changing {0} to {1}'.format(info.rooturl, root))
                info.rooturl = root
                info.save()
                count += 1
            print('{0} root urls fixed in {1}'.format(count, language))


