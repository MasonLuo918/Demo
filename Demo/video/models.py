from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your models here.
class Classify(models.Model):

    column = models.CharField(max_length=20)

    def __str__(self):
        return self.column

class LectureVideo(models.Model):
    title = models.CharField(max_length=20)
    video = models.FileField(upload_to="video/LectureVideo")
    image = models.ImageField(upload_to="images/Lectureimage")
    introduce = models.TextField(blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    user_like = models.ManyToManyField(User,related_name="video_like",blank=True)
    column = models.ForeignKey(Classify,null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("video:VideoDetail",args=[self.id])
