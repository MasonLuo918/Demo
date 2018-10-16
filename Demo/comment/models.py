from django.db import models
from django.contrib.auth.models import User
from video.models import LectureVideo
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User,related_name="user_comment")
    video = models.ForeignKey(LectureVideo,related_name="Video_comment")
    body = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    display = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}".format(self.user.username,self.video.title)
