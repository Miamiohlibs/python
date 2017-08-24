import requests
import pymarc
from pymarc import MARCReader

url = "https://holmes.lib.miamioh.edu:443/iii/sierra-api/v4/bibs/"

querystring = {"id":"4530689"}

headers = {
    'authorization': str(token_param),
    'cache-control': "no-cache",
    'postman-token': "715478e1-10c5-8bc7-7758-415c1be73131"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)