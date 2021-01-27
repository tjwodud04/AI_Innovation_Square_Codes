from urllib import request, error, parse

url = ('https://www.google.com/search?q=박보영')
req = request.Request(url,
                      headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"},
                      method="GET")
parse.urlencode({'q':'박보영'})

# try:
#     resp = request.urlopen(req)
# except error.HTTPError as e:
#     print(e.code)
#     print(e.reason)
#     print(e.headers)
    #print(e.request.headers)

# resp.geturl()
# resp.getcode()
# resp.getheaders()
#403 error -> 접근 권한이 없는데 요청함
# resp.geturl()
# resp.getcode()
# resp.getheaders()
