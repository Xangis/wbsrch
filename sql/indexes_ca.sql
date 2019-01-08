CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_ca_pagetitle_gin ON dir_siteinfo_ca USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_ca_pagedescription_gin ON dir_siteinfo_ca USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_ca_pagekeywords_gin ON dir_siteinfo_ca USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_ca_pagefirstheadtag_gin ON dir_siteinfo_ca USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_ca_pagefirsth2tag_gin ON dir_siteinfo_ca USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_ca_pagefirsth3tag_gin ON dir_siteinfo_ca USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_ca_pagetext_gin ON dir_siteinfo_ca USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_ca_url_gin ON dir_siteinfo_ca USING gin(url gin_trgm_ops);
