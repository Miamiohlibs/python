import get_token, requests, json
from get_token import get_token

def bib():

token_param = get_token()

url = "https://holmes.lib.miamioh.edu:443/iii/sierra-api/v4/bibs/marc?"

querystring = {"id":"4530689"}

headers = {
    'authorization': str(token_param),
    'cache-control': "no-cache",
    'postman-token': "715478e1-10c5-8bc7-7758-415c1be73131"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

bib_data = response.json()

bib_url = bib_data["file"]

marc_response = requests.request("GET", bib_url, headers=headers)