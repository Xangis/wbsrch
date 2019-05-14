#!/bin/bash
time psql -c "COPY ( select url from dir_blockedsite where reason = 4 ) TO STDOUT WITH CSV HEADER " urls > /tmp/adult_domains_2019-05.csv
