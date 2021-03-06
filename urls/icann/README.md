ICANN zone file downloads go here.

Typicall the czdz Python client will be configured to write to this directory.

https://github.com/icann/czds-api-client-python

To process zone files, first gunzip them, then run:

```
python process_zone_files.py zonefiles_2021-02-16
```

(or whatever directory the text files are in).

Processed files go in out/ and can be crawled with crawl_all_icann_domains.py in
the root directory.
