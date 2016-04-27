import urllib,urllib.request

url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
values = {'username':'490216194@qq.com','password':'490216194'}
headers = {'User_Agent':user_agent}#'Referer':'http://www.zhihu.com/articles'
data = urllib.parse.urlencode(values).encode(encoding='UTF-8')
request = urllib.request.Request(url,data,headers)
response = urllib.request.urlopen(request)
page = response.read()
print(page)
print(response.geturl())