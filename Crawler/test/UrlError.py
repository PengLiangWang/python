#! /usr/bin/env python
# encoding=utf-8

import urllib2
requset = urllib2.Request('http://www.123456.com')
try:
    urllib2.urlopen(requset)
except urllib2.URLError, e:
    print e.reason
    
