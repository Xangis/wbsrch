#!/bin/bash
time psql -c "COPY ( select url from dir_blockedsite where reason = 4 ) TO STDOUT WITH CSV HEADER " indexes > /tmp/adult_domains_2021-03.csv
