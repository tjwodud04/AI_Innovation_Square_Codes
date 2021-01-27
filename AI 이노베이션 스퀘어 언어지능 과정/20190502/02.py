<<<<<<< HEAD
import requests
from urllib import request, error, parse

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}

def download(url, params={}, retries=3):
    resp = None

    try:
        resp = requests.get(url, params=params, headers = header)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if 500 <= e.response.status_code < 600 and retries > 0:
            print(retries)
            resp = download(url, params, retries - 1)
        else:
            print(e.response.status_code, "\n")
            print(e.response.reason, "\n")
            print(e.request.headers, "\n")

    return resp

#html = download("http://httpbin.org/get", {"Key":"Value"})
html = download("https://www.crawler-test.com/status_codes/status_500")
#print(html.text, html.content)

#print("https://www.crawler-test.com/status_codes/status_숫자")
# &_returnType=json (json 반환 , 웹 뒤에 붙여 쓰면 됨)
# 웹 페이지 헤더 확인하기 (계속)
=======
import requests
from urllib import request, error, parse

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}

def download(url, params={}, retries=3):
    resp = None

    try:
        resp = requests.get(url, params=params, headers = header)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if 500 <= e.response.status_code < 600 and retries > 0:
            print(retries)
            resp = download(url, params, retries - 1)
        else:
            print(e.response.status_code, "\n")
            print(e.response.reason, "\n")
            print(e.request.headers, "\n")

    return resp

#html = download("http://httpbin.org/get", {"Key":"Value"})
html = download("https://www.crawler-test.com/status_codes/status_500")
#print(html.text, html.content)

#print("https://www.crawler-test.com/status_codes/status_숫자")
# &_returnType=json (json 반환 , 웹 뒤에 붙여 쓰면 됨)
# 웹 페이지 헤더 확인하기 (계속)
>>>>>>> 125e15a4c5fcf711dd279c9b18e149867466699e
