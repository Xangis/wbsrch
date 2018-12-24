CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_pt_pagetitle_gin ON dir_siteinfo_pt USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_pt_pagedescription_gin ON dir_siteinfo_pt USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_pt_pagekeywords_gin ON dir_siteinfo_pt USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_pt_pagefirstheadtag_gin ON dir_siteinfo_pt USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_pt_pagefirsth2tag_gin ON dir_siteinfo_pt USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_pt_pagefirsth3tag_gin ON dir_siteinfo_pt USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_pt_pagetext_gin ON dir_siteinfo_pt USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_pt_url_gin ON dir_siteinfo_pt USING gin(url gin_trgm_ops);