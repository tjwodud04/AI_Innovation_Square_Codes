#resp = response
import requests

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}
resp = requests.get("https://www.google.com/search", params={"q":"박보영"}, headers = header)

print(resp.status_code)
print(resp.reason)
print(resp.headers)
print(resp.content)
print(resp.encoding)
resp.encoding = "utf-8"
print(resp.text)

