# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core import serializers
from django.utils import timezone
from optparse import make_option
from dir.models import DomainInfo
from dir.domain import GetDomainInfo
from django.db.utils import DataError
import time

class Command(BaseCommand):
    help = "This command updates domain whois-related information such as expiration, registrar, etc."

    option_list = BaseCommand.option_list + (
        #make_option('-a', '--abbreviated', default=False, action='store_true', dest='abbreviated', help='Run in abbreviated mode, which does not scan page text.'),
        make_option('-d', '--detailed', default=False, action='store_true', dest='detailed', help='Run in verbose mode.'),
        #make_option('-p', '--pending', default=False, action='store_true', dest='pending', help='Get pending term list from database.'),
        #make_option('-l', '--language', default='en', action='store', type='string', dest='language', help='Language to use for pending indexes (default=en).'),
        #make_option('-r', '--reindex', default=False, action='store_true', dest='reindex', help='Reindex existing least-recently-indexed terms.'),
        make_option('-j', '--justthisdomain', default=None, action='store', type='string', dest='justthisdomain', help='Gets the data for a specific domain'),
        make_option('-m', '--max', default=5, action='store', type='int', dest='max', help='Max number of domains to update. (default=5)'),
        make_option('-s', '--sleep', default=15, action='store', type='int', dest='sleep', help='Time to sleep between domain queries. (default=15)'),
        make_option('-o', '--offset', default=0, action='store', type='int', dest='offset', help='Domain slice offset - distance from beginning to start. (default=0)'),
        make_option('-r', '--random', default=False, action='store_true', dest='random', help='Update un-populated domains in random order (default=no)'),
        #make_option('-f', '--file', default=None, action='store', type='string', dest='file', help='Load term list from specified file.'),

        # TODO: Make an option to fill in nulls vs update already-queried domains.
    )

    def handle(self, *args, **options):
        if options['random']:
            domains = DomainInfo.objects.filter(whois_last_updated__isnull=True).order_by('?')[options['offset']:options['offset']+options['max']]
        elif options['justthisdomain']:
            domains = DomainInfo.objects.filter(url=options['justthisdomain'])
        else:
            domains = DomainInfo.objects.filter(whois_last_updated__isnull=True).order_by('alexa_rank')[options['offset']:options['offset']+options['max']]
        detailed = options['detailed']
        for domain in domains:
            print 'Updating {0}'.format(domain.url)
            #try:
            if True:
                info = GetDomainInfo(domain.url)
                if detailed:
                    print 'Domain Info: {0}'.format(info)
                try:
                    domain.domain_created = info['creation_date'][0]
                except TypeError:
                    domain.domain_created = info['creation_date']
                except KeyError:
                    pass
                try:
                    domain.domain_expires = info['expiration_date'][0]
                except TypeError:
                    domain.domain_expires = info['expiration_date']
                except KeyError:
                    pass
                try:
                    domain.domain_updated = info['updated_date'][0]
                except TypeError:
                    pass
                except KeyError:
                    pass
                try:
                    domain.whois_name = info['name'][0:60]
                except TypeError:
                    pass
                except KeyError:
                    pass
                try:
                    domain.whois_city = info['city'][0:40]
                except TypeError:
                    pass
                except KeyError:
                    pass
                try:
                    domain.whois_country = info['country'][0:16]
                except TypeError:
                    pass
                except KeyError:
                    pass
                try:
                    domain.whois_state = info['state'][0:3]
                except TypeError:
                    pass
                except KeyError:
                    pass
                try:
                    domain.whois_address = info['address'][0:60]
                except TypeError:
                    pass
                except KeyError:
                    pass
                try:
                    domain.whois_org = info['org'][0:60]
                except TypeError:
                    pass
                except KeyError:
                    pass
                try:
                    domain.whois_registrar = info['registrar'][0:60]
                except TypeError:
                    pass
                except KeyError:
                    pass
                try:
                    domain.whois_zipcode = info['zipcode'][0:8]
                except TypeError:
                    pass
                except KeyError:
                    pass
                try:
                    domain.whois_nameservers = info['name_servers']
                except KeyError:
                    pass
                try:
                    domain.whois_emails = info['emails']
                except KeyError:
                    pass
            domain.whois_last_updated = timezone.now()
            if detailed:
                print 'Created: {0}, Expires: {1}, Update Date: {2}, Name: {3}, City: {4}, Country: {5}, State: {6}, Address: {7}, Org: {8}, Registrar: {9}, Zipcode: {10}, Nameservers: {11}, EMails: {12}'.format(
                    domain.domain_created, domain.domain_expires, domain.domain_updated, domain.whois_name, domain.whois_city, domain.whois_country, domain.whois_state, domain.whois_address, domain.whois_org, domain.whois_registrar, domain.whois_zipcode, domain.whois_nameservers, domain.whois_emails)
            try:
                domain.save()
            except DataError, e:
                print 'Failed to get domain info for {0}: {1}'.format(domain.url, e)
                print(serializers.serialize("json", [domain,], indent=4))
            # Even if the query failed, we should update the last-checked time so we don't keep re-checking bad domains.
            time.sleep(options['sleep'])
