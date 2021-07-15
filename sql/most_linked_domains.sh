#!/bin/bash
time psql -c "COPY ( select url, domains_linking_in from dir_domaininfo where domains_linking_in > 0 order by domains_linking_in desc limit 1000000 ) TO STDOUT WITH CSV HEADER " zetaweb > /tmp/most_linked_domains_2021-07.csv
