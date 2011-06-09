'''
Created on 2011-5-24

@author: wangyaoyao
'''

import urllib.parse
import urllib.request
import re

def getTranslateHtml(text):
    values = {'hl':'zh-CN', 'ie':'utf8', 'text':text, 'langpair':"en|zh-CN"}
    url = 'http://translate.google.cn/#'
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(url, data)
    req.add_header('User-Agent', "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)")
    response = urllib.request.urlopen(req)
    return response.read().decode('utf-8')

def getTranslateText(html):
    rettxt = ""
    m = re.search(r'<span id=result_box.*?><span .*?>.*?</span></span>', html)
    if m:
        rettxt = re.sub('</?span.*?>', '', m.group(0))
    return rettxt


def main():
    while True:
        text = input('Enter translate text(q exit):')
        if text == 'q':
            break
        print(getTranslateText(getTranslateHtml(text)))

if __name__ == '__main__':
	main()
