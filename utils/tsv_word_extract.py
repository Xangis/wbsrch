# -*- coding: utf-8 -*-

# Script to split CSV files into URL list, assuming URL in first line of file.
#
# This should be run after split.sh if processing DMOZ urls.

import csv
import argparse


parser = argparse.ArgumentParser(description="Load a file containing a tsv of words or indexterms one per line and print those words.")
parser.add_argument('input', action='store', type=str, help='Input filename.')
parser.add_argument('column', default=2, action='store', type=int, help='Column number to check. Default=2.')
options = parser.parse_args()


def ProcessCSVFile(filename):
    column = options['column']
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            if len(row) >= column:
                print(row[column-1])


ProcessCSVFile(options['input'])
