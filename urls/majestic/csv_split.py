# -*- coding: utf-8 -*-

# Script to split Domcop CSV file into URL list.
import csv


def ProcessCSVFile(filename):
    num_domains = 0
    domains = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # Set all Alexa results as old.
        for row in reader:
            if len(row) >= 2:
                if row[2] == 'Domain':
                    continue
                domains.append(row[2])
                num_domains = num_domains + 1
    with open(filename + '.txt', 'w') as outfile:
        for item in domains:
            outfile.write('{0}\n'.format(item))
        outfile.close()
    print('Processed {0} domains in {1}.'.format(num_domains, filename))


for file in ('majestic_million_2021-05-03.csv',):
    ProcessCSVFile(file)