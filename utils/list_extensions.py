# Takes the output of count_extensions and prints extensions one per line.
import codecs
import argparse


parser = argparse.ArgumentParser(description="Load a file containing one domain per line and count the number of domains with each extension.")
parser.add_argument('input', action='store', type=str, help='Input filename.')
options = parser.parse_args()


def GetExtension(line):
    if not line:
        return None
    pieces = line.split(':')
    return pieces[0].strip()


extensions = []
filename = options.input
f = open(filename, 'rb')
reader = codecs.getreader('utf8')(f)
for line in reader.readlines():
    ext = GetExtension(line)
    if ext:
        print(ext)
    extensions.append(ext)
print(extensions)
