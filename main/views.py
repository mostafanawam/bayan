from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.contrib import messages
from main.form import ContactForm, UniversityApplicationForm
from main.models import Category, Program
from main.tasks import send_email
# Create your views here.

def home_page(request):

    return render(request,'home.html')

def contact_page(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(form.cleaned_data)
            # Send email (adjust this part with your email settings)
            # send_email(
            #     f"{subject} - Message from {name}",  # Subject
            #     message,  # Message
            #     ['recipient@example.com'],  # To email
            # )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('main:contact')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = ContactForm()        
    return render(request,'contact.html',{'form': form})

def student_apply_page(request):
    if request.method == 'POST':
        form = UniversityApplicationForm(request.POST)
        if form.is_valid():
            return HttpResponse('Application submitted successfully!')
    else:
        form = UniversityApplicationForm()

    return render(request,'student-application.html', {'form': form})



def tutor_apply_page(request):
    if request.method == 'POST':
        form = UniversityApplicationForm(request.POST)
        if form.is_valid():
            return HttpResponse('Application submitted successfully!')
    else:
        form = UniversityApplicationForm()

    return render(request,'tutor-application.html', {'form': form})



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


