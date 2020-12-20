# -*- coding: utf-8 -*-
import codecs
from subprocess import call

# This script launches every line of a file as a browser tab, except lines that begin with ---.

f = open("urls.txt", 'rb')
reader = codecs.getreader('utf8')(f)
count = 0
for line in reader.readlines():
    line = line.strip().lower()
    if line and not line.startswith('--'):
        if not line.startswith('http'):
            line = line.split(' ')[1]
        call(['firefox', line])
        count = count + 1
