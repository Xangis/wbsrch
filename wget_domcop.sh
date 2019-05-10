#!/bin/bash
# This retrieves the top 10 domcop URLs. It is called by a cron job, but
# can also be used manually.
/bin/mkdir -p ./urls/domcop
MYDATESTR=$(/bin/date +"%Y-%m-%d")
MYFILENAME="./urls/domcop/top10milliondomains_$MYDATESTR.csv.zip"
echo "Getting top10milliondomains.csv.zip as $MYFILENAME"
/usr/bin/wget -nv -O $MYFILENAME https://www.domcop.com/files/top/top10milliondomains.csv.zip
/bin/ls -l $MYFILENAME
