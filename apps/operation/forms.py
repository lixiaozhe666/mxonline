# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/04/12 19:12'
from django import forms
from .models import UserAsk
class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name','mobile','course_name']