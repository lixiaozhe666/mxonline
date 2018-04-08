"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include

from django.views.generic import TemplateView
import xadmin
from users.views import LoginView,RegisterView,UserActivateView,ForgetPwdView,ResetPasswordView,Modify_pwdView
from organization.views import TestView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$',TemplateView.as_view(template_name='index.html'),name = 'index'),
    # url('^login/$', user_login,name ='login'),
    url('^login/$', LoginView.as_view(),name ='login'),
    url('^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<activate_code>.*)/$',UserActivateView.as_view(),name='active'),
    url(r'^forget/$',ForgetPwdView.as_view(),name='forget'),
    url(r'^reset/(?P<activate_code>.*)/$', ResetPasswordView.as_view(), name='reset'),
    url(r'^modify/$', Modify_pwdView.as_view(), name='modify'),
    url(r'^ora/$', TestView.as_view(), name='ora'),

]
