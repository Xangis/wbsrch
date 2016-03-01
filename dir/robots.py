from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from dir.models import Setting
import robotparser
import urllib2
import httplib
import socket
import cgi
import robotexclusionrulesparser

def GetIPAddress(url, descriptive=False):
    try:
        ip = socket.gethostbyname(url)
        if descriptive:
            print u'IP address is: {0}'.format(ip)
        return ip
    except:
        if descriptive:
            print u'IP address not found.'

def AllowedByRobots(url, domaininfo, use_google_agent=True):
    """
    Checks whether the URL is allowed by a domain's existing robots.txt file.

    Does not retrieve the robots.txt file. Only uses rules from the domain info. If
    no robots data is present, then it's allowed.
    """
    rerp = robotexclusionrulesparser.RobotExclusionRulesParser()
    if not domaininfo.robots_txt:
        return True
    rerp.parse(domaininfo.robots_txt)
    if use_google_agent:
        return rerp.is_allowed('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', url)
    else:
        return rerp.is_allowed('*', url)
        #return rerp.is_allowed('Mozilla/5.0 (compatible; WbSrch/1.1; +https://wbsrch.com)', url):

def CheckUrlAgainstRobotsFile(url):
    """
    Retrieves robots.txt file for URL and returns a boolean stating whether crawling the URL is allowed.

    Always retrieves the file. 
    """
    # TODO: Query the domain info first. If that doesn't have a robots.txt file, or if it's more than X out of
    # date, update it.
    #
    # Or just don't bother updating the robots.txt for a domain if it doesn't exist -- we will have a daemon
    # for that.
    rp = robotparser.RobotFileParser()
    rooturl = GetRootUrl(url)
    rp.set_url(rooturl + '/robots.txt')
    allowed = rp.is_allowed('*', url)
    print 'URL "{0}" allowed by robots: {1}'.format(url, allowed)
    return allowed

def GetRobotsFile(domain, descriptive=False, save_failures=False):
    """
    Gets the robots.txt file for a domain, updates it in the domain, and updates the last robots.txt date.

    Takes a DomainInfo object as a parameter.

    Returns True if successful, false if not.
    """
    # TODO: Get the robots.txt file for a domain and store it.
    url = u'http://{0}/robots.txt'.format(domain.url)
    print u'GetRobotsFile: {0}'.format(url)
    req = urllib2.Request(url)

    try:
        user_agent = Setting.objects.get(name='wbsrch_user_agent')
        req.add_header('User-agent', user_agent.value)
    except ObjectDoesNotExist:
        req.add_header('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/34.0')

    try:
        response = urllib2.urlopen(req, timeout=20)
        realurl = response.geturl()
        if realurl != url:
            if descriptive:
                try:
                    print 'Robots request file for {0} returned {1}'.format(url, realurl)
                except:
                    pass
            if realurl[7:] == url [8:] or realurl[8:] == url[7:]:
                if descriptive:
                    print 'ITS ONLY AN HTTP => HTTPS REDIRECT, WE ARE OK'
            else:
                print u'Request returned different URL: {0}, marking as no robots.txt'.format(realurl)
                # We cannot set the IP here because we didn't get the server we asked for.
                domain.robots_txt = ''
                domain.robots_last_updated = timezone.now()
                domain.save()
                return False
        _, params = cgi.parse_header(response.headers.get('Content-Type', ''))
        encoding = params.get('charset', 'utf-8')
        try:
            text = response.read().decode(encoding)
        except LookupError:
            text = response.read().strip()
        if text.startswith('<html') or text.startswith('<HTML') or text.startswith('<!DOCTYPE') or text.startswith('<doctype') or text.startswith('<head') or text.startswith('<!doctype') or text.startswith('<script') or text.startswith('<?php') or text.startswith('<br />') or text.startswith('<head') or text.startswith('<h1'):
            print u'Request returned HTML, marking as no robots.txt'
            domain.robots_ip = GetIPAddress(domain.url, descriptive)
            domain.robots_txt = ''
            domain.robots_last_updated = timezone.now()
            domain.save()
        try:
            if descriptive:
                print u'Robots Response: {0}'.format(text)
        except:
            pass
        if response:
            domain.robots_ip = GetIPAddress(domain.url, descriptive)
            domain.robots_txt = text
            domain.robots_last_updated = timezone.now()
            domain.save()
        return True
    except UnicodeDecodeError:
        print u'Content Decoding Problem, marked as no robots.txt'
        # We got content, it was just bad. So we can set the IP
        domain.robots_ip = GetIPAddress(domain.url, descriptive)
        domain.robots_txt = ''
        domain.robots_last_updated = timezone.now()
        domain.save()
        return False
    except socket.error, e:
        print u'Socket Error: {0}'.format(e)
        return False
    except httplib.BadStatusLine, e:
        print u'httplib.BadStatusLine Error: {0}'.format(e)
        return False
    except httplib.IncompleteRead, e:
        print u'httplib.IncompleteRead read crawling URL: {0} - {1}'.format(url,e)
        return False
    # This needs to be before URLError due to subclassing.
    except urllib2.HTTPError, e:
        print u'Error Code: {0}'.format(e.code)
        if e.code == 404 or e.code == 403 or e.code == 410 or e.code == 500:
            # We got the server, it just didn't have the file we wanted, so we should be able to get the IP.
            # but response is empty. Balls.
            domain.robots_ip = GetIPAddress(domain.url, descriptive)
            print e
            print u'Domain marked as no robots.txt'
            domain.robots_txt = ''
            domain.robots_last_updated = timezone.now()
            domain.save()
        return False
    except urllib2.URLError, e:
        print u'URL Error: {0}'.format(e)
        if isinstance(e.args, (tuple,)):
            print u'Error: {0} [{1}]]'.format(e.args[0], type(e.args[0])) + u']'
            if isinstance(e.args[0], (socket.timeout,)):
                print u'Timed out retrieving URL: ' + url
            elif isinstance(e.args[0], (socket.gaierror,)):
                print u'This is a socket.gaierror - Error: ' + unicode(e.args[0].errno) + u', Message: ' + e.args[0].strerror
                # A DNS lookup failure means we should remove it from the database.
                print 'Domain lookup failed.'
                if save_failures:
                    if e.args[0].errno == -2 or e.args[0].errno == -5 or e.args[0].errno == -8:
                        # We cannot set the IP here because we didn't get one.
                        print 'Domain lookup failed, marking as no robots.txt.'
                        domain.robots_txt = ''
                        domain.robots_last_updated = timezone.now()
                        domain.save()
                    else:
                        print 'Domain lookup failed, error number is {0}, NOT marking as no robots.txt.'.format(e.args[0].errno)
        return False
