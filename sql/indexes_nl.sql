CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_nl_pagetitle_gin ON dir_siteinfo_nl USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_nl_pagedescription_gin ON dir_siteinfo_nl USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_nl_pagekeywords_gin ON dir_siteinfo_nl USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_nl_pagefirstheadtag_gin ON dir_siteinfo_nl USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_nl_pagefirsth2tag_gin ON dir_siteinfo_nl USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_nl_pagefirsth3tag_gin ON dir_siteinfo_nl USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_nl_pagetext_gin ON dir_siteinfo_nl USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_nl_url_gin ON dir_siteinfo_nl USING gin(url gin_trgm_ops);
