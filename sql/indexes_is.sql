CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_is_pagetitle_gin ON dir_siteinfo_is USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_is_pagedescription_gin ON dir_siteinfo_is USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_is_pagekeywords_gin ON dir_siteinfo_is USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_is_pagefirstheadtag_gin ON dir_siteinfo_is USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_is_pagefirsth2tag_gin ON dir_siteinfo_is USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_is_pagefirsth3tag_gin ON dir_siteinfo_is USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_is_pagetext_gin ON dir_siteinfo_is USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_is_url_gin ON dir_siteinfo_is USING gin(url gin_trgm_ops);
CREATE INDEX dir_siteinfo_is_rooturl_gin ON dir_siteinfo_is USING gin(rooturl gin_trgm_ops);
CREATE INDEX dir_siteinfo_is_rooturl_btree ON dir_siteinfo_is (rooturl);