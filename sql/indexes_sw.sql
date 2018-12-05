CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_sw_pagetitle_gin ON dir_siteinfo_sw USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_sw_pagedescription_gin ON dir_siteinfo_sw USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_sw_pagekeywords_gin ON dir_siteinfo_sw USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_sw_pagefirstheadtag_gin ON dir_siteinfo_sw USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_sw_pagefirsth2tag_gin ON dir_siteinfo_sw USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_sw_pagefirsth3tag_gin ON dir_siteinfo_sw USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_sw_pagetext_gin ON dir_siteinfo_sw USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_sw_url_gin ON dir_siteinfo_sw USING gin(url gin_trgm_ops);
