#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib3 import PoolManager
from http_header import *

class HttpClientWithUA(PoolManager):
    def __init__(self, host='www.baidu.com', refer='https://www.baidu.com/', **kw):
        PoolManager.__init__(self, **kw)
        self.headers = {
            'User-Agent': define_user_agent(),
            'X-Forward-For': define_x_forward(), 
            'Host': host,
            'Referer': refer,
            'Accept': HDR_ACCEPT,
            'Accept-Encoding': HDR_ACCEPT_ENCODING,
            'Accept-Language': HDR_ACCEPT_LANG,
            'Cache-Control': HDR_CACHE_CONTROL,
            'Connection': HDR_CONN,
            'If-Modified-Since': HDR_LAST_MOD
        }

    def request(self, meth, url, fields=None, **kw):
        return super(HttpClientWithUA, self)\
                .request(meth, url, fields,
                         headers=self.headers, **kw)

class NovelOutlineHelper(HttpClientWithUA):
    pass

class ChapterDLHelper(HttpClientWithUA):
    pass

class NovelCategoryHelper(HttpClientWithUA):
    pass

if __name__ == "__main__":
    # import pdb; pdb.set_trace()
    client = HttpClientWithUA(host='www.xbiquge.la', refer='http://www.xbiquge.la')
    resp = client.request('GET', 'http://www.xbiquge.la/0/52/')
    print resp.status, resp.data
