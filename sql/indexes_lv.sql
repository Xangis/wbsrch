CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_lv_pagetitle_gin ON dir_siteinfo_lv USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_lv_pagedescription_gin ON dir_siteinfo_lv USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_lv_pagekeywords_gin ON dir_siteinfo_lv USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_lv_pagefirstheadtag_gin ON dir_siteinfo_lv USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_lv_pagefirsth2tag_gin ON dir_siteinfo_lv USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_lv_pagefirsth3tag_gin ON dir_siteinfo_lv USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_lv_pagetext_gin ON dir_siteinfo_lv USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_lv_url_gin ON dir_siteinfo_lv USING gin(url gin_trgm_ops);