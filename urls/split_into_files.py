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

import codecs


def SplitDomains(filename):
    processed = 0
    domain_files = {}
    f = open(filename, 'rb')
    reader = codecs.getreader('utf8')(f)
    for line in reader:
        line = line.strip()
        pieces = line.split('.')
        suffix = pieces[-1]
        if suffix not in domain_files:
            domain_files[suffix] = open('{0}.txt'.format(suffix), 'w')
        domain_files[suffix].write('{0}\n'.format(line))
        processed = processed + 1
    for item in domain_files.keys():
        domain_files[item].close()
    print('Processed {0} domains.'.format(processed))


SplitDomains('_all.txt')
# SplitDomains('_all.txt')
# SplitDomains('top-1m.csv')
# SplitDomains('top500.domains.03.16.csv')
