# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from .models import Organization,CityDict
# Create your views here.


class TestView(View):
    def get(self,request):
        all_org = Organization.objects.all()
        org_nums =all_org.count()
        all_city = CityDict.objects.all()
        return  render(request,'org-list.html',{
            "all_org":all_org ,
            "all_city":all_city,
            "org_nums":org_nums
        })