#!/usr/bin/env python
# coding=utf-8

import sys
import hashlib
import urlparse
reload(sys)
sys.setdefaultencoding('utf-8')

def md5(mess): # Function md5()
    m2 = hashlib.md5()
    m2.update(mess)
    return str(m2.hexdigest())


def urlFilter(url): # Filter URL
    u_scheme = urlparse.urlparse(url).scheme
    if u_scheme == '':
        u_scheme = 'http'
        u_domin = str(urlparse.urlparse(url).path)
    else:
        u_scheme = str(u_scheme)
        u_domin = str(urlparse.urlparse(url).netloc)
    return u_scheme, u_domin


def mkdir(url):
    pass

