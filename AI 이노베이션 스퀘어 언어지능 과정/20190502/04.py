<<<<<<< HEAD
import requests

#header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}

url = "https://pythonscraping.com/pages/files/processing.php"

def download(url, params={}, retries=3):
    resp = None

    try:
        resp = requests.get(url, params=params)#headers = header)
        #resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if 500 <= e.response.status_code < 600 and retries > 0:
            print(retries)
            resp = download(url, params, retries - 1)
        else:
            print(e.response.status_code, "\n")
            print(e.response.reason, "\n")
            print(e.request.headers, "\n")

    return resp

#html = download(url, {"firstname":"1234", "lastname":"1234"})
html = requests.post(url,{"firstname":"1234", "lastname":"1234"} )
print(html.request.headers)

print(html.request.body)
=======
import requests

#header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}

url = "https://pythonscraping.com/pages/files/processing.php"

def download(url, params={}, retries=3):
    resp = None

    try:
        resp = requests.get(url, params=params)#headers = header)
        #resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if 500 <= e.response.status_code < 600 and retries > 0:
            print(retries)
            resp = download(url, params, retries - 1)
        else:
            print(e.response.status_code, "\n")
            print(e.response.reason, "\n")
            print(e.request.headers, "\n")

    return resp

#html = download(url, {"firstname":"1234", "lastname":"1234"})
html = requests.post(url,{"firstname":"1234", "lastname":"1234"} )
print(html.request.headers)

print(html.request.body)
>>>>>>> 125e15a4c5fcf711dd279c9b18e149867466699e
print(html.text)