# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/03/15 20:34'
import  xadmin

from  .models import CityDict
from  .models import Teacher
from  .models import Organization


class CityDictAdmin(object):
    list_display=['name','desc','add_time']
    search_fields=['name']
    list_filter = ['name','add_time']


class TeacherAdmin(object):
    list_display = ['name', 'work_company', 'org','add_time']
    search_fields = ['name', 'work_company', 'org']
    list_filter = ['name', 'work_company', 'org','add_time']


class OrganizationAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'add_time']


xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
xadmin.site.register(Organization,OrganizationAdmin)