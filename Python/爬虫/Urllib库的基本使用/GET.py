import urllib.request,urllib

values = {'username':'490216194@qq.com','password':'490216194'}
data = urllib.parse.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + '?' + data
request = urllib.request.Request(geturl)
response = urllib.request.urlopen(request)
print(response.read())
print('\n\n\n')
print(response.geturl())