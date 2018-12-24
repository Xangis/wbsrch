CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_ro_pagetitle_gin ON dir_siteinfo_ro USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_ro_pagedescription_gin ON dir_siteinfo_ro USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_ro_pagekeywords_gin ON dir_siteinfo_ro USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_ro_pagefirstheadtag_gin ON dir_siteinfo_ro USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_ro_pagefirsth2tag_gin ON dir_siteinfo_ro USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_ro_pagefirsth3tag_gin ON dir_siteinfo_ro USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_ro_pagetext_gin ON dir_siteinfo_ro USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_ro_url_gin ON dir_siteinfo_ro USING gin(url gin_trgm_ops);