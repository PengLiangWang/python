#! coding=utf-8
"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import *
from HelloWorld.view import hello
from HelloWorld.testdb import testdb
from HelloWorld import search
from HelloWorld import search2



urlpatterns = patterns("", 
                ('^wpl/test/$', hello),
                ('^wpl/testdb/$', testdb),
                (r'^search-form/$', search.search_form),
                (r'^search/$', search.search),
                (r'^search-post/$', search2.search_post),
                (r'^admin/', include(admin.site.urls)),
                )
