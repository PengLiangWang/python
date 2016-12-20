#! /usr/bin/env python
#! coding=utf-8

import re

pattern = re.compile(r'world')

#如果使用match将无法匹配到
search = re.search(pattern, "hello world!")

if search:
    print search.group()
