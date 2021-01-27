from urllib import parse
import requests
import json
from requests.utils import quote, unquote

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}

def download(url, params={}, retries=3):
    resp = None

    try:
        resp = requests.get(url, params=params, headers = header)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if 500 <= e.response.status_code < 600 and retries > 0:
            print(retries)
            resp = download(url, params, retries-1)
        else:
            print("status_code: ", e.response.status_code, "\n")
            print("response reason: ", e.response.reason, "\n")
            print("headers: ", e.request.headers, "\n")

    return resp

url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
params = {
    "serviceKey": "SOiHe0eIo6uoLf60XK0keAAwBXmx33hU4bEEdZZ0rYoCbbWRYswGsk2JdpJsUcHRQbvdp0ACEbmu5YcpfiJcKw%3D%3D",
    "numOfRows": 10,
    "pageNo": 1,
    "sidoName": "경기",
    "ver": 1.3,
    "_returnType": "json"
}

result = download(url, params)
print("result text: ", result.text, "\n")
print("result url: ", result.url, "\n")

#params["serviceKey"] = unquote(params["serviceKey"])
#quote(unquote(params["serviceKey"]))
org = requests.utils.unquote(params["serviceKey"])
params['serviceKey'] = org
result = download(url, params)
result = json.loads(result.text)
print("result: ", result)

for row in result['list']:
    print("동이름: ",row['stationName'], "/", "미세먼지 농도: ",row['pm25Value'], "/", "통합대기 등급: ", row['khaiGrade'])