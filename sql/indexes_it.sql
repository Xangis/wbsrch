CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_it_pagetitle_gin ON dir_siteinfo_it USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_it_pagedescription_gin ON dir_siteinfo_it USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_it_pagekeywords_gin ON dir_siteinfo_it USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_it_pagefirstheadtag_gin ON dir_siteinfo_it USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_it_pagefirsth2tag_gin ON dir_siteinfo_it USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_it_pagefirsth3tag_gin ON dir_siteinfo_it USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_it_pagetext_gin ON dir_siteinfo_it USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_it_url_gin ON dir_siteinfo_it USING gin(url gin_trgm_ops);
