#!/bin/bash
# This builds files containing all of the things that have been updated since
# the date provided.
# Usage: ./extract_latest.sh 2018-12-12
#
# These extracts will be in text files that you can then use with python manage.py index -f
# and similar commands.
psql indexes -t -c "SELECT keywords FROM dir_indexterm WHERE date_indexed >= '$1'" > /tmp/new_keywords.txt
psql indexes -c "SELECT id, keywords, typo_for FROM dir_indexterm WHERE typo_for IS NOT NULL AND date_indexed >= '$1'" > /tmp/new_keyword_typos.txt
psql indexes -t -c "SELECT keywords FROM dir_indexterm WHERE actively_blocked = true AND date_indexed >= '$1'" > /tmp/new_keyword_blocks.txt
psql indexes -c "SELECT keywords, is_language FROM dir_indexterm WHERE is_language IS NOT NULL AND is_language != '' AND date_indexed >= '$1'" > /tmp/new_keyword_languages.txt
psql urls -c "SELECT url, reason, date_added FROM dir_blockedsite WHERE date_added >= '$1'" > /tmp/new_blockedistes.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex WHERE date_added >= '$1'" > /tmp/new_indexes.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_hr WHERE date_added >= '$1'" > /tmp/new_indexes_hr.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_cs WHERE date_added >= '$1'" > /tmp/new_indexes_cs.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_nl WHERE date_added >= '$1'" > /tmp/new_indexes_nl.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_et WHERE date_added >= '$1'" > /tmp/new_indexes_et.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_fi WHERE date_added >= '$1'" > /tmp/new_indexes_fi.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_fr WHERE date_added >= '$1'" > /tmp/new_indexes_fr.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_de WHERE date_added >= '$1'" > /tmp/new_indexes_de.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_el WHERE date_added >= '$1'" > /tmp/new_indexes_el.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_hu WHERE date_added >= '$1'" > /tmp/new_indexes_hu.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_it WHERE date_added >= '$1'" > /tmp/new_indexes_it.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_lv WHERE date_added >= '$1'" > /tmp/new_indexes_lv.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_lt WHERE date_added >= '$1'" > /tmp/new_indexes_lt.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_pl WHERE date_added >= '$1'" > /tmp/new_indexes_pl.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_pt WHERE date_added >= '$1'" > /tmp/new_indexes_pt.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_ro WHERE date_added >= '$1'" > /tmp/new_indexes_ro.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_es WHERE date_added >= '$1'" > /tmp/new_indexes_es.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_sw WHERE date_added >= '$1'" > /tmp/new_indexes_sw.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_sv WHERE date_added >= '$1'" > /tmp/new_indexes_sv.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_tr WHERE date_added >= '$1'" > /tmp/new_indexes_tr.txt
psql zetaweb -t -c "SELECT url FROM site_info WHERE lastcrawled >= '$1'" > /tmp/new_pages.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_hr WHERE lastcrawled >= '$1'" > /tmp/new_pages_hr.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_cs WHERE lastcrawled >= '$1'" > /tmp/new_pages_cs.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_nl WHERE lastcrawled >= '$1'" > /tmp/new_pages_nl.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_et WHERE lastcrawled >= '$1'" > /tmp/new_pages_et.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_fi WHERE lastcrawled >= '$1'" > /tmp/new_pages_fi.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_fr WHERE lastcrawled >= '$1'" > /tmp/new_pages_fr.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_de WHERE lastcrawled >= '$1'" > /tmp/new_pages_de.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_el WHERE lastcrawled >= '$1'" > /tmp/new_pages_el.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_hu WHERE lastcrawled >= '$1'" > /tmp/new_pages_hu.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_it WHERE lastcrawled >= '$1'" > /tmp/new_pages_it.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_lv WHERE lastcrawled >= '$1'" > /tmp/new_pages_lv.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_lt WHERE lastcrawled >= '$1'" > /tmp/new_pages_lt.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_pl WHERE lastcrawled >= '$1'" > /tmp/new_pages_pl.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_pt WHERE lastcrawled >= '$1'" > /tmp/new_pages_pt.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_ro WHERE lastcrawled >= '$1'" > /tmp/new_pages_ro.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_es WHERE lastcrawled >= '$1'" > /tmp/new_pages_es.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_sw WHERE lastcrawled >= '$1'" > /tmp/new_pages_sw.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_sv WHERE lastcrawled >= '$1'" > /tmp/new_pages_sv.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_tr WHERE lastcrawled >= '$1'" > /tmp/new_pages_tr.txt
psql zetaweb -c "SELECT * FROM dir_domaininfo WHERE domain_updated >= '$1' OR whois_last_updated >= '$1' OR robots_last_updated >= '$1'" > /tmp/new_domains_full.txt
psql zetaweb -t -c "SELECT url FROM dir_domaininfo WHERE domain_updated >= '$1' OR whois_last_updated >= '$1' OR robots_last_updated >= '$1'" > /tmp/new_domains.txt
# TODO: Also extract these in a useful re-importable way:
# dir_domainsearchlog
# --> Extract all after certain date.
# dir_ipsearchlog
# --> Extract all after certain date.
# dir_resultclick
# --> Extract all data after a certain date.
# --> For ALL languages.
# dir_searchlog
# --> Extract all data after a certain date.
# --> For ALL languages.
