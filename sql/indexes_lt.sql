CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_lt_pagetitle_gin ON dir_siteinfo_lt USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_lt_pagedescription_gin ON dir_siteinfo_lt USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_lt_pagekeywords_gin ON dir_siteinfo_lt USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_lt_pagefirstheadtag_gin ON dir_siteinfo_lt USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_lt_pagefirsth2tag_gin ON dir_siteinfo_lt USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_lt_pagefirsth3tag_gin ON dir_siteinfo_lt USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_lt_pagetext_gin ON dir_siteinfo_lt USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_lt_url_gin ON dir_siteinfo_lt USING gin(url gin_trgm_ops);
