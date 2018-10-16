from django.conf.urls import url
from . import views as video_views
app_name = "video"

urlpatterns = [
    url(r'^(?P<column_id>\d+)/$',video_views.AllVideo,name="AllVideo"),
    url(r'^VidioDetail/(?P<video_id>\d+)/$',video_views.VideoDetail,name="VideoDetail"),
    url(r'^like-video/$',video_views.like_video,name="like_video"),

]