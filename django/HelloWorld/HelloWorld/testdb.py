#! coding=utf-8

from django.http import HttpResponse
from TestModel.models import Test

# 数据库操作
""" 向数据库添加数据(测试1)
def testdb(request):
    test1 = Test(name='wpltest')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
"""

#获取数据库内容
def testdb(request):
    #初始化
    response = ""
    response1 = ""

    
    #通过objects模型管理器的all()获取所有数据行, 相当于SQL中的select * from
    list = Test.objects.all()

    #filter相当于SQL中的where
    response2 = Test.objects.filter(id=3)

    #获取单个对象
    response3 = Test.objects.get(id=1)

    #限制返回的数据 相当于OFFSET 0 LIMIT 2;
    response4 =  Test.objects.order_by('name')[0:2]

    #数据排序
    response5 = Test.objects.order_by("id")

    #上面方法可以连锁使用
    response6 = Test.objects.filter(name="w3cschool.cc").order_by("id")

    #输出所有数据
    for var in response6:
        response1 += var.name + "\n"
    response = response1
    return HttpResponse("<p>" + response + "</p>")
