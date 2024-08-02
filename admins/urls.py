
from django.urls import path
from .views import  *

app_name = "admins"
urlpatterns = [
    path("", admin_main,name='admin_main'),
    path("login/", admin_login,name='admin_login'),
    path("logout/", admin_logout,name='admin_logout'),
]
