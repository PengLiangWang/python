# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.context_processors import csrf


# search.py中 使用的是GET方法, 视图显示和请求处理分成两个函数处理.
# 提交数据时更常用POST方法

def search_post(request):
    ctx = {}
    ctx.update(csrf(request))
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
