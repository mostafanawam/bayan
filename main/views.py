from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.contrib import messages
from bayan_university import settings
from main.form import  ContactForm, UniversityApplicationForm
from main.models import Category, ContactUs, Events, Program
from main.tasks import send_email
# Create your views here.

def home_page(request):
    events=Events.objects.filter(event_date__gte=datetime.now().date()).order_by('event_date').order_by('event_time')
    context={
        "events":events
    }
    return render(request,'main/home.html',context)

def contact_page(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            contact_us=ContactUs.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            # Send email (adjust this part with your email settings)
            html_message=f"""
                <h3>Hello Dear, <br> 
                You have a new message from {name} having the email: {email}<br>
                message subject:{subject} <br>
                Message content:{message}<br>
                </h3>
            """
            
            send_email.delay(f'Bayan - Message from {name}',html_message,[settings.EMAIL_RECEIVER])
            
            html_customer=f"""
                <h3>Hello {name}, <br> 
                we have received your message
            """
            send_email.apply_async(args=(f'Bayan - Message Received',html_customer,[email]),countdown=60)
            

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('main:contact')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = ContactForm()        
    return render(request,'main/contact.html',{'form': form})

def student_apply_page(request):
    if request.method == 'POST':
        form = UniversityApplicationForm(request.POST)
        if form.is_valid():
            return HttpResponse('Application submitted successfully!')
    else:
        form = UniversityApplicationForm()

    return render(request,'main/student-application.html', {'form': form})



def tutor_apply_page(request):
    if request.method == 'POST':
        form = UniversityApplicationForm(request.POST)
        if form.is_valid():
            return HttpResponse('Application submitted successfully!')
    else:
        form = UniversityApplicationForm()

    return render(request,'main/tutor-application.html', {'form': form})



def about_page(request):
    return render(request,'main/about.html')


def team_page(request):
    return render(request,'main/team.html')


def programs_page(request):
    categories = Category.objects.all().order_by('index').prefetch_related('program_set')
    context={
        "categories":categories,
        # "categories_programs":categories_programs
    }

    return render(request,'main/programs.html',context)




