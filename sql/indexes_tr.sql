CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_tr_pagetitle_gin ON dir_siteinfo_tr USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_tr_pagedescription_gin ON dir_siteinfo_tr USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_tr_pagekeywords_gin ON dir_siteinfo_tr USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_tr_pagefirstheadtag_gin ON dir_siteinfo_tr USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_tr_pagefirsth2tag_gin ON dir_siteinfo_tr USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_tr_pagefirsth3tag_gin ON dir_siteinfo_tr USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_tr_pagetext_gin ON dir_siteinfo_tr USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_tr_url_gin ON dir_siteinfo_tr USING gin(url gin_trgm_ops);