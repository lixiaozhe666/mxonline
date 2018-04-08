# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/03/15 19:24'

import xadmin
from xadmin import  views

from .models import EmailVerifyRecord

from  .models import Banner


class BaseSetting(object):
    enable_themes = True;
    use_bootswatch =True;


class GlobalSettings(object):
    site_title='莫学管理系统'
    site_footer ='暮雪在线网'
    menu_style = 'accordion' #可伸展

class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']


class BannerAdmin(object):
    list_display = ['title', 'url', 'index', 'add_time']
    search_fields = ['title', 'url', 'index']
    list_filter = ['title', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)

xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
