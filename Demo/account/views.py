from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,HttpResponse
from .models import Userprofile,College,EmailVerifyRecord
from .forms import RegisterForm,UserprofileForm
from django.contrib.auth.models import User
from utils.email_send import send_register_email
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
# Create your views here.

def register(request):
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        userprofile_form = UserprofileForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid():
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            user = user_form.save(commit=False)
            user.is_active = False
            user.set_password(password)
            user.save()
            userprofile = userprofile_form.save(commit=False)
            userprofile.user = user
            userprofile.save()
            send_register_email(email)
            return render(request,"account/Success.html")
    else:
        user_form = RegisterForm()
        userprofile_form = UserprofileForm()
    print(user_form.errors)
    print(userprofile_form.errors)
    return render(request,"account/register.html",{"user_form":user_form,"userprofile_form":userprofile_form})

def ActivateUser(request,activate_code):
    print(activate_code)
    all_records = EmailVerifyRecord.objects.filter(code=activate_code)
    if all_records:
        for record in all_records:
            email = record.email
            user = User.objects.get(email=email)
            user.is_active=True
            user.save()
    else:
        return render(request,"account/active_fail.html")
    return render(request,"account/activate.html")