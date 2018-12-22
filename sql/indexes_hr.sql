CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX dir_siteinfo_hr_pagetitle_gin ON dir_siteinfo_hr USING gin(pagetitle gin_trgm_ops);
CREATE INDEX dir_siteinfo_hr_pagedescription_gin ON dir_siteinfo_hr USING gin(pagedescription gin_trgm_ops);
CREATE INDEX dir_siteinfo_hr_pagekeywords_gin ON dir_siteinfo_hr USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX dir_siteinfo_hr_pagefirstheadtag_gin ON dir_siteinfo_hr USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX dir_siteinfo_hr_pagefirsth2tag_gin ON dir_siteinfo_hr USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_hr_pagefirsth3tag_gin ON dir_siteinfo_hr USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX dir_siteinfo_hr_pagetext_gin ON dir_siteinfo_hr USING gin(pagetext gin_trgm_ops);
CREATE INDEX dir_siteinfo_hr_url_gin ON dir_siteinfo_hr USING gin(url gin_trgm_ops);
