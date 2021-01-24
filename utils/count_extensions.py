# This script will take a file containing domains with one per line
# and get the counts by extension.
import codecs
import argparse


parser = argparse.ArgumentParser(description="Load a file containing one domain per line and count the number of domains with each extension.")
parser.add_argument('input', action='store', type=str, help='Input filename.')
options = parser.parse_args()


def GetExtension(url):
    if not url:
        return None
    url = url.strip()
    ext = url.split('.')[-1]
    return ext


groups = {}
filename = options.input
f = open(filename, 'rb')
reader = codecs.getreader('utf8')(f)
for line in reader.readlines():
    ext = GetExtension(line)
    if ext in groups:
        groups[ext] = groups[ext] + 1
    else:
        groups[ext] = 1
dictlist = [(k, v) for k, v in groups.items()]
dictlist.sort(key=lambda x: x[1], reverse=False)
for item in dictlist:
    print('{0}: {1}'.format(item[0], item[1]))
