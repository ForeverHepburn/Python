import urllib
url = 'https://www.baidu.com/s?wd=cloga'
html = urllib.urlopen(url).read()
print(html)