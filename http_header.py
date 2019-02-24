#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

UAs = [
'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',  # Firefox/win
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.0; rv:42.0) Gecko/20170101 Firefox/42.0', # Firefox/macos
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50', # Safari
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

HDR_ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
HDR_ACCEPT_ENCODING = 'gzip, deflate'
HDR_ACCEPT_LANG = 'zh-CN,zh;q=0.9'
HDR_CACHE_CONTROL = 'max-age=0'
HDR_CONN = 'keep-alive'
HDR_LAST_MOD = 'Mon, 25 Feb 2010 13:08:34 GMT'

def define_x_forward():    
    return '.'.join([ '%s' % random.randint(1, 254) for i in range(4) ])

def define_user_agent():
    return random.choice(UAs)

def define_refer():
    return random.choice(Refers)
