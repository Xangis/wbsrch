CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_cs_pagetitle_gin ON dir_siteinfo_cs USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_cs_pagedescription_gin ON dir_siteinfo_cs USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_cs_pagekeywords_gin ON dir_siteinfo_cs USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_cs_pagefirstheadtag_gin ON dir_siteinfo_cs USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_cs_pagefirsth2tag_gin ON dir_siteinfo_cs USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_cs_pagefirsth3tag_gin ON dir_siteinfo_cs USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_cs_pagetext_gin ON dir_siteinfo_cs USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_cs_url_gin ON dir_siteinfo_cs USING gin(url gin_trgm_ops);
