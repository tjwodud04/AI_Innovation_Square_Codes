<<<<<<< HEAD
import requests
import json

resp = requests.request("get", "http://httpbin.org/get", params={"key":"value"})
print(resp.status_code, "\n", resp.headers, "\n", resp.content, "\n")

# resp = requests.request("post", "http://httpbin.org/post", data={"key":"value"})
# print(resp)

=======
import requests
import json

resp = requests.request("get", "http://httpbin.org/get", params={"key":"value"})
print(resp.status_code, "\n", resp.headers, "\n", resp.content, "\n")

# resp = requests.request("post", "http://httpbin.org/post", data={"key":"value"})
# print(resp)

>>>>>>> 125e15a4c5fcf711dd279c9b18e149867466699e
result = json.loads(resp.content)