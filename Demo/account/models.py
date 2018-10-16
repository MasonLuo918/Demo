from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class College(models.Model):
    college = models.CharField(max_length=100)

    def __str__(self):
        return self.college

class Userprofile(models.Model):

    RealName = models.CharField(max_length=20)
    Schoolid = models.CharField(max_length=12,unique=True,null=True)
    college = models.ForeignKey(College,blank=True,null=True,related_name="college_user")
    user = models.OneToOneField(User,unique=True)
    create_time = models.DateTimeField(auto_now_add=True,null=True)
    update_time = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.RealName

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name="验证码")
    email = models.CharField(max_length=50,verbose_name="邮箱")
    send_time = models.DateTimeField(verbose_name="发送时间",auto_now_add=True)
    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}({})'.format(self.code,self.email)
