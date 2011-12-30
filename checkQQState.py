#!/usr/bin/env python
import time,datetime
import urllib2

def chk_qq(qqnum):
    chkurl = 'http://wpa.qq.com/pa?p=1:'+`qqnum`+':1'
    a = urllib2.urlopen(chkurl)
    length=a.headers.get("content-length")
    a.close()
    print datetime.datetime.now()
    if length=='2329':
        return 'Online'
    elif length=='2262':
        return 'Offline'
    else:
        return 'Unknown Status!'

def main():
    while True:
        num = raw_input("Input the qq num: ")
        if num == "q":
            return 0
        print(chk_qq(num))

if __name__ == '__main__':
	main()
