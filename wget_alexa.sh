#!/bin/bash
# This retrieves the top 1 million Alexa URLs. It is called by a cron job, but
# can also be used manually.
mkdir -p ./urls/alexa
MYDATESTR=$(date +"%Y-%m-%d")
MYFILENAME="./urls/alexa/top-1m_$MYDATESTR.csv.zip"
echo "Getting top-1m.csv.zip as $MYFILENAME"
wget -O $MYFILENAME http://s3.amazonaws.com/alexa-static/top-1m.csv.zip
ls -l $MYFILENAME
