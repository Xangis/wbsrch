# -*- coding: utf-8 -*-

# This file will split a list of domains into individual text files with extensions
# based on the domain extensions.
#
# This has been tested on the Moz top 500, the Alexa top 1 million, and the domains-index.com
# domain list.
#
# For comma-separated lines in a domain list, it assumes the domain name is in the second position
# on the line, otherwise it assumes a text file containing one domain per line. This will only list
# the root domains, so www.example.com/pages/page/ will put www.example.com in the text file.
#
# This script also does not do de-duplication or sorting. If you want to do that, you can always run
# cat <filename> | sort | uniq > <newfilename> on the Linux command line.
#
# It does not read files into memory, nor does it store large lists, and has been tested on files
# as large as 4.3 GB.
#
# Tested with Python 2.7. See the .py3 version for a Python3 variant.

import os
import sys
import codecs
from urllib.parse import urlparse

def GetRootUrl(url, secure=False):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
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
    domain_files = {}
    f = open(filename, 'rb')
    reader = codecs.getreader('utf8')(f)
    for line in reader:
        if ',' in line:
            line = line.split(',')[1]
        if line.startswith('"'):
            line = line[1:]
        root = GetRootUrl(line.strip())
        lastpart = root.split('.')[-1]
        if len(lastpart) < 2:
            print('{0} is not a valid domain extension for {1}'.format(lastpart, line))
            continue
        if lastpart not in domain_files:
            domain_files[lastpart] = open('{0}.txt'.format(lastpart), 'w')
        domain_files[lastpart].write('{0}\n'.format(root))
        processed = processed + 1
    for item in domain_files.keys():
        domain_files[item].close()
    print('Processed ' + str(processed) + ' domains.')

SplitDomains('domains.txt')
#SplitDomains('top-1m.csv')
#SplitDomains('top500.domains.03.16.csv')
