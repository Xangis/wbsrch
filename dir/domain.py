from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core import serializers
from django.db.utils import DataError
from pytz import AmbiguousTimeError
from pytz.exceptions import NonExistentTimeError
import dateutil.parser
import datetime
import whois
from socket import gaierror, timeout

BAD_DATE_STRINGS = ('b', ':', 'N', 'None', '0', '2', 'B')

# Accepts a DomainInfo object and updates its whois information.
def UpdateDomainWhois(domain, detailed=False):
    print('Updating {0}'.format(domain.url))
    info = GetDomainInfo(domain.url)
    if info:
        if detailed:
            print('Domain Info: {0}'.format(info))
        try:
            domain.domain_created = info['creation_date'][0]
        except TypeError:
            domain.domain_created = info['creation_date']
        except KeyError:
            pass
        if domain.domain_created in BAD_DATE_STRINGS:
            print('Invalid domain_created date "{0}". Resetting to None'.format(domain.domain_created))
            domain.domain_created = None
        try:
            domain.domain_expires = info['expiration_date'][0]
        except TypeError:
            domain.domain_expires = info['expiration_date']
        except KeyError:
            pass
        if domain.domain_expires in BAD_DATE_STRINGS:
            print('Invalid domain_expires date "{0}". Resetting to None'.format(domain.domain_expires))
            domain.domain_expires = None
        try:
            domain.domain_updated = info['updated_date'][0]
        except TypeError:
            pass
        except KeyError:
            pass
        if domain.domain_updated in BAD_DATE_STRINGS:
            print('Invalid domain_updated date "{0}". Resetting to None'.format(domain.domain_updated))
            domain.domain_updated = None
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
    else:
        print('Could not get whois info for {0}'.format(domain.url))
    domain.whois_last_updated = timezone.now()
    if detailed:
        print('Created: {0}, Expires: {1}, Update Date: {2}, Name: {3}, City: {4}, Country: {5}, State: {6}, Address: {7}, Org: {8}, Registrar: {9}, Zipcode: {10}, Nameservers: {11}, EMails: {12}'.format(
            domain.domain_created, domain.domain_expires, domain.domain_updated, domain.whois_name, domain.whois_city, domain.whois_country, domain.whois_state, domain.whois_address, domain.whois_org, domain.whois_registrar, domain.whois_zipcode, domain.whois_nameservers, domain.whois_emails))
    try:
        domain.save()
    except DataError as e:
        print('DataError: Failed to get domain info for {0}: {1}'.format(domain.url, e))
        print(serializers.serialize("json", [domain, ], indent=4))
    except AmbiguousTimeError as e:
        print('AmbiguousTimeError: Failed to get domain info for {0}: {1}'.format(domain.url, e))
        print(serializers.serialize("json", [domain, ], indent=4))
    except ValidationError as e:
        print('ValidationError: Failed to get domain info for {0}: {1}'.format(domain.url, e))
        try:
            print(serializers.serialize("json", [domain, ], indent=4))
        except ValueError:
            print('domain_created: "{0}"'.format(domain.domain_created))
            print('domain_expires: "{0}"'.format(domain.domain_expires))
            print('domain_updated: "{0}"'.format(domain.domain_updated))
        except AttributeError:
            print('domain_created: "{0}"'.format(domain.domain_created))
            print('domain_expires: "{0}"'.format(domain.domain_expires))
            print('domain_updated: "{0}"'.format(domain.domain_updated))
    except NonExistentTimeError:
        domain.domain_created = None
        domain.domain_expires = None
        domain.domain_updated = None
        domain.save()

def GetDomainAge(domain):
    """
    Gets the creation and expiration date for a domain as a tuple.
    """
    try:
        info = whois.whois(domain)
    except whois.parser.PywhoisError as e:
        print('PywhoisError (setting creation and expiration to None): {0}'.format(e))
        return (None, None)
    try:
        print('Domain {0} Creation Date {1}, Expiration Date: {2}'.format(domain, info.creation_date, info.expiration_date))
    except Exception:
        print('Something failed.')
        return (None, None)
    try:
        if isinstance(info.expiration_date, list):
            expiration_date = info.expiration_date[0]
        else:
            expiration_date = info.expiration_date
    except Exception:
        print('GetDomainAge: Cannot get expiration date. Returned "{0}"'.format(info.expiration_date))
        expiration_date = None
    try:
        if isinstance(info.creation_date, list):
            creation_date = info.creation_date[0]
        else:
            creation_date = info.creation_date
    except Exception:
        print('GetDomainAge: Cannot get creation date. Returned "{0}"'.format(info.creation_date))
        creation_date = None
    if creation_date and not isinstance(creation_date, datetime.datetime):
        creation_date = dateutil.parser.parse(creation_date)
    if expiration_date and not isinstance(expiration_date, datetime.datetime):
        expiration_date = dateutil.parser.parse(expiration_date)
    print('Domain "{0}" Created: {1}, Expires: {2}'.format(domain, creation_date, expiration_date))
    return (creation_date, expiration_date)

def GetDomainInfo(domain):
    """
    Gets the full set of data for a domain.
    """
    try:
        info = whois.whois(domain)
        return info
    except whois.parser.PywhoisError as e:
        try:
            print('PywhoisError (setting creation and expiration to None): {0}'.format(e))
        except Exception:
            print('PywhoisError (setting creation and expiration to None): {0}'.format(domain))
        return None
    except gaierror:
        print('Could not look up domain {0}: socket.gaierror'.format(domain))
        return None
    except timeout:
        print('Could not look up domain {0}: socket.timeout'.format(domain))
        return None
    except Exception as e:
        print('Unspecified error in GetDomainInfo for {0}: {1}'.format(domain, e))
        return None
