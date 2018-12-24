CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_sv_pagetitle_gin ON dir_siteinfo_sv USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_sv_pagedescription_gin ON dir_siteinfo_sv USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_sv_pagekeywords_gin ON dir_siteinfo_sv USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_sv_pagefirstheadtag_gin ON dir_siteinfo_sv USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_sv_pagefirsth2tag_gin ON dir_siteinfo_sv USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_sv_pagefirsth3tag_gin ON dir_siteinfo_sv USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_sv_pagetext_gin ON dir_siteinfo_sv USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_sv_url_gin ON dir_siteinfo_sv USING gin(url gin_trgm_ops);