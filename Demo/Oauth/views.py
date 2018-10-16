from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from .Base import Oauth_yiban
from .models import Oauth_ex
from account.models import Userprofile
from .forms import BindUserForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from utils.email_send import send_register_email
import time,uuid
# Create your views here.
def yiban_login(request):
    oauth_yiban = Oauth_yiban(settings.YIBAN_APP_ID,settings.YIBAN_APP_KEY,settings.YIBAN_REDIRECT_URL)
    url = oauth_yiban.get_auth_url()
    return HttpResponseRedirect(url)

def yiban_check(request):
    oauth_yiban = Oauth_yiban(settings.YIBAN_APP_ID,settings.YIBAN_APP_KEY,settings.YIBAN_REDIRECT_URL)
    code = request.GET.get('code','')
    try:
        access_token = oauth_yiban.get_access_token(code)
        time.sleep(0.1)
    except:
        return render(request,"Oauth/AccessTokenGetFailure.html")
    openid = oauth_yiban.get_open_id()
    infos = oauth_yiban.get_user_info()
    nickname = infos['yb_username']
    yiban = Oauth_ex.objects.filter(openid=openid)
    if yiban:
        auth_login(request,yiban[0].user)
        return HttpResponseRedirect("/home")
    else:
        url = '%s?nickname=%s&openid=%s' % (reverse("Oauth:bind_user"),nickname,openid)
        print(url)
        return HttpResponseRedirect(url)

def bind_user(request):
    nickname = request.GET.get('nickname',request.POST.get('nickname',''))
    openid = request.GET.get('openid',request.POST.get('openid',''))
    if request.method == "POST":
        form = BindUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            openid = cd['openid']
            nickname = cd['nickname']
            email = cd['email']
            user = User.objects.filter(email=email)
            if user:
                user = user[0]
                user.is_active=False
                send_register_email(email)
                user.save()
            else:
                while User.objects.filter(username=nickname):
                    nickname += "*"
                password = uuid.uuid1()
                user = User(username=nickname,email=email)
                user.set_password(password)
                user.is_active = False
                send_register_email(email)
                user.save()
                userprofile = Userprofile(user=user)
                userprofile.save()
            oauth_ex = Oauth_ex(user=user,openid=openid)
            oauth_ex.save()
            auth_login(request,user)
            return render(request,"Oauth/Success.html")
    else:
        form = BindUserForm(
            initial={
                "openid":openid,
                "nickname":nickname,
            }
        )
    return render(request,"Oauth/form.html",{"form":form,"nickname":nickname})


