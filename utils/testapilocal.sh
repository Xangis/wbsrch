#!/bin/bash
# This is meant for testing API calls on the local machine. If your local token doesn't match, either replace it in this file,
# or add it manually.
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=youporn.com -H 'Authorization: Token e359fc54f273955db5a2d8db531fbd7b2767c65d'
echo
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=http://www.tacobell.com -H 'Authorization: Token e359fc54f273955db5a2d8db531fbd7b2767c65d'
echo
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=searchengineland.com -H 'Authorization: Token e359fc54f273955db5a2d8db531fbd7b2767c65d'
echo
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=http://youtube.com -H 'Authorization: Token e359fc54f273955db5a2d8db531fbd7b2767c65d'
echo
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=arstechnica.com -H 'Authorization: Token e359fc54f273955db5a2d8db531fbd7b2767c65d'
echo
curl -X GET http://localhost:8000/api/domain_link_rank/?domain=www.zetacentauri.com -H 'Authorization: Token e359fc54f273955db5a2d8db531fbd7b2767c65d'
echo
curl -X GET http://localhost:8000/api/ip_to_country/?ip=216.151.17.10 -H 'Authorization: Token e359fc54f273955db5a2d8db531fbd7b2767c65d'
echo
curl -X GET http://localhost:8000/api/domain_pages_in_index/?domain=zetacentauri.com -H 'Authorization: Token e359fc54f273955db5a2d8db531fbd7b2767c65d'
echo
curl -X GET http://localhost:8000/api/domain_pages_in_index/?domain=freewavesamples.com -H 'Authorization: Token e359fc54f273955db5a2d8db531fbd7b2767c65d'
echo
curl -X GET http://localhost:8000/api/domain_pages_in_index/?domain=stampscoinsnotes.com -H 'Authorization: Token e359fc54f273955db5a2d8db531fbd7b2767c65d'
echo
curl -X GET http://localhost:8000/api/domain_keywords_ranked/?domain=zetacentauri.com -H 'Authorization: Token e359fc54f273955db5a2d8db531fbd7b2767c65d'
echo
curl -X GET http://localhost:8000/api/domain_keywords_ranked/?domain=freewavesamples.com -H 'Authorization: Token e359fc54f273955db5a2d8db531fbd7b2767c65d'
echo
curl -X GET http://localhost:8000/api/domain_keywords_ranked/?domain=stampscoinsnotes.com -H 'Authorization: Token e359fc54f273955db5a2d8db531fbd7b2767c65d'
echo
