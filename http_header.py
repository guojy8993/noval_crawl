#!/usr/bin/env python
import random

UAs = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',  # Chrome
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',  # IE
'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',  # Firefox/win
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.0; rv:42.0) Gecko/20170101 Firefox/42.0', # Firefox/macos
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50', # Safari
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)', # QQ
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',  # 360
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',  # Sougo
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',  # AoYou
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41' # Opera 
]

Refers = [
'https://www.baidu.com/',     # Baidu
'https://www.sogou.com/',     # Sougou
'https://www.so.com/',        # 360
'https://www.google.com.hk/', # Google - hk
'https://www.google.com.jp/', # Google - jp
'https://www.google.com.sg/', # Google - sg
'https://cn.bing.com/',       # Bing
'https://global.bing.com/'    # Bing
]

def _define_x_forward():    
    return '.'.join([ '%s' % random.randint(1, 254) for i in range(4) ])

def _define_user_agent():
    return random.choice(UAs)

def _define_refer():
    return random.choice(Refers)

if __name__ == "__main__":
    print _define_x_forward(), _define_user_agent(), _define_refer()
