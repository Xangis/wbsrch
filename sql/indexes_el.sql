CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_el_pagetitle_gin ON dir_siteinfo_el USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_el_pagedescription_gin ON dir_siteinfo_el USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_el_pagekeywords_gin ON dir_siteinfo_el USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_el_pagefirstheadtag_gin ON dir_siteinfo_el USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_el_pagefirsth2tag_gin ON dir_siteinfo_el USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_el_pagefirsth3tag_gin ON dir_siteinfo_el USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_el_pagetext_gin ON dir_siteinfo_el USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_el_url_gin ON dir_siteinfo_el USING gin(url gin_trgm_ops);
