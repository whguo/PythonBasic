import urllib.request

request = urllib.request.Request("http://www.baidu.com")
#response = urllib.request.urlopen("http://www.baidu.com")
response = urllib.request.urlopen(request)
print (response.read())