
from multiprocessing import Pool
import os
import argparse
import subprocess


parser = argparse.ArgumentParser(description="Load a file containing one domain per line and count the number of domains with each extension.")
parser.add_argument('directory', action='store', type=str, help='Input directory.')
parser.add_argument('-p', '--processes', default=8, action='store', type=int, dest='processes', help='Number of concurrent processes for crawling (default=4).')
options = parser.parse_args()


def ProcessFile(filename):
    fullpath = '{0}/{1}'.format(options.directory, filename)
    num_lines = sum(1 for line in open(fullpath))
    print('Crawling {0} with {1} domains.'.format(filename, num_lines))
    subprocess.call(['python', 'manage.py', 'crawl', '-f', fullpath, '-m', str(num_lines), '-s', '0'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.call(['mv', fullpath, fullpath + '_'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print('Done crawling {0} with {1} lines.'.format(filename, num_lines))


if __name__ == '__main__':
    files = []
    for filename in os.listdir(options.directory):
        if filename.endswith('.txt'):
            files.append(filename)
    with Pool(options.processes) as p:
        p.map(ProcessFile, files)
