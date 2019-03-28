# use list of isbns to return list of bib record numbers

import get_token, requests, json, sys, urllib, os, objectpath
from get_token import get_token
 #sample get_token https://github.com/Miamiohlibs/python/blob/master/get_token_template.py

from urllib.parse import urlparse

BARCODE = sys.argv[1]

##to accept barcode and convert it into an item ID
def eisbn(ISBN):
token_param = get_token()
url = "https://lib.cat.edu:443/iii/sierra-api/v4/bibs/query?offset=0&limit=100"

querystring = {
  "queries": [
          {"target": {
                "record": {"type": "bib"},
                "field": {"tag": "i"}
                },
                "expr": {"op": "equals",
                 "operands": [ISBN]
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

print(BARCODE)
barcode(BARCODE)
