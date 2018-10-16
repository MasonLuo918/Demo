from random import Random
from django.core.mail import send_mail
from account.models import EmailVerifyRecord
from django.conf import settings

def random_str(RandomLength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(RandomLength):
        str+=chars[random.randint(0,length)]
    return str

def send_register_email(email):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.save()
    email_title = "注册激活链接"
    email_body = "请点击下面的链接激活你的账号:www.masonluo.online/account/activate/{0}".format(code)
    print(settings.EMAIL_HOST_USER)
    print(type(email))
    print(email)
    send_status = send_mail(email_title,email_body,settings.EMAIL_HOST_USER,[email])
    if send_status:
        pass
