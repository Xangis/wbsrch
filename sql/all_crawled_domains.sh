#!/bin/bash
time psql -c "COPY ( select distinct rooturl from site_info order by rooturl ) TO STDOUT WITH CSV HEADER " zetaweb > /tmp/wbsrch_all_crawled_domains_2021-07.csv
