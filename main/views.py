from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
# Create your views here.

def home_page(request):
    return render(request,'home.html')

def contact_page(request):
    return render(request,'contact.html')
