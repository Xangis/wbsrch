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


nameserver_list = ['ns1', 'ns2', 'ns3', 'ns4', 'ns5', 'ns6', 'ns7', 'ns8', 'ns9', 'ns01', 'ns02', 'ns03', 'ns04', 'ns05', 'ns06', 'ns07', 'ns08', 'ns09',
                   'ns10', 'ns11', 'ns12', 'ns13', 'ns14', 'ns15', 'ns16', 'ns17', 'ns18', 'ns19',
                   'ns20', 'ns21', 'ns22', 'ns23', 'ns24', 'ns25', 'ns26', 'ns27', 'ns28', 'ns29',
                   'ns30', 'ns31', 'ns32', 'ns33', 'ns34', 'ns35', 'ns36', 'ns37', 'ns38', 'ns39',
                   'ns40', 'ns41', 'ns42', 'ns43', 'ns44', 'ns45', 'ns46', 'ns47', 'ns48', 'ns49',
                   'ns50', 'ns51', 'ns52', 'ns53', 'ns54', 'ns55', 'ns56', 'ns57', 'ns58', 'ns59']


def ProcessDomains(filename):
    processed = 0
    domains = set()
    f = open("{0}/{1}".format(options.directory, filename), 'rb')
    reader = codecs.getreader('utf8')(f)
    filenumber = 0

    for line in reader:
        line = line.strip()
        pieces = line.split('\t')
        domain = (pieces[0])[0:-1]
        # Skip the domain root.
        if '.' not in domain:
            continue
        if domain.startswith('ns.'):
            continue
        if domain.startswith('mail.'):
            pieces = domain.split('.')
            if len(pieces) > 2:
                continue
        if domain.startswith('ns'):
            pieces = domain.split('.')
            if len(pieces) > 2:
                if pieces[0] in nameserver_list:
                    continue
        if domain not in domains:
            # print('Domain: {0}'.format(domain))
            domains.add(domain)
            processed += 1
        if(processed % 1000000) == 0:
            print('Writing 1 million domains to out/{0}{1}.txt'.format(filename, filenumber))
            with open('out/{0}{1}.txt'.format(filename, filenumber), 'w') as f:
                for item in domains:
                    f.write("{0}\n".format(item))
            filenumber += 1
            domains = set()
    with open('out/{0}{1}.txt'.format(filename, filenumber), 'w') as f:
        for item in domains:
            f.write("{0}\n".format(item))
    return processed


for filename in os.listdir(options.directory):
    if filename.endswith('.txt'):
        count = ProcessDomains(filename)
        print('{0} contains {1} domains'.format(filename, count))
