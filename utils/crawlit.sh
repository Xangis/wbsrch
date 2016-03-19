#!/bin/bash
# Run with the name of a domain file and it does the rest. Want to crawl de.csv.zip?
# ./crawl.sh de
unzip $1.csv.zip
python clean.py
words=`wc -l $1.txt | awk '{print $1}'`;
mv $1.csv.zip orig/
mv $1.csv csv/
python /var/django/wbsrch/manage.py crawl -f /home/xangis/domainlist/$1.txt -s 0 -m $words
mv $1.txt crawled/
