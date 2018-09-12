import get_token, requests, json, sys
from get_token import get_token

bibid = sys.argv[1]
#pass along argument when running python scripts from autoit

def bib(bibid):
    token_param = get_token()


    url = 'https://holmes.lib.miamioh.edu:443/iii/sierra-api/v4/bibs/marc?'

    querystring = {"id": {bibid}}  # full number is b4530689a minus b and final check digit a

    headers = {
        'authorization': str(token_param),
        'cache-control': "no-cache",
        'postman-token': "715478e1-10c5-8bc7-7758-415c1be73131",
        'content-type': "application/json"
    }

    response = requests.get(url, headers=headers, params=querystring)

    bib_data = response.json()

    bib_url = bib_data["file"]

    marc_response = requests.get(bib_url, headers=headers)

    print(marc_response.text)

print(bibid)
bib(bibid)
