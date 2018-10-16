from django import forms
from .models import Oauth_ex
from .Base import Oauth_yiban
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class BindUserForm(forms.Form):

   openid = forms.CharField(widget=forms.HiddenInput(attrs={"id":"openid","name":"openid"}))
   email = forms.EmailField(widget=forms.EmailInput(attrs={"id":"email","name":"email","placeholder":"请输入你的邮箱"}))
   nickname = forms.CharField(widget=forms.HiddenInput(attrs={"id":"nickname","name":"nickname"}))



