CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_fi_pagetitle_gin ON dir_siteinfo_fi USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_fi_pagedescription_gin ON dir_siteinfo_fi USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_fi_pagekeywords_gin ON dir_siteinfo_fi USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_fi_pagefirstheadtag_gin ON dir_siteinfo_fi USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_fi_pagefirsth2tag_gin ON dir_siteinfo_fi USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_fi_pagefirsth3tag_gin ON dir_siteinfo_fi USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_fi_pagetext_gin ON dir_siteinfo_fi USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_fi_url_gin ON dir_siteinfo_fi USING gin(url gin_trgm_ops);
