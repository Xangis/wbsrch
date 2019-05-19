# -*- coding: utf-8 -*-

# Script to split CSV files into URL list, assuming URL in first line of file.
#
# This should be run after split.sh if processing DMOZ urls.

import os
import sys
import csv

def ProcessCSVFile(filename):
    num_domains = 0
    domains = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        lines = 0
        for row in reader:
            lines = lines + 1
            if len(row) >= 2:
                dom = row[1]
                if dom != 'Hidden profile' and dom != 'Site':
                    domains.append(row[1])
                    num_domains = num_domains + 1
    with open(filename + '.txt', 'w') as outfile:
        for item in domains:
            outfile.write('{0}\n'.format(item))
        outfile.close()
    print('Processed {0} lines and found {1} domains in {2}.'.format(lines, num_domains, filename))

for file in ('Quantcast-Top-Million.txt',):
    ProcessCSVFile(file)
