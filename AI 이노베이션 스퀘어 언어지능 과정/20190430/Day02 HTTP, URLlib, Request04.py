from urllib import parse

result = parse.urlparse("https://www.google.com/search/q=%EB%B0%95%EB%B3%B4%EC%98%81'")
print([_ for _ in result])

#parse.urlenconde("박보영")
print(parse.quote("박보영"))
print(parse.quote_plus("박보영"))
print(parse.unquote('q=%EB%B0%95%EB%B3%B4%EC%98%81'))