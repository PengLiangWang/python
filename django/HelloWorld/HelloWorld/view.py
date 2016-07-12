#! /usr/bin/python2.6
#! coding=utf-8

#from django.http import HttpResponse
from django.shortcuts import render     #用于向模块提交数据

def hello(request):
    context = {}
    context['hello'] = 'Hello World'
    return render(request, 'hello.html', context)  #字典context作为参数, hello对应了模块中的"{{hello}}"
