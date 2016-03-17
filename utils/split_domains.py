# -*- coding: utf-8 -*-
import os
import sys
import codecs
from urlparse import urlparse

def GetRootUrl(url, secure=False):
    if not url.startswith(u'http'):
        url = u'http://' + url
    parsed_uri = urlparse( url )
    loc = parsed_uri.netloc
    loc = loc.lower()
    if loc.endswith('.'):
        loc = loc[:-1]
    if loc.endswith(':80'):
        loc = loc[:-3]
    return loc

def SplitDomains(filename):
    processed = 0
    domain_lists = {}
    f = open(filename, 'rb')
    reader = codecs.getreader('utf8')(f)
    for line in reader.readlines():
        root = GetRootUrl(line.strip())
        lastpart = root.split('.')[-1]
        if len(lastpart) < 2:
            continue
        #print 'Lastpart: {0}'.format(lastpart)
        if not domain_lists.has_key(lastpart):
            domain_lists[lastpart] = [root,]
        else:
            domain_lists[lastpart].append(root)
        processed = processed + 1
    f.close()
    for item in domain_lists.keys():
        print '{0}: {1}'.format(item, domain_lists[item])
    print 'Processed ' + str(processed) + ' domains.'

SplitDomains('domains.txt')
