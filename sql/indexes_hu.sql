CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_hu_pagetitle_gin ON dir_siteinfo_hu USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_hu_pagedescription_gin ON dir_siteinfo_hu USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_hu_pagekeywords_gin ON dir_siteinfo_hu USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_hu_pagefirstheadtag_gin ON dir_siteinfo_hu USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_hu_pagefirsth2tag_gin ON dir_siteinfo_hu USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_hu_pagefirsth3tag_gin ON dir_siteinfo_hu USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_hu_pagetext_gin ON dir_siteinfo_hu USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_hu_url_gin ON dir_siteinfo_hu USING gin(url gin_trgm_ops);