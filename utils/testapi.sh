#!/bin/bash
# This script is meant for testing the WbSrch API using CURL.
curl -X GET https://wbsrch.com/api/domain_link_rank/?domain=youporn.com -H 'Authorization: Token ed740e11d3f0e7383d1c7a05a204d6c5f9c501d6'
echo
curl -X GET https://wbsrch.com/api/domain_link_rank/?domain=http://www.tacobell.com -H 'Authorization: Token ed740e11d3f0e7383d1c7a05a204d6c5f9c501d6'
echo
curl -X GET https://wbsrch.com/api/domain_link_rank/?domain=searchengineland.com -H 'Authorization: Token ed740e11d3f0e7383d1c7a05a204d6c5f9c501d6'
echo
curl -X GET https://wbsrch.com/api/domain_link_rank/?domain=https://youtube.com -H 'Authorization: Token ed740e11d3f0e7383d1c7a05a204d6c5f9c501d6'
echo
curl -X GET https://wbsrch.com/api/domain_link_rank/?domain=arstechnica.com -H 'Authorization: Token ed740e11d3f0e7383d1c7a05a204d6c5f9c501d6'
echo
curl -X GET https://wbsrch.com/api/ip_to_country/?ip=216.151.17.10 -H 'Authorization: Token ed740e11d3f0e7383d1c7a05a204d6c5f9c501d6'
echo
curl -X GET https://wbsrch.com/api/domain_pages_in_index/?domain=zetacentauri.com -H 'Authorization: Token ed740e11d3f0e7383d1c7a05a204d6c5f9c501d6'
echo
curl -X GET https://wbsrch.com/api/domain_pages_in_index/?domain=freewavesamples.com -H 'Authorization: Token ed740e11d3f0e7383d1c7a05a204d6c5f9c501d6'
echo
curl -X GET https://wbsrch.com/api/domain_pages_in_index/?domain=stampscoinsnotes.com -H 'Authorization: Token ed740e11d3f0e7383d1c7a05a204d6c5f9c501d6'
echo
curl -X GET https://wbsrch.com/api/domain_keywords_ranked/?domain=zetacentauri.com -H 'Authorization: Token ed740e11d3f0e7383d1c7a05a204d6c5f9c501d6'
echo
curl -X GET https://wbsrch.com/api/domain_keywords_ranked/?domain=freewavesamples.com -H 'Authorization: Token ed740e11d3f0e7383d1c7a05a204d6c5f9c501d6'
echo
curl -X GET https://wbsrch.com/api/domain_keywords_ranked/?domain=stampscoinsnotes.com -H 'Authorization: Token ed740e11d3f0e7383d1c7a05a204d6c5f9c501d6'
echo
