CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_fr_pagetitle_gin ON dir_siteinfo_fr USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_fr_pagedescription_gin ON dir_siteinfo_fr USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_fr_pagekeywords_gin ON dir_siteinfo_fr USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_fr_pagefirstheadtag_gin ON dir_siteinfo_fr USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_fr_pagefirsth2tag_gin ON dir_siteinfo_fr USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_fr_pagefirsth3tag_gin ON dir_siteinfo_fr USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_fr_pagetext_gin ON dir_siteinfo_fr USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_fr_url_gin ON dir_siteinfo_fr USING gin(url gin_trgm_ops);
