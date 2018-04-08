# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/03/21 18:51'
from  random import  Random
from django.core.mail import send_mail
from  users.models import EmailVerifyRecord
from MxOnline.settings import EMAIL_FROM


def rando_char(randomLength = 8):
    str = '';
    base_chars = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890'
    length = len(base_chars)-1
    random = Random()
    for temp in range(randomLength):
        str += base_chars[random.randint(0,length)]
    return  str;


def send_register_email(email,send_type='register'):
    email_record = EmailVerifyRecord()
    code = rando_char(16)
    email_record.code = code
    email_record.email =email
    email_record.send_type =send_type
    email_record.save()

    email_title = ''
    email_body = ''
    if send_type =='register':
        email_title = '激活邮件'
        email_body = '请点击以下链接，激活你的账号：http://127.0.0.1:8000/active/{0}'.format(code)
        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass
    elif send_type =='forget':
        email_title = '忘记密码'
        email_body = '请点击以下链接，重置你的密码：http://127.0.0.1:8000/reset/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass