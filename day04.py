'''
import requests
def html(url):
    html = requests.get(url)
    print(html.test)
html("url")
'''
'''
def AGS(*aa):
    print(aa)
AGS(1,2,5,8,32,45,4)
'''

def KWargs(**kwargs):
   print(kwargs)
KWargs(a='42',b='54',c='72')
