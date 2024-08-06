
from django.urls import path
from .views import  *

app_name = "admins"
urlpatterns = [
    path("", admin_main,name='admin_main'),
    path("programs/", admin_programs,name='admin_programs'),
    path("students/", admin_students,name='admin_students'),
    path("staff/", admin_staff,name='admin_staff'),

    path("contacts/", admin_contacts,name='admin_contacts'),


    path("login/", admin_login,name='admin_login'),
    path("logout/", admin_logout,name='admin_logout'),
]
