'''
Created on 2011-5-24

@author: wangyaoyao
'''

import datetime
import urllib.request

def chkqq(qqnum):
    chkurl = 'http://wpa.qq.com/pa?p=1:{}:1'.format(qqnum)
    page = urllib.request.urlopen(chkurl)
    length = page.headers.get('content-length')
    page.close()
    print(datetime.datetime.now())
    if length == '2329':
        return 'Online'
    elif length == '2262':
        return 'Offline'
    else:
        return 'Unknown Status!'

def main():
    print(chkqq(904312667))
    print(chkqq(435515401))

if __name__ == '__main__': main()