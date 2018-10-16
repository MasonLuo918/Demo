from django.conf.urls import url
from . import views as Oauth_views

app_name = "Oauth"

urlpatterns = [
    url(r'^yiban_login/$',Oauth_views.yiban_login,name="yiban_login"),#跳转到易班的授权页面
    url(r'^yiban_check/$',Oauth_views.yiban_check,name="yiban_check"),#回调地址
    url(r'^bind_user',Oauth_views.bind_user,name="bind_user"),#绑定用户名的地址
]