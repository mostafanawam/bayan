from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _

from main.models import Category, Program
# Create your views here.

def home_page(request):
    # categories=Category.objects.filter(is_enabled=True).order_by('index')

    # programs=Program.objects.filter(is_enabled=True).order_by('index')

    # categories_programs = Category.objects.prefetch_related('program_set').order_by('index')

    categories = Category.objects.all().order_by('index').prefetch_related('program_set')
    context={
        "categories":categories,
        # "categories_programs":categories_programs
    }
    return render(request,'home.html',context)

def contact_page(request):
    return render(request,'contact.html')
