# -*- coding: utf-8 -*-
import os
import csv


def CleanFile(filename):
    crawl_needed = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            crawl_needed.append(row[0])
    with open("{0}.txt".format(filename[0:(len(filename) - 4)]), 'w') as outfile:
        for item in crawl_needed:
            outfile.write('%s\n' % item)
        outfile.close()
    print('{0} domains copied into {1}.txt'.format(len(crawl_needed), filename[0:(len(filename) - 4)]))


for item in os.listdir('.'):
    if os.path.isfile(item) and item.endswith('.csv'):
        CleanFile(item)
