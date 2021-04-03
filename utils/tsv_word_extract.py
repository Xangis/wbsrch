# -*- coding: utf-8 -*-

# Script to split CSV files into URL list, assuming URL in first line of file.
#
# This should be run after split.sh if processing DMOZ urls.

import csv
import argparse


parser = argparse.ArgumentParser(description="Load a file containing a tsv of words or indexterms one per line and print those words.")
parser.add_argument('input', action='store', type=str, help='Input filename.')
parser.add_argument('-c', '--column', default=2, dest='column', action='store', type=int, help='Column number to check. Default=2.')
options = parser.parse_args()


def ProcessCSVFile(filename):
    column = options.column
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar=None)
        for row in reader:
            if len(row) >= column:
                word = row[column - 1].strip()
                if len(word) < 2:
                    continue
                if ':' in word:
                    continue
                if '(' in word:
                    continue
                if ']' in word:
                    continue
                if ')' in word:
                    continue
                if '[' in word:
                    continue
                if '«' in word:
                    continue
                if '»' in word:
                    continue
                if '…' in word:
                    continue
                if '‘' in word:
                    continue
                if '.' in word:
                    continue
                if ',' in word:
                    continue
                if '–' in word:
                    continue
                if '”' in word:
                    continue
                if '†' in word:
                    continue
                if '•' in word:
                    continue
                if '·' in word:
                    continue
                if '‹' in word:
                    continue
                if '›' in word:
                    continue
                if '₤' in word:
                    continue
                if '⁰' in word:
                    continue
                if '™' in word:
                    continue
                if '″' in word:
                    continue
                if '‶' in word:
                    continue
                if '≈' in word:
                    continue
                if 'ℓ' in word:
                    continue
                if '≥' in word:
                    continue
                if '¡' in word:
                    continue
                if '¿' in word:
                    continue
                if '°' in word:
                    continue
                if 'µ' in word:
                    continue
                print(word)


ProcessCSVFile(options.input)
