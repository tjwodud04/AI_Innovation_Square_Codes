from urllib import request, error, parse

#url = ('https://www.google.com/search?q=박보영')
#parse.urlencode({'q':'박보영'})
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}

def download(url, params={}, retries=3):
    resp = None

    try:
        req = request.Request(url + "?" + parse.urlencode(params), headers = header)
        #req.add_header("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36")
        resp = request.urlopen(req)
    except error.HTTPError as e:
        if 500 <= e.code < 600 and retries > 0:
            resp = download(url, params, retries=1)
        else:
            print(e.code)
            print(e.reason)
            print(e.geturl())
            print(e.headers)

    return resp

params = {"q":"박보영"}
parse.urlencode(params)
resp = download("https://www.google.com/search", params)

#resp.read()
print(resp.read().decode('utf-8'))
