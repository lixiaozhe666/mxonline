# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/04/12 19:20'
from django.conf.urls import url,include
from .views import TestView,AddAskView

urlpatterns = [
    url(r'^list/$', TestView.as_view(), name='ora_list'),
    url(r'^add_ask/$', AddAskView.as_view(), name='add_ask')
]