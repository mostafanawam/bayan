
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from admins.forms import AdminLoginForm

def admin_login(request):
    if request.method == 'POST':
        form=AdminLoginForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admins:admin_main')  # Replace 'home' with your desired redirect URL
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Please correct the error below.')

    return render(request,'login.html')

def admin_main(request):
    if not request.user.is_authenticated:
        return redirect('admins:admin_login')
    
    return render(request,'main.html')

def admin_logout(request):
    logout(request)
    return redirect("admins:admin_login")

def admin_programs(request):
    return render(request,'programs.html')

def admin_students(request):

    return render(request,'students.html')


def admin_staff(request):
    return render(request,'staff.html')


def admin_contacts(request):
    return render(request,'contacts.html')


