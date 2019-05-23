# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from dir.models import *
from dir.utils import *
from dir.robots import GetRobotsFile
import robotexclusionrulesparser 

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-m', '--maxurls', default=100, action='store', type='int', dest='maxurls', help='Max number of URLs to check. (default=100)'),
        make_option('-j', '--justthisdomain', default=None, action='store', type='string', dest='justthisdomain', help='Only check rules for this domain.'),
        make_option('-l', '--language', default='en', action='store', type='string', dest='language', help='Language to use for page checks (default=en)'),
        make_option('-o', '--offset', default=0, action='store', type='int', dest='offset', help='Record offset for check.'),
        make_option('-d', '--detailed', default=False, action='store_true', dest='detailed', help='Print details of blocked urls.'),
        make_option('-f', '--forcerobots', default=False, action='store_true', dest='forcerobots', help='Force download of robots.txt for sites that lack it.'),
        make_option('-n', '--nuke', default=False, action='store_true', dest='nuke', help='Nuke URLs blocked from Google.'),
    )

    def handle(self, *args, **options):
        ok = 0
        blocked = 0
        gok = 0
        gblocked = 0
        wbok = 0
        wbblocked = 0
        norobots = 0
        gotrobots = 0
        max = 50000
        nuked = 0
        nuke = False
        verbose = False
        forcerobots = False
        lang = options['language']
        onlyfromdomain = options.get('justthisdomain', None)
        site_model = GetSiteInfoModelFromLanguage(lang)
        if options.has_key('maxurls'):
            max = int(options['maxurls'])
        if options['detailed']:
            verbose = True
        if options['nuke']:
            nuke = True
        if options['forcerobots']:
            forcerobots = True
        offset = 0
        if options.has_key('offset'):
            offset = int(options['offset'])
        print u'Checking robots.txt rules for urls with a max of ' + str(max) + u' and offset ' + str(offset) + u'.'
        if onlyfromdomain:
            pending = site_model.objects.filter(rooturl=onlyfromdomain)[offset:offset+max]
        else:
            pending = site_model.objects.all()[offset:offset+max]
        totalurls = pending.count()
        rerp = robotexclusionrulesparser.RobotExclusionRulesParser()
        for link in pending:
            try:
                domain = DomainInfo.objects.get(url=link.rooturl)
                if forcerobots and domain.robots_last_updated is None:
                    if verbose:
                        print 'Need to retrieve robots file for {0}'.format(link.rooturl)
                    GetRobotsFile(domain, descriptive=verbose, save_failures=True)
                    gotrobots = gotrobots + 1
                if domain.robots_last_updated is None:
                    norobots = norobots + 1
                    ok = ok + 1
                    wbok = wbok + 1
                    gok = gok + 1
                    continue
                if len(domain.robots_txt) < 1:
                    ok = ok + 1
                    wbok = wbok + 1
                    gok = gok + 1
                    continue
                rerp.parse(domain.robots_txt)
            except:
                norobots = norobots + 1
                ok = ok + 1
                wbok = wbok + 1
                gok = gok + 1
                continue
            if rerp.is_allowed('*', link.url):
                ok = ok + 1
            else:
                blocked = blocked + 1
                if verbose:
                    print u'{0} is blocked for all sites.'.format(link.url)
            if rerp.is_allowed('Mozilla/5.0 (compatible; WbSrch/1.1; +https://wbsrch.com)', link.url):
                wbok = wbok + 1
            else:
                wbblocked = wbblocked + 1
                if verbose:
                    print u'{0} is blocked for WbSrch.'.format(link.url)
            if rerp.is_allowed('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', link.url):
                gok = gok + 1
            else:
                gblocked = gblocked + 1
                if verbose:
                    print u'{0} is blocked for Google.'.format(link.url)
                if nuke:
                    print u'{0} is nuked because it is blocked for Google.'.format(link.url)
                    link.delete()
        print u'Of the existing {0} urls, {1} are blocked for all sites by robots.txt and {2} are OK. attempted to retrieve {4} robots files and {3} failed to retrieve robots.txt.'.format(
              totalurls, blocked, ok, norobots, gotrobots)
        print u'{0} are blocked for Google, {1} blocked for WbSrch, {2} are OK for Google, {3} are OK for WbSrch.'.format(gblocked, wbblocked, gok, wbok)
