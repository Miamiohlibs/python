import get_token, requests, json, sys, urllib, os, objectpath
from get_token import get_token
from urllib.parse import urlparse

BARCODE = sys.argv[1]

def barcode(BARCODE):
    token_param = get_token()



    url = "https://holmes.lib.miamioh.edu:443/iii/sierra-api/v4/items/query?offset=0&limit=100"

    querystring = {
  "queries": [
          {
            "target": {
                "record": {
                "type": "item"
                 },
                "field": {
                   "tag": "b"
                   }
                },
                "expr": {
                 "op": "equals",
                 "operands": [
                  BARCODE,
                  ""
                 ]
               }
             }
          ]
        }


    headers = {
        'authorization': str(token_param),
        'cache-control': "no-cache",
        'postman-token': "715478e1-10c5-8bc7-7758-415c1be73131",
        'content-type': "application/json"
    }

    response = requests.post(url, headers=headers, json=querystring)

    entry = response.json()['entries']

    ##parse nested json array entry containing link, removing only url dir path
    dir = urlparse(entry[0]["link"]).path
    ## splits dir into head and tail, leaving item record id in [1]
    id = os.path.split(dir)[1]

    print(id)

##response = requests.get(url, headers=headers, params=querystring)

##    marc_response = requests.get(bib_url, headers=headers)

##    print(marc_response.text)

print(BARCODE)
barcode(BARCODE)
