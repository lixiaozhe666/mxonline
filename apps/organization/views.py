# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from .models import Organization,CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from operation.forms import UserAskForm
# Create your views here.


class TestView(View):
    def get(self,request):
        all_org = Organization.objects.all()

        all_city = CityDict.objects.all()
        hot_org = Organization.objects.order_by("-click_nums")[:3]

        city_id = request.GET.get('city','')
        sort  = request.GET.get('sort','')
        ct = request.GET.get('ct', '')
        if city_id:
            all_org = Organization.objects.filter(city_id=int(city_id))
        if ct:
            all_org = Organization.objects.filter(category=ct)

        if sort:
            if sort =="students":
                all_org = Organization.objects.order_by("-student")
            else:
                all_org = Organization.objects.order_by("-course_num")
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_org , request=request,per_page=3)

        orgs = p.page(page)
        org_nums = all_org.count()
        return  render(request,'org-list.html',{
            "all_org":orgs,
            "all_city":all_city,
            "org_nums":org_nums,
            "city_id":city_id,
            "category":ct,
            "hot_org":hot_org,
            "sort":sort
        })


class AddAskView(View):
    def post(self,request):
        useraskForm = UserAskForm(request.POST)
        if useraskForm.is_valid():
            userask = useraskForm.save(commit=True)
            return HttpResponse("{'status':'success'}",content_type='application/json')
        else:
            return HttpResponse("{'status':'fail' , 'msg':'111'}",content_type='application/json')


