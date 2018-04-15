# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/04/12 19:12'
from django import forms
from .models import UserAsk

import  re
class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name','mobile','course_name']

    def clean_mobile(self):#验证手机字段是否合法
        mobile = self.cleaned_data["mobile"]
        regex = "^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$"
        p =re.compile(regex)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机格式错误","mobile_invalid")