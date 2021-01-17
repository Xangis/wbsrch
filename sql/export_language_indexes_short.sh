#!/bin/bash
# Exports all of the tables required to update an index for a particular language.
# Assumes you already ran export_language_indexes at some point and just need to
# update the indexterm and keywordranking tables.
# Usage: ./export_language_indexes_short.sh <2-letter-language-code>
# Example: ./export_language_indexes_short.sh fr
DATE=$(/bin/date +"%Y-%m-%d")
MYLANG=$1
time pg_dump -t dir_indexterm_$MYLANG indexes > /tmp/dir_indexterm_"$MYLANG"_$DATE.sql
time pg_dump -t dir_keywordranking_$MYLANG indexes > /tmp/dir_keywordranking_"$MYLANG"_$DATE.sql
ls -l /tmp/*.sql
