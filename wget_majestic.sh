#!/bin/bash
# This retrieves the top 1 million Alexa URLs. It is called by a cron job, but
# can also be used manually.
mkdir -p ./urls/majestic
MYDATESTR=$(date +"%Y-%m-%d")
MYFILENAME="./urls/majestic/majestic_million_$MYDATESTR.csv"
echo "Getting majestic_million.csv as $MYFILENAME"
wget -O $MYFILENAME http://downloads.majestic.com/majestic_million.csv
ls -l $MYFILENAME
