#!/bin/bash
# This retrieves the Quantcast top URLs. It is called by a cron job, but
# can also be used manually.
mkdir -p ./urls/quantcast
MYDATESTR=$(date +"%Y-%m-%d")
MYFILENAME="./urls/quantcast/quantcast-top-sites_$MYDATESTR.csv.zip"
echo "Getting quantcast-top-sites.zip as $MYFILENAME"
wget -O $MYFILENAME https://ak.quantcast.com/quantcast-top-sites.zip
ls -l $MYFILENAME
