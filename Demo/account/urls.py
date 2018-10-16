from django.conf.urls import url
from . import views as account_views
from django.contrib.auth import views as auth_views
app_name = "account"

urlpatterns = [
    url(r'^activate/(?P<activate_code>.*)/$',account_views.ActivateUser,name="ActivateUser"),
    url(r'^register/$',account_views.register,name="register"),
    url(r'^login/$',auth_views.login,{"template_name":"account/login.html"},name="login"),
    url(r'^logout/$',auth_views.logout,{"template_name":"account/logout.html"},name="logout"),
    url(r'^password-change/$',auth_views.password_change,{"template_name":"account/password_change.html","post_change_redirect":"/account/password-change-done"},name="password_change"),
    url(r'^password-change-done/$',auth_views.password_change_done,{"template_name":"account/password_change_done.html"},name="password_change_done")
]