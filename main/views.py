from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _

from main.form import UniversityApplicationForm
from main.models import Category, Program
# Create your views here.

def home_page(request):

    return render(request,'home.html')

def contact_page(request):
    return render(request,'contact.html')

def apply_page(request):
    if request.method == 'POST':
        form = UniversityApplicationForm(request.POST)
        if form.is_valid():
            return HttpResponse('Application submitted successfully!')
    else:
        form = UniversityApplicationForm()

    return render(request,'application.html', {'form': form})


def about_page(request):
    return render(request,'about.html')


def team_page(request):
    return render(request,'team.html')


def programs_page(request):
    categories = Category.objects.all().order_by('index').prefetch_related('program_set')
    context={
        "categories":categories,
        # "categories_programs":categories_programs
    }

    return render(request,'programs.html',context)


