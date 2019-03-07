import urllib.request

respone = urllib.request.urlopen("http://placekitten.com/g/500/600")
cat_img = respone.read()

with open("cat_500_600.jpg", 'wb') as f:
    f.write(cat_img)
