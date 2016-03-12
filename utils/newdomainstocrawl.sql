# This gets new domains to crawl from the domain search logs.
# It was last run on Feb 7, 2016 at noon.
SELECT distinct(keywords) FROM dir_domainsearchlog WHERE last_search > (CURRENT_DATE - INTERVAL '31 days') AND result_count = 0 AND keywords not ilike '% %' AND keywords ILIKE '%.%' AND is_bot = false;
