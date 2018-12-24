CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_pl_pagetitle_gin ON dir_siteinfo_pl USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_pl_pagedescription_gin ON dir_siteinfo_pl USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_pl_pagekeywords_gin ON dir_siteinfo_pl USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_pl_pagefirstheadtag_gin ON dir_siteinfo_pl USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_pl_pagefirsth2tag_gin ON dir_siteinfo_pl USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_pl_pagefirsth3tag_gin ON dir_siteinfo_pl USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_pl_pagetext_gin ON dir_siteinfo_pl USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_pl_url_gin ON dir_siteinfo_pl USING gin(url gin_trgm_ops);