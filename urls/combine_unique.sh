#!/bin/bash
for filename in /var/django/wbsrch/urls/domainsindex/*_new; do
    echo $filename
    shortfile=$(basename $filename)
    #echo $shortfile
    basefile="${shortfile%.*}"
    otherfile="/var/django/wbsrch/urls/commoncrawl/$basefile.txt"
    echo $otherfile
    cat  $filename $otherfile | sort|uniq > $basefile.uniq
done
