# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/03/15 20:22'
import xadmin

from .models import UserAsk
from .models import UserMessage
from .models import CourseComment
from .models import UserFavourite
from .models import UserCourse


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'has_read', 'add_time']
    search_fields = ['user', 'has_read']
    list_filter = ['user', 'has_read', 'add_time']


class CourseCommentAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


class UserFavouriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavourite, UserFavouriteAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
