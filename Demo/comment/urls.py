from django.conf.urls import url
from . import views as Comment_views
app_name = "comment"

urlpatterns = [
    url(r'^upload/$',Comment_views.upload_comment,name="upload_comment"),
]