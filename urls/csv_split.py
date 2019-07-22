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
        reader = csv.reader(csvfile, delimiter=',')
        # Set all Alexa results as old.
        for row in reader:
            if len(row) >= 2:
                domains.append(row[0])
                num_domains = num_domains + 1
    with open(filename + '.txt', 'w') as outfile:
        for item in domains:
            outfile.write('{0}\n'.format(item))
        outfile.close()
    print('Processed {0} domains in {1}.'.format(num_domains, filename))

for file in ('aero.csv', 'biz.csv', 'com.csv', 'edu.csv', 'info.csv', 'jobs.csv', 'mil.csv', 'name.csv', 'org.csv', 'tel.csv', 'xxx.csv',
             'asia.csv', 'cat.csv', 'coop.csv', 'gov.csv', 'int.csv', 'mobi.csv', 'net.csv', 'pro.csv', 'travel.csv'):
    ProcessCSVFile(file)
