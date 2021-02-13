# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from dir.models import BlockedSite
from dir.utils import RemoveURLsForDomain


def TrimDomain(domain):
    """
    Rough and dirty method to clean leading HTTP and trailing slash from a domain name.
    """
    domain = domain.strip()
    if domain.endswith('/'):
        domain = domain[0:-1]
    if domain.startswith('http://'):
        domain = domain[7:]
    if domain.startswith('https://'):
        domain = domain[8:]
    return domain


class Command(BaseCommand):
    help = """
    Checks all of the sites with the specified extension to see whether they should be moved to the target language.
    Unlike the admin command, this is domain-language-aware, so pages from domains tagged as a specific language or
    as an infix or url parameter language will only be moved if they fit those rules.
    """
    def add_arguments(self, parser):
        parser.add_argument('-s', '--site', action='store', dest='site', help='Site to block.'),
        parser.add_argument('-r', '--reason', default=8, action='store', type=int, dest='reason', help='Reason (4=porn, 5=pills, 8=unindexed language, 20=arabic, 21=chinese, 25=japanese, 28=russian)'),

    def handle(self, *args, **options):
        site = options.get('site')
        site = TrimDomain(site)
        reason = int(options.get('reason'))
        print('Blocking {0} for reason {1}'.format(site, reason))
        try:
            BlockedSite.objects.get(url=site)
            # If the domain is already blocked, the URL must have been added erroneously.
            # in that case, just delete it.
            RemoveURLsForDomain(site)
        except ObjectDoesNotExist:
            bsite = BlockedSite()
            bsite.url = site
            bsite.reason = reason
            bsite.save()
