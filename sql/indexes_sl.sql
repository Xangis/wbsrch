CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_sl_pagetitle_gin ON dir_siteinfo_sl USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_sl_pagedescription_gin ON dir_siteinfo_sl USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_sl_pagekeywords_gin ON dir_siteinfo_sl USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_sl_pagefirstheadtag_gin ON dir_siteinfo_sl USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_sl_pagefirsth2tag_gin ON dir_siteinfo_sl USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_sl_pagefirsth3tag_gin ON dir_siteinfo_sl USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_sl_pagetext_gin ON dir_siteinfo_sl USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_sl_url_gin ON dir_siteinfo_sl USING gin(url gin_trgm_ops);
