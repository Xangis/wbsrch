CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_es_pagetitle_gin ON dir_siteinfo_es USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_es_pagedescription_gin ON dir_siteinfo_es USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_es_pagekeywords_gin ON dir_siteinfo_es USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_es_pagefirstheadtag_gin ON dir_siteinfo_es USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_es_pagefirsth2tag_gin ON dir_siteinfo_es USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_es_pagefirsth3tag_gin ON dir_siteinfo_es USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_es_pagetext_gin ON dir_siteinfo_es USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_es_url_gin ON dir_siteinfo_es USING gin(url gin_trgm_ops);