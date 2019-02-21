#imports bib records file from sierra api and writes to working directory
import sys

#allows receiving of date variable through CLI;
#currently not working 2019-02-21
#date = sys.argv[1]

def bib(date):
    import get_token, requests, json, urllib3
    from get_token import get_token

    url = "https://lib.caturl.edu/iii/sierra-api/v5/bibs/marc?createdDate="+date

    headers = {
        'authorization': str(get_token()),
        'cache-control': "no-cache",
        'postman-token': "715478e1-10c5-8bc7-7758-415c1be73131",
        'content-type': "application/json"
    }
    #retrieve file download link
    try:
        response = requests.get(url, headers=headers)
        data_url = response.json()['file']
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
    #download marc records file
    try:
        marc = requests.get(data_url, headers=headers)
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)

    #save marc file
    f = open(date+".mrc", "w")
    f.write(marc.text)
    f.close()
