#! /usr/bin/python2.6
#! coding=utf-8

import json

info={}
info["code"]=1
info["id"]=1900
info["name"]='Alex'
info["sex"]='nan'
info["text"]=None


JsonStr =  json.dumps(info)

print "JsonStr: ", JsonStr
