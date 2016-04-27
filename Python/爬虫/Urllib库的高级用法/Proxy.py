import urllib.request

enable_proxy = True
proxy_handler = urllib.request.ProxyHandler({"http":"http://some-proxy.com:8080"})#输入代理的地址
null_proxy_handler = urllib.request.ProxyHandler({})
if enable_proxy:
	opener = urllib.request.build_opener(proxy_handler)
else:
	opener = urllib.request.build_opener(null_proxy_handler)
urllib.request.install_opener(opener)

response = urllib.request.urlopen("http://www.baidu.com")
print(response.read())