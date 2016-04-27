import urllib.request

httpHandler = urllib.request.HTTPHandler(debuglevel = 1)
httpsHandler = urllib.request.HTTPSHandler(debuglevel = 1)
opener = urllib.request.build_opener(httpHandler,httpsHandler)
urllib.request.install_opener(opener)
response = urllib.request.urlopen("http://www.baidu.com")
print (response.read())