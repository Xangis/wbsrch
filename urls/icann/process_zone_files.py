# -*- coding: utf-8 -*-
#
# Takes a folder containing ICANN zone files and processes them into
# separate files in the out/ directory containing one domain per line.
#
# Requires a LOT of RAM because the .com zone file is ~22GB.
import codecs
import argparse
import os

parser = argparse.ArgumentParser(description="Load a file containing one domain per line and count the number of domains with each extension.")
parser.add_argument('directory', action='store', type=str, help='Input directory.')
options = parser.parse_args()


def ProcessDomains(filename):
    processed = 0
    domains = set()
    f = open("{0}/{1}".format(options.directory, filename), 'rb')
    reader = codecs.getreader('utf8')(f)

    for line in reader.readlines():
        line = line.strip()
        pieces = line.split('\t')
        domain = (pieces[0])[0:-1]
        # Skip the domain root.
        if '.' not in domain:
            continue
        if domain not in domains:
            #print('Domain: {0}'.format(domain))
            domains.add(domain)
            processed += 1
    with open('out/{0}'.format(filename), 'w') as f:
        for item in domains:
            f.write("{0}\n".format(item))
    return processed


for filename in os.listdir(options.directory):
    if filename.endswith('.txt'):
        count = ProcessDomains(filename)
        print('{0} contains {1} domains'.format(filename, count))
