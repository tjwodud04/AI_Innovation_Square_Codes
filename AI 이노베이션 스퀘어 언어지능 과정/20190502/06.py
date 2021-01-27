import requests

#header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}

url = " http://timetime.kr/user/login"

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

html = requests.post(url,{"username":"donddog", "password":"12345678"} )

print(html.text)