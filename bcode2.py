import get_token, requests, json, objectpath, sys
from get_token import get_token

bibid = sys.argv[1]
#pass along argument when running python scripts from autoit
#sys.argv causes interactive python to fail to import bcode2.py; but it works fine

#to return bcode2 as an autoit variable
def bcode2(bibid):
    token_param = get_token()

    url = "https://holmes.lib.miamioh.edu:443/iii/sierra-api/v4/bibs/?"

    querystring = {"id": {bibid}}  # full number is b4530689a minus b and final check digit a

    headers = {
        'authorization': str(token_param),
        'cache-control': "no-cache",
        'postman-token': "715478e1-10c5-8bc7-7758-415c1be73131",
        'content-type': "application/json"
    }

    response = requests.get(url, headers=headers, params=querystring)

    bib_data = response.json()

    json_tree = objectpath.Tree(bib_data['entries'])

    matType = tuple(json_tree.execute('$.materialType'))[0]

    return matType['code']
    print( matType['code'])

bcode2(bibid)
