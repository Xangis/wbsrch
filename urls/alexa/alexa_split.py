# -*- coding: utf-8 -*-

# This file should be run in a directory full of alexa top 1 million zip files.
# It will extract all of the domains from them and concatenate them into a single
# large text file with one domain per line.
#
# After that, you can run this shell command to get unique domains:
# time cat domains.txt|sort|uniq > domains_unique.txt
#
# This will take about 12 seconds to generate from 4 million domains on a fast system
# and the domains_unique output file will be a list of unique domain names.
#
# wc domains_unique.txt will tell you the total number of different domains.

import os
import csv
import zipfile

domains = []


def ProcessCSVFile(filename):
    num_domains = 0
    print('Opening {0}'.format(filename))
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # Set all Alexa results as old.
        for row in reader:
            if len(row) >= 2:
                # This makes things get progressively slower to add domains.
                # if(row[0] not in domains):
                domains.append(row[1])
                num_domains = num_domains + 1
                if num_domains % 100000 == 0:
                    print('Processed {0}'.format(num_domains))
    with open('domains.txt', 'w') as outfile:
        for item in domains:
            outfile.write('{0}\n'.format(item))
        outfile.close()
    print('Processed {0} more domains in {1}, {2} were new.'.format(num_domains, filename, len(domains)))


def UnzipFile(file):
    zip_ref = zipfile.ZipFile(file, 'r')
    zip_ref.extractall('.')
    zip_ref.close()


for file in os.listdir('.'):
    if file.endswith('.zip'):
        print(file)
        UnzipFile(file)
        ProcessCSVFile('top-1m.csv')
