import urllib.request

req=urllib.request.Request('http://placekitten.com/500/600')
response=urllib.request.urlopen(req)
cat_img=response.read()

with open('cat_500_600.jpg','wb') as f:
    f.write(cat_img)
