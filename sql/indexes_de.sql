CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_de_pagetitle_gin ON dir_siteinfo_de USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_de_pagedescription_gin ON dir_siteinfo_de USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_de_pagekeywords_gin ON dir_siteinfo_de USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_de_pagefirstheadtag_gin ON dir_siteinfo_de USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_de_pagefirsth2tag_gin ON dir_siteinfo_de USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_de_pagefirsth3tag_gin ON dir_siteinfo_de USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_de_pagetext_gin ON dir_siteinfo_de USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_de_url_gin ON dir_siteinfo_de USING gin(url gin_trgm_ops);
