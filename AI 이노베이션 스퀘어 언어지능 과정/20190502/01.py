import requests
import json

resp = requests.request("get", "http://httpbin.org/get", params={"key":"value"})
print(resp.status_code, "\n", resp.headers, "\n", resp.content, "\n")

# resp = requests.request("post", "http://httpbin.org/post", data={"key":"value"})
# print(resp)

result = json.loads(resp.content)