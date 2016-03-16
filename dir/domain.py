import dateutil.parser
import datetime
import whois

def GetDomainAge(domain):
    """
    Gets the creation and expiration date for a domain as a tuple.
    """
    try:
        info = whois.whois(domain)
    except whois.parser.PywhoisError, e:
        print 'PywhoisError (setting creation and expiration to None): {0}'.format(e)
        return (None, None)
    try:
        print 'Domain {0} Creation Date {1}, Expiration Date: {2}'.format(domain, info.creation_date, info.expiration_date)
    except:
        print 'Something failed.'
        return (None, None)
    try:
        if isinstance(info.expiration_date, list):
            expiration_date = info.expiration_date[0]
        else:
            expiration_date = info.expiration_date
    except:
        print 'GetDomainAge: Cannot get expiration date. Returned ""'.format(info.expiration_date)
        expiration_date = None
    try:
        if isinstance(info.creation_date, list):
            creation_date = info.creation_date[0]
        else:
            creation_date = info.creation_date
    except:
        print 'GetDomainAge: Cannot get creation date. Returned ""'.format(info.creation_date)
        creation_date = None
    if creation_date and not isinstance(creation_date, datetime.datetime):
        creation_date = dateutil.parser.parse(creation_date)
    if expiration_date and not isinstance(expiration_date, datetime.datetime):
        expiration_date = dateutil.parser.parse(expiration_date)
    print 'Domain "{0}" Created: {1}, Expires: {2}'.format(domain, creation_date, expiration_date)
    return (creation_date, expiration_date)

def GetDomainInfo(domain):
    """
    Gets the full set of data for a domain.
    """
    try:
        info = whois.whois(domain)
        return info
    except whois.parser.PywhoisError, e:
        print 'PywhoisError (setting creation and expiration to None): {0}'.format(e)
        return None
