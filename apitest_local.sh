#!/bin/bash
# You'll want to replace the token in this file with the one auto-generated in your admin.
echo Domain Link Rank
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=youporn.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=www.tacobell.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=facebook.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=apple.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=google.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=linkedin.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=pinterest.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=youtube.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=twitter.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=zetacentauri.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=freewavesamples.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=soundprogramming.net -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
echo IP To Country
curl -X GET http://localhost:8000/api/ip_to_country/?ip=216.151.17.10 -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
echo Domain Pages In Index
curl -X GET http://localhost:8000/api/domain_pages_in_index/?domain=xangis.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_pages_in_index/?domain=bloodlessmushroom.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_pages_in_index/?domain=youtube.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_pages_in_index/?domain=instagram.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_pages_in_index/?domain=pinterest.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_pages_in_index/?domain=kickstarter.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
echo Domain Keywords Ranked
curl -X GET http://localhost:8000/api/domain_keywords_ranked/?domain=sashaandthechildren.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_keywords_ranked/?domain=rainwithoutend.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_keywords_ranked/?domain=indiegogo.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/domain_keywords_ranked/?domain=facebook.com -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET "http://localhost:8000/api/domain_keywords_ranked/?domain=bild.de&lang=de" -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET "http://localhost:8000/api/domain_keywords_ranked/?domain=free.fr&lang=fr" -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
echo Autocomplete
curl -X GET http://localhost:8000/api/autocomplete/?q=th -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/autocomplete/?q=davi -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
echo Check Typo
curl -X GET http://localhost:8000/api/check_typo/?q=listenin -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
curl -X GET http://localhost:8000/api/check_typo/?q=erfume -H 'Authorization: Token af5d375f478eb35a23c39de002fd4ff479efc80a'
echo
