import json, requests, urllib3, get_bass, base64
from get_bass import get_bass
##sample get_bass https://github.com/Miamiohlibs/python/blob/master/get_bass_template.py

def get_token():
    bass = get_bass()
    url = 'https://holmes.lib.miamioh.edu:443/iii/sierra-api/v4/token'
    payload = {'grant_type': 'client_credentials'}
    headers = {'authorization': 'Basic ' + str(bass)}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    mytoken = r.json()['token_type']
    mytokentype = r.json()['access_token']
    token_param = str(mytoken) + ' ' + str(mytokentype)
    return token_param
