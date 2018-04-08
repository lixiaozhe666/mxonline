# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.


class TestView(View):
    def get(self,request):
        return  render(request,'org-list.html')