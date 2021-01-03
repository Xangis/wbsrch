#!/bin/bash
# Exports all of the tables required to run an index for a particular language.
# Usage: ./export_language_indexes <2-letter-language-code>
# Example: ./export_language_indexes fr
DATE=$(/bin/date +"%Y-%m-%d")
MYLANG=$1
time pg_dump -t dir_autocomplete_$MYLANG indexes > /tmp/dir_autocomplete_"$MYLANG"_$DATE.sql
time pg_dump -t dir_indexterm_$MYLANG indexes > /tmp/dir_indexterm_"$MYLANG"_$DATE.sql
time pg_dump -t dir_keywordranking_$MYLANG indexes > /tmp/dir_keywordranking_"$MYLANG"_$DATE.sql
time pg_dump -t dir_pendingindex_$MYLANG indexes > /tmp/dir_pendingindex_"$MYLANG"_$DATE.sql
time pg_dump -t dir_resultclick_$MYLANG indexes > /tmp/dir_resultclick_"$MYLANG"_$DATE.sql
time pg_dump -t dir_searchlog_$MYLANG indexes > /tmp/dir_searchlog_"$MYLANG"_$DATE.sql
ls -l /tmp/*.sql
