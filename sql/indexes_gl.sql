CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_gl_pagetitle_gin ON dir_siteinfo_gl USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_gl_pagedescription_gin ON dir_siteinfo_gl USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_gl_pagekeywords_gin ON dir_siteinfo_gl USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_gl_pagefirstheadtag_gin ON dir_siteinfo_gl USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_gl_pagefirsth2tag_gin ON dir_siteinfo_gl USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_gl_pagefirsth3tag_gin ON dir_siteinfo_gl USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_gl_pagetext_gin ON dir_siteinfo_gl USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_gl_url_gin ON dir_siteinfo_gl USING gin(url gin_trgm_ops);
CREATE INDEX dir_siteinfo_gl_rooturl_gin ON dir_siteinfo_gl USING gin(rooturl gin_trgm_ops);