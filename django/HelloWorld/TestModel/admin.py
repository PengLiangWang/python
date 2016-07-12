# -*- coding:utf-8 -*-
#让admin界面管理某个数据模型
from django.contrib import admin
from TestModel.models import Test, Contact, Tag

# Register your models here.
admin.site.register([Test, Contact, Tag])
