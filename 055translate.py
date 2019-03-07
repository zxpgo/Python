import urllib.request
import json
import urllib.parse

url =  "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
data = {}
head= {}
head['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"

data['i'] =  "I love"
data['from'] = "AUTO"
data['to'] = "AUTO"
data['smartresult'] = "dict"
data['client'] = "fanyideskweb"
data['salt'] = "1507538690679"
data['sign'] = "064eb1df7a827289ecad455714c4d2c5"
data['doctype'] = "json"
data['version'] = "2.1"
data['keyfrom'] = "fany.web"
data['action'] = "FY_BY_REALTIME"
data['typoResult'] = "true" 

data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, data, head)
respone = urllib.request.urlopen(req)
#respone = urllib.request.urlopen(url, data)
html = respone.read().decode("utf-8")

