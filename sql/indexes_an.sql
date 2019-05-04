CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_an_pagetitle_gin ON dir_siteinfo_an USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_an_pagedescription_gin ON dir_siteinfo_an USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_an_pagekeywords_gin ON dir_siteinfo_an USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_an_pagefirstheadtag_gin ON dir_siteinfo_an USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_an_pagefirsth2tag_gin ON dir_siteinfo_an USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_an_pagefirsth3tag_gin ON dir_siteinfo_an USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_an_pagetext_gin ON dir_siteinfo_an USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_an_url_gin ON dir_siteinfo_an USING gin(url gin_trgm_ops);
CREATE INDEX dir_siteinfo_an_rooturl_gin ON dir_siteinfo_an USING gin(rooturl gin_trgm_ops);