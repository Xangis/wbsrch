CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_et_pagetitle_gin ON dir_siteinfo_et USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_et_pagedescription_gin ON dir_siteinfo_et USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_et_pagekeywords_gin ON dir_siteinfo_et USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_et_pagefirstheadtag_gin ON dir_siteinfo_et USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_et_pagefirsth2tag_gin ON dir_siteinfo_et USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_et_pagefirsth3tag_gin ON dir_siteinfo_et USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_et_pagetext_gin ON dir_siteinfo_et USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_et_url_gin ON dir_siteinfo_et USING gin(url gin_trgm_ops);
