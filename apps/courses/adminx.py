# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/03/15 20:09'

import  xadmin

from .models import Course
from .models import Lessons
from  .models import Videos
from .models import CourseResource


class CourseAdmin(object):
    list_display =['name','add_time']
    search_fileds = ['name']
    list_filter =['name','add_time']


class LessonsAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fileds = ['course', 'name']
    list_filter = ['course', 'name',  'add_time']


class VideosAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fileds = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fileds = ['course', 'name']
    list_filter = ['course', 'name', 'add_time']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register( Lessons, LessonsAdmin)
xadmin.site.register( Videos, VideosAdmin)
xadmin.site.register( CourseResource, CourseResourceAdmin)

