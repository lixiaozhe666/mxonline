# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/03/19 19:54'
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True,)
    password = forms.CharField(required=True,)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True,)
    password = forms.CharField(required=True,)
    captcha =CaptchaField(error_messages={'invalid':u'验证码错误'},)


class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True,)
    captcha =CaptchaField(error_messages={'invalid':u'验证码错误'},)


class ResetPwdForm(forms.Form):
    password1 = forms.CharField(required=True,)
    password2 = forms.CharField(required=True,)
