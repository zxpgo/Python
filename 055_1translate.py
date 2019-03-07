import urllib.request
import json
import urllib.parse

head = {}
head['User-Agent'] =  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc'
data ={
    "type" : "AUTO",
     "i" : 'sentence',
    "doctype" : "json",
    "xmlVersion" : "1.8",
    "keyfrom" : "fanyi.web",
    "ue" : "UTF-8",
    "action" : "FY_BY_CLICKBUTTON",
    "typoResult" : "true"
    }


data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, data, head)
respone = urllib.request.urlopen(req)
#respone = urllib.request.urlopen(url, data)
html = respone.read().decode("utf-8")
