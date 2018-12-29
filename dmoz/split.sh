#!/bin/bash
#
# This script is meant to be run against the extracted parsed-domain.csv.7z file available via Harvard Dataverse here:
# https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/OMV93V
#
# That file contains URLs from the DMOZ data dump and this script splits that file into files grouped by language.
# Extract using: p7zip -d parsed-domain.csv.7z
#
# Those files can then presumably be split into language-specific URL lists by parsing the CSV and using the contents of column 1.
# See csv_split.py for that.
#
#cat parsed-new.csv |grep -v "World/Japanese"|grep -v "World/Russian"|grep -v "World/Thai"|grep -v "World/Ukrainian"|grep -v "World/Bulgarian"|grep -v "World/Galego"|grep -v "World/Chinese_Traditional"|grep -v "World/Chinese_Simplified" > parsed-new_no_ja_th_bg_uk_ru_ga_zh
#World/Lietuvių
#World/Slovensko
#World/Hrvatski
#World/Arabic
#World/Bosanski

grep "World/Česky" parsed-new.csv > cs.csv
grep "World/Nederlands" parsed-new.csv > nl.csv
grep "World/Suomi" parsed-new.csv > fi.csv
grep "World/Français" parsed-new.csv > fr.csv
grep "World/Deutsch" parsed-new.csv > de.csv
grep "World/Greek" parsed-new.csv > el.csv
grep "World/Magyar" parsed-new.csv > hu.csv
grep "World/Italiano" parsed-new.csv > it.csv
grep "World/Polski" parsed-new.csv > pl.csv
grep "World/Português" parsed-new.csv > pt.csv
grep "World/Español" parsed-new.csv > es.csv
grep "World/Svenska" parsed-new.csv > sv.csv
grep "World/Dansk" parsed-new.csv > da.csv
grep "World/Norsk" parsed-new.csv > no.csv
grep "World/Türkçe" parsed-new.csv > tr.csv
grep "World/Hrvatski" parsed-new.csv > hr.csv
grep "World/Eesti" parsed-new.csv > et.csv
grep "World/Lietuvių" parsed-new.csv > lt.csv
grep "World/Latviski" parsed-new.csv > lv.csv
grep "World/Română" parsed-new.csv > ro.csv
grep "World/Kiswahili" parsed-new.csv > sw.csv
grep -v "/World/" parsed-new.csv > en.csv

