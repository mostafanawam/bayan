from django.urls import path
from .views import  *

app_name = "main"
urlpatterns = [
      path("", home_page,name='home'),
      path("contact/", contact_page,name='contact'),
      path("about-us/", about_page,name='about'),

      path("programs/", programs_page,name='programs'),

      path("team/", team_page,name='team'),

      
      path("admissions/student/", student_apply_page,name='student_apply'),
      path("admissions/tutor/", tutor_apply_page,name='tutor_apply'),

]
