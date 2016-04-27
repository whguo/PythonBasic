import urllib.request

response = urllib.request.urlopen('http://www.hupu.com',timeout = 10)
print(response.read())