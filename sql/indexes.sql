CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX site_info_pagetitle_gin ON site_info USING gin(pagetitle gin_trgm_ops);
CREATE INDEX site_info_pagedescription_gin ON site_info USING gin(pagedescription gin_trgm_ops);
CREATE INDEX site_info_pagekeywords_gin ON site_info USING gin(pagekeywords gin_trgm_ops);
CREATE INDEX site_info_pagefirstheadtag_gin ON site_info USING gin(pagefirstheadtag gin_trgm_ops);
CREATE INDEX site_info_pagefirsth2tag_gin ON site_info USING gin(pagefirsth2tag gin_trgm_ops);
CREATE INDEX site_info_pagefirsth3tag_gin ON site_info USING gin(pagefirsth3tag gin_trgm_ops);
CREATE INDEX site_info_pagetext_gin ON site_info USING gin(pagetext gin_trgm_ops);
CREATE INDEX site_info_url_gin ON site_info USING gin(url gin_trgm_ops);