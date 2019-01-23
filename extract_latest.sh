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
psql urls -c "SELECT url, reason, date_added FROM dir_blockedsite WHERE date_added >= '$1'" > /tmp/new_blockedsites.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex WHERE date_added >= '$1'" > /tmp/new_indexes.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_hr WHERE date_added >= '$1'" > /tmp/new_indexes_hr.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_ca WHERE date_added >= '$1'" > /tmp/new_indexes_ca.txt
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
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_sl WHERE date_added >= '$1'" > /tmp/new_indexes_sl.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_sv WHERE date_added >= '$1'" > /tmp/new_indexes_sv.txt
psql indexes -t -c "SELECT keywords FROM dir_pendingindex_tr WHERE date_added >= '$1'" > /tmp/new_indexes_tr.txt
psql zetaweb -t -c "SELECT url FROM site_info WHERE lastcrawled >= '$1'" > /tmp/new_pages.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_hr WHERE lastcrawled >= '$1'" > /tmp/new_pages_hr.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_ca WHERE lastcrawled >= '$1'" > /tmp/new_pages_ca.txt
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
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_sl WHERE lastcrawled >= '$1'" > /tmp/new_pages_sl.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_sw WHERE lastcrawled >= '$1'" > /tmp/new_pages_sw.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_sv WHERE lastcrawled >= '$1'" > /tmp/new_pages_sv.txt
psql zetaweb -t -c "SELECT url FROM dir_siteinfo_tr WHERE lastcrawled >= '$1'" > /tmp/new_pages_tr.txt
psql zetaweb -c "SELECT * FROM dir_domaininfo WHERE domain_updated >= '$1' OR whois_last_updated >= '$1' OR robots_last_updated >= '$1'" > /tmp/new_domains_full.txt
psql zetaweb -t -c "SELECT url FROM dir_domaininfo WHERE domain_updated >= '$1' OR whois_last_updated >= '$1' OR robots_last_updated >= '$1'" > /tmp/new_domains.txt
psql indexes -t -c "CREATE TABLE export_domainsearches AS SELECT * FROM dir_domainsearchlog WHERE last_search >= '$1'"
pg_dump --table=export_domainsearches --data-only --column-inserts indexes > /tmp/new_domain_searches.sql
psql indexes -t -c "DROP TABLE export_domainsearches"
psql indexes -t -c "SELECT * FROM dir_domainsearchlog WHERE last_search >= '$1'" > /tmp/new_domain_searches.txt
psql indexes -t -c "CREATE TABLE export_ipsearches AS SELECT * FROM dir_ipsearchlog WHERE last_search >= '$1'"
pg_dump --table=export_ipsearches --data-only --column-inserts indexes > /tmp/new_ip_searches.sql
psql indexes -t -c "DROP TABLE export_ipsearches"
psql indexes -t -c "SELECT * FROM dir_ipsearchlog WHERE last_search >= '$1'" > /tmp/new_ip_searches.txt
# dir_resultclick
psql indexes -t -c "CREATE TABLE export_resultclicks AS SELECT * FROM dir_resultclick WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks --data-only --column-inserts indexes > /tmp/new_result_clicks.sql
psql indexes -t -c "DROP TABLE export_resultclicks"
psql indexes -t -c "SELECT * FROM dir_resultclick WHERE click_time >= '$1'" > /tmp/new_result_clicks.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_de AS SELECT * FROM dir_resultclick_de WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_de --data-only --column-inserts indexes > /tmp/new_result_clicks_de.sql
psql indexes -t -c "DROP TABLE export_resultclicks_de"
psql indexes -t -c "SELECT * FROM dir_resultclick_de WHERE click_time >= '$1'" > /tmp/new_result_clicks_de.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_fr AS SELECT * FROM dir_resultclick_fr WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_fr --data-only --column-inserts indexes > /tmp/new_result_clicks_fr.sql
psql indexes -t -c "DROP TABLE export_resultclicks_fr"
psql indexes -t -c "SELECT * FROM dir_resultclick_fr WHERE click_time >= '$1'" > /tmp/new_result_clicks_fr.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_es AS SELECT * FROM dir_resultclick_es WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_es --data-only --column-inserts indexes > /tmp/new_result_clicks_es.sql
psql indexes -t -c "DROP TABLE export_resultclicks_es"
psql indexes -t -c "SELECT * FROM dir_resultclick_es WHERE click_time >= '$1'" > /tmp/new_result_clicks_es.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_nl AS SELECT * FROM dir_resultclick_nl WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_nl --data-only --column-inserts indexes > /tmp/new_result_clicks_nl.sql
psql indexes -t -c "DROP TABLE export_resultclicks_nl"
psql indexes -t -c "SELECT * FROM dir_resultclick_nl WHERE click_time >= '$1'" > /tmp/new_result_clicks_nl.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_it AS SELECT * FROM dir_resultclick_it WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_it --data-only --column-inserts indexes > /tmp/new_result_clicks_it.sql
psql indexes -t -c "DROP TABLE export_resultclicks_it"
psql indexes -t -c "SELECT * FROM dir_resultclick_it WHERE click_time >= '$1'" > /tmp/new_result_clicks_it.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_pl AS SELECT * FROM dir_resultclick_pl WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_pl --data-only --column-inserts indexes > /tmp/new_result_clicks_pl.sql
psql indexes -t -c "DROP TABLE export_resultclicks_pl"
psql indexes -t -c "SELECT * FROM dir_resultclick_pl WHERE click_time >= '$1'" > /tmp/new_result_clicks_pl.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_hr AS SELECT * FROM dir_resultclick_hr WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_hr --data-only --column-inserts indexes > /tmp/new_result_clicks_hr.sql
psql indexes -t -c "DROP TABLE export_resultclicks_hr"
psql indexes -t -c "SELECT * FROM dir_resultclick_hr WHERE click_time >= '$1'" > /tmp/new_result_clicks_hr.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_cs AS SELECT * FROM dir_resultclick_cs WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_cs --data-only --column-inserts indexes > /tmp/new_result_clicks_cs.sql
psql indexes -t -c "DROP TABLE export_resultclicks_cs"
psql indexes -t -c "SELECT * FROM dir_resultclick_cs WHERE click_time >= '$1'" > /tmp/new_result_clicks_cs.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_pt AS SELECT * FROM dir_resultclick_pt WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_pt --data-only --column-inserts indexes > /tmp/new_result_clicks_pt.sql
psql indexes -t -c "DROP TABLE export_resultclicks_pt"
psql indexes -t -c "SELECT * FROM dir_resultclick_pt WHERE click_time >= '$1'" > /tmp/new_result_clicks_pt.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_fi AS SELECT * FROM dir_resultclick_fi WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_fi --data-only --column-inserts indexes > /tmp/new_result_clicks_fi.sql
psql indexes -t -c "DROP TABLE export_resultclicks_fi"
psql indexes -t -c "SELECT * FROM dir_resultclick_fi WHERE click_time >= '$1'" > /tmp/new_result_clicks_fi.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_el AS SELECT * FROM dir_resultclick_el WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_el --data-only --column-inserts indexes > /tmp/new_result_clicks_el.sql
psql indexes -t -c "DROP TABLE export_resultclicks_el"
psql indexes -t -c "SELECT * FROM dir_resultclick_el WHERE click_time >= '$1'" > /tmp/new_result_clicks_el.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_sv AS SELECT * FROM dir_resultclick_sv WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_sv --data-only --column-inserts indexes > /tmp/new_result_clicks_sv.sql
psql indexes -t -c "DROP TABLE export_resultclicks_sv"
psql indexes -t -c "SELECT * FROM dir_resultclick_sv WHERE click_time >= '$1'" > /tmp/new_result_clicks_sv.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_tr AS SELECT * FROM dir_resultclick_tr WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_tr --data-only --column-inserts indexes > /tmp/new_result_clicks_tr.sql
psql indexes -t -c "DROP TABLE export_resultclicks_tr"
psql indexes -t -c "SELECT * FROM dir_resultclick_tr WHERE click_time >= '$1'" > /tmp/new_result_clicks_tr.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_ro AS SELECT * FROM dir_resultclick_ro WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_ro --data-only --column-inserts indexes > /tmp/new_result_clicks_ro.sql
psql indexes -t -c "DROP TABLE export_resultclicks_ro"
psql indexes -t -c "SELECT * FROM dir_resultclick_ro WHERE click_time >= '$1'" > /tmp/new_result_clicks_ro.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_hu AS SELECT * FROM dir_resultclick_hu WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_hu --data-only --column-inserts indexes > /tmp/new_result_clicks_hu.sql
psql indexes -t -c "DROP TABLE export_resultclicks_hu"
psql indexes -t -c "SELECT * FROM dir_resultclick_hu WHERE click_time >= '$1'" > /tmp/new_result_clicks_hu.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_sw AS SELECT * FROM dir_resultclick_sw WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_sw --data-only --column-inserts indexes > /tmp/new_result_clicks_sw.sql
psql indexes -t -c "DROP TABLE export_resultclicks_sw"
psql indexes -t -c "SELECT * FROM dir_resultclick_sw WHERE click_time >= '$1'" > /tmp/new_result_clicks_sw.txt

psql indexes -t -c "CREATE TABLE export_resultclicks_et AS SELECT * FROM dir_resultclick_et WHERE click_time >= '$1'"
pg_dump --table=export_resultclicks_et --data-only --column-inserts indexes > /tmp/new_result_clicks_et.sql
psql indexes -t -c "DROP TABLE export_resultclicks_et"
psql indexes -t -c "SELECT * FROM dir_resultclick_et WHERE click_time >= '$1'" > /tmp/new_result_clicks_et.txt

# Still need:
# ca
# lv
# lt
# sl

# --> Extract all data after a certain date.
# --> For ALL languages.

# dir_searchlog for ALL languages.
psql indexes -t -c "CREATE TABLE export_searches AS SELECT * FROM dir_searchlog WHERE last_search >= '$1'"
pg_dump --table=export_searches --data-only --column-inserts indexes > /tmp/new_searches.sql
psql indexes -t -c "DROP TABLE export_searches"
psql indexes -t -c "SELECT * FROM dir_searchlog WHERE last_search >= '$1'" > /tmp/new_searches.txt

psql indexes -t -c "CREATE TABLE export_searches_de AS SELECT * FROM dir_searchlog_de WHERE last_search >= '$1'"
pg_dump --table=export_searches_de --data-only --column-inserts indexes > /tmp/new_searches_de.sql
psql indexes -t -c "DROP TABLE export_searches_de"
psql indexes -t -c "SELECT * FROM dir_searchlog_de WHERE last_search >= '$1'" > /tmp/new_searches_de.txt

psql indexes -t -c "CREATE TABLE export_searches_fr AS SELECT * FROM dir_searchlog_fr WHERE last_search >= '$1'"
pg_dump --table=export_searches_fr --data-only --column-inserts indexes > /tmp/new_searches_fr.sql
psql indexes -t -c "DROP TABLE export_searches_fr"
psql indexes -t -c "SELECT * FROM dir_searchlog_fr WHERE last_search >= '$1'" > /tmp/new_searches_fr.txt

psql indexes -t -c "CREATE TABLE export_searches_es AS SELECT * FROM dir_searchlog_es WHERE last_search >= '$1'"
pg_dump --table=export_searches_es --data-only --column-inserts indexes > /tmp/new_searches_es.sql
psql indexes -t -c "DROP TABLE export_searches_es"
psql indexes -t -c "SELECT * FROM dir_searchlog_es WHERE last_search >= '$1'" > /tmp/new_searches_es.txt

psql indexes -t -c "CREATE TABLE export_searches_nl AS SELECT * FROM dir_searchlog_nl WHERE last_search >= '$1'"
pg_dump --table=export_searches_nl --data-only --column-inserts indexes > /tmp/new_searches_nl.sql
psql indexes -t -c "DROP TABLE export_searches_nl"
psql indexes -t -c "SELECT * FROM dir_searchlog_nl WHERE last_search >= '$1'" > /tmp/new_searches_nl.txt

psql indexes -t -c "CREATE TABLE export_searches_it AS SELECT * FROM dir_searchlog_it WHERE last_search >= '$1'"
pg_dump --table=export_searches_it --data-only --column-inserts indexes > /tmp/new_searches_it.sql
psql indexes -t -c "DROP TABLE export_searches_it"
psql indexes -t -c "SELECT * FROM dir_searchlog_it WHERE last_search >= '$1'" > /tmp/new_searches_it.txt

psql indexes -t -c "CREATE TABLE export_searches_pl AS SELECT * FROM dir_searchlog_pl WHERE last_search >= '$1'"
pg_dump --table=export_searches_pl --data-only --column-inserts indexes > /tmp/new_searches_pl.sql
psql indexes -t -c "DROP TABLE export_searches_pl"
psql indexes -t -c "SELECT * FROM dir_searchlog_pl WHERE last_search >= '$1'" > /tmp/new_searches_pl.txt

psql indexes -t -c "CREATE TABLE export_searches_sv AS SELECT * FROM dir_searchlog_sv WHERE last_search >= '$1'"
pg_dump --table=export_searches_sv --data-only --column-inserts indexes > /tmp/new_searches_sv.sql
psql indexes -t -c "DROP TABLE export_searches_sv"
psql indexes -t -c "SELECT * FROM dir_searchlog_sv WHERE last_search >= '$1'" > /tmp/new_searches_sv.txt

psql indexes -t -c "CREATE TABLE export_searches_cs AS SELECT * FROM dir_searchlog_cs WHERE last_search >= '$1'"
pg_dump --table=export_searches_cs --data-only --column-inserts indexes > /tmp/new_searches_cs.sql
psql indexes -t -c "DROP TABLE export_searches_cs"
psql indexes -t -c "SELECT * FROM dir_searchlog_cs WHERE last_search >= '$1'" > /tmp/new_searches_cs.txt

psql indexes -t -c "CREATE TABLE export_searches_tr AS SELECT * FROM dir_searchlog_tr WHERE last_search >= '$1'"
pg_dump --table=export_searches_tr --data-only --column-inserts indexes > /tmp/new_searches_tr.sql
psql indexes -t -c "DROP TABLE export_searches_tr"
psql indexes -t -c "SELECT * FROM dir_searchlog_tr WHERE last_search >= '$1'" > /tmp/new_searches_tr.txt

psql indexes -t -c "CREATE TABLE export_searches_ca AS SELECT * FROM dir_searchlog_ca WHERE last_search >= '$1'"
pg_dump --table=export_searches_ca --data-only --column-inserts indexes > /tmp/new_searches_ca.sql
psql indexes -t -c "DROP TABLE export_searches_ca"
psql indexes -t -c "SELECT * FROM dir_searchlog_ca WHERE last_search >= '$1'" > /tmp/new_searches_ca.txt

psql indexes -t -c "CREATE TABLE export_searches_hr AS SELECT * FROM dir_searchlog_hr WHERE last_search >= '$1'"
pg_dump --table=export_searches_hr --data-only --column-inserts indexes > /tmp/new_searches_hr.sql
psql indexes -t -c "DROP TABLE export_searches_hr"
psql indexes -t -c "SELECT * FROM dir_searchlog_hr WHERE last_search >= '$1'" > /tmp/new_searches_hr.txt

psql indexes -t -c "CREATE TABLE export_searches_et AS SELECT * FROM dir_searchlog_et WHERE last_search >= '$1'"
pg_dump --table=export_searches_et --data-only --column-inserts indexes > /tmp/new_searches_et.sql
psql indexes -t -c "DROP TABLE export_searches_et"
psql indexes -t -c "SELECT * FROM dir_searchlog_et WHERE last_search >= '$1'" > /tmp/new_searches_et.txt

psql indexes -t -c "CREATE TABLE export_searches_fi AS SELECT * FROM dir_searchlog_fi WHERE last_search >= '$1'"
pg_dump --table=export_searches_fi --data-only --column-inserts indexes > /tmp/new_searches_fi.sql
psql indexes -t -c "DROP TABLE export_searches_fi"
psql indexes -t -c "SELECT * FROM dir_searchlog_fi WHERE last_search >= '$1'" > /tmp/new_searches_fi.txt

psql indexes -t -c "CREATE TABLE export_searches_el AS SELECT * FROM dir_searchlog_el WHERE last_search >= '$1'"
pg_dump --table=export_searches_el --data-only --column-inserts indexes > /tmp/new_searches_el.sql
psql indexes -t -c "DROP TABLE export_searches_el"
psql indexes -t -c "SELECT * FROM dir_searchlog_el WHERE last_search >= '$1'" > /tmp/new_searches_el.txt

psql indexes -t -c "CREATE TABLE export_searches_hu AS SELECT * FROM dir_searchlog_hu WHERE last_search >= '$1'"
pg_dump --table=export_searches_hu --data-only --column-inserts indexes > /tmp/new_searches_hu.sql
psql indexes -t -c "DROP TABLE export_searches_hu"
psql indexes -t -c "SELECT * FROM dir_searchlog_hu WHERE last_search >= '$1'" > /tmp/new_searches_hu.txt

psql indexes -t -c "CREATE TABLE export_searches_lt AS SELECT * FROM dir_searchlog_lt WHERE last_search >= '$1'"
pg_dump --table=export_searches_lt --data-only --column-inserts indexes > /tmp/new_searches_lt.sql
psql indexes -t -c "DROP TABLE export_searches_lt"
psql indexes -t -c "SELECT * FROM dir_searchlog_lt WHERE last_search >= '$1'" > /tmp/new_searches_lt.txt

psql indexes -t -c "CREATE TABLE export_searches_lv AS SELECT * FROM dir_searchlog_lv WHERE last_search >= '$1'"
pg_dump --table=export_searches_lv --data-only --column-inserts indexes > /tmp/new_searches_lv.sql
psql indexes -t -c "DROP TABLE export_searches_lv"
psql indexes -t -c "SELECT * FROM dir_searchlog_lv WHERE last_search >= '$1'" > /tmp/new_searches_lv.txt

psql indexes -t -c "CREATE TABLE export_searches_pt AS SELECT * FROM dir_searchlog_pt WHERE last_search >= '$1'"
pg_dump --table=export_searches_pt --data-only --column-inserts indexes > /tmp/new_searches_pt.sql
psql indexes -t -c "DROP TABLE export_searches_pt"
psql indexes -t -c "SELECT * FROM dir_searchlog_pt WHERE last_search >= '$1'" > /tmp/new_searches_pt.txt

psql indexes -t -c "CREATE TABLE export_searches_ro AS SELECT * FROM dir_searchlog_ro WHERE last_search >= '$1'"
pg_dump --table=export_searches_ro --data-only --column-inserts indexes > /tmp/new_searches_ro.sql
psql indexes -t -c "DROP TABLE export_searches_ro"
psql indexes -t -c "SELECT * FROM dir_searchlog_ro WHERE last_search >= '$1'" > /tmp/new_searches_ro.txt

psql indexes -t -c "CREATE TABLE export_searches_sl AS SELECT * FROM dir_searchlog_sl WHERE last_search >= '$1'"
pg_dump --table=export_searches_sl --data-only --column-inserts indexes > /tmp/new_searches_sl.sql
psql indexes -t -c "DROP TABLE export_searches_sl"
psql indexes -t -c "SELECT * FROM dir_searchlog_sl WHERE last_search >= '$1'" > /tmp/new_searches_sl.txt

psql indexes -t -c "CREATE TABLE export_searches_sw AS SELECT * FROM dir_searchlog_sw WHERE last_search >= '$1'"
pg_dump --table=export_searches_sw --data-only --column-inserts indexes > /tmp/new_searches_sw.sql
psql indexes -t -c "DROP TABLE export_searches_sw"
psql indexes -t -c "SELECT * FROM dir_searchlog_sw WHERE last_search >= '$1'" > /tmp/new_searches_sw.txt
