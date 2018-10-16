from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Oauth_ex(models.Model):
    user = models.ForeignKey(User)
    openid = models.CharField(max_length=100,default='')