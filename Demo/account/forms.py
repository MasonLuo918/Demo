from django import forms
from .models import Userprofile
from django.contrib.auth.models import User
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="密码",widget=forms.PasswordInput(attrs={"placeholder":"请输入你的密码"}))
    password2 = forms.CharField(label="确认密码",widget=forms.PasswordInput(attrs={"placeholder":"请确认你的密码"}))
    class Meta:
        model = User
        fields = ("username","email")
        error_messages = {
            "username": {'required': "modelform 得到了：用户名已存在，请重新输入"},
        }
    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({"placeholder":"请输入你的用户名"})
        self.fields['email'].widget.attrs.update({"placeholder":"请输入你的邮箱"})


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("两个密码输入不一致,请重新输入")
        return cd['password2']

class UserprofileForm(forms.ModelForm):

    class Meta:
        model = Userprofile
        fields = ("Schoolid","RealName")
        error_messages = {
            "Schoolid":{'required':"学号已被注册，请跟管理员联系"},
            "RealName":{'required':"请输入你的真实姓名"}
        }

    def __init__(self,*args,**kwargs):
        super(UserprofileForm,self).__init__(*args,**kwargs)
        self.fields['Schoolid'].widget.attrs.update({"placeholder":"请输入你的学号"})
        self.fields['RealName'].widget.attrs.update({"placeholder":"请输入你的真实姓名"})
