ICANN zone file downloads go here.

Typicall the czdz Python client will be configured to write to this directory.

https://github.com/icann/czds-api-client-python

To process zone files, run:

```
python process_zone_files.py zonefiles_2021-02-16
```

(or whatever directory the text files are in).

There is no need to unzip the files because the script uses gzip. Unzipping takes
forever and wastes a lot of disk space anyway.

Processed files go in out/ and can be crawled with crawl_all_icann_domains.py in
the root directory.
