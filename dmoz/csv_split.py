# -*- coding: utf-8 -*-

# Script to split CSV files into URL list, assuming URL in first line of file.

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

for file in ('cs.csv', 'da.csv', 'de.csv', 'el.csv', 'en.csv', 'es.csv', 'fi.csv', 'fr.csv', 'hu.csv', 'it.csv', 'nl.csv', 'no.csv', 'pl.csv', 'pt.csv', 'sv.csv', 'tr.csv'):
    ProcessCSVFile(file)
