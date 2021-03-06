import get_token, requests, json
from get_token import get_token


def patron():
    token_param = get_token()

    url = "https://holmes.lib.miamioh.edu:443/iii/sierra-api/v4/patrons"

    querystring = {"id": "1306450"}  # full number is p4530689a minus p and final check digit a

    headers = {
        'authorization': str(token_param),
        'cache-control': "no-cache",
        'postman-token': "715478e1-10c5-8bc7-7758-415c1be73131",
        'content-type': "application/json"
    }

    response = requests.get(url, headers=headers, params=querystring)

    patron_data = response.json()
