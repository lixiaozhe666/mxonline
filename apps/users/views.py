# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import  authenticate,login
from django.contrib.auth.backends import ModelBackend
from  django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.views.generic.base import View
from .models import userProfile,EmailVerifyRecord
from .forms import LoginForm,RegisterForm,ForgetPwdForm,ResetPwdForm
from utils.email_send import send_register_email
# Create your views here.


class UserActivateView(View):
    def get(self,request,activate_code):

        all_record = EmailVerifyRecord.objects.filter(code=activate_code)

        if all_record:
            email = all_record.email
            user_record = userProfile.objects.get(email=email)
            user_record.is_active = True
            user_record.save()
            return render(request, "login.html")
        else:
            return render(request, "activeFail.html")
        pass


class RegisterView(View):
    def get(self,request):
        regist_form = RegisterForm()
        return render(request, "register.html",{'regist_form':regist_form})

    def post(self,request):
        regist_form = RegisterForm(request.POST)
        if regist_form.is_valid():
            email = request.POST.get("email", "")
            user_password = request.POST.get("password", "")
            if userProfile.objects.filter(email = email):
                return render(request, "register.html", {'msg': '用户已经注册'})
            user_profile = userProfile()
            user_profile.username =email
            user_profile.email =email
            user_profile.password =make_password(user_password)
            user_profile.save()

            send_register_email(email,'register')
            return render(request, "login.html")
            pass
        else:
            return render(request, "register.html",{'regist_form':regist_form})



class LoginView(View):
    def get(self,request):
        return render(request, "login.html", {})

    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            user_password = request.POST.get("password", "")
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html", {})
                else:
                    return render(request, "login.html", {"msg": "用户未激活"})
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form": login_form})


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user =userProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
            else:
                return None
        except Exception as e:
            return None


def user_login(request):
    if request.method =='POST':
        user_name = request.POST.get("username","")
        user_password=request.POST.get("password","")

        user = authenticate(username = user_name,password = user_password)

        if user is not None:
            login(request,user)
            return render(request,"index.html",{})
        else:
            return render(request, "login.html", {"msg":"用户名或密码错误！"})
        pass
    elif request.method =='GET':
        return render(request,"login.html",{})


class ForgetPwdView(View):
    def get(self,request):
        forgetForm = ForgetPwdForm();
        return render(request ,"forgetpwd.html",{'forgetpwd': forgetForm})

    def post(self,request):
        forgetForm = ForgetPwdForm(request.POST)
        if forgetForm.is_valid():
            email =  request.POST.get("email", "")
            send_register_email(email, 'forget')
            return render(request, "send_Success.html", {})


class ResetPasswordView(View):
    def get(self,request,activate_code):

        all_record = EmailVerifyRecord.objects.get(code=activate_code)
        print(all_record)
        if all_record:
            email = all_record.email
            return render(request, "password_reset.html",{'email' : email})
        else:
            return render(request, "activeFail.html")
        pass


class Modify_pwdView(View):
    def post(self,request):
        resetPwd = ResetPwdForm(request.POST)
        if resetPwd.is_valid():
            pass1 = request.POST.get('password1','')
            pass2 = request.POST.get('password2','')
            email = request.POST.get('email','')
            if pass1 == pass2:
                user = userProfile.objects.get(email=email)
                user.password = make_password(pass2)
                user.save()
                return render(request, "login.html", {})

            else:
                return render(request, "password_reset.html", {'msg':'两次密码输入不一样'})
            pass
        else:
            email = request.POST.get('email', '')
            return render(request, "password_reset.html", {'msg': '两次密码输入不一样', 'email': email})