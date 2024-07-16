from django.urls import path
from .views import  *

app_name = "main"
urlpatterns = [

     path("", home_page,name='home'),
     path("contact/", contact_page,name='contact'),


]
