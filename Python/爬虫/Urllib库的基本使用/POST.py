import urllib,urllib.parse,urllib.request

values = {'username':'490216194@qq.com','password':'490216194'}
data = urllib.parse.urlencode(values).encode(encoding='UTF-8')
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib.request.Request(url,data)
response = urllib.request.urlopen(request)
print(response.read())
print(response.geturl())
