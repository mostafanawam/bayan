
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from admins.forms import AdminLoginForm
from main.models import Category, ContactUs, Program
import django_filters
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms

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
    if not request.user.is_authenticated:
        return redirect('admins:admin_login')
    
    programs=Program.objects.all().order_by('index')
    categories=Category.objects.all().order_by('index')
    context={
        'programs':programs,
        'categories':categories
    }
    return render(request,'programs.html',context)

def admin_students(request):
    if not request.user.is_authenticated:   
        return redirect('admins:admin_login')
    return render(request,'students.html')


def admin_staff(request):
    if not request.user.is_authenticated:   
        return redirect('admins:admin_login')
    
    return render(request,'staff.html')



class ContactFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
    )
    email = django_filters.CharFilter(
        lookup_expr='icontains',
    )

    class Meta:
        model = ContactUs
        fields = ['name', 'email']

def admin_contacts(request):
    if not request.user.is_authenticated:   
        return redirect('admins:admin_login')

    queryset=ContactUs.objects.all().order_by('-id')

    items_per_page = 10
    page= request.GET.get('page', 1)
    contacts_filter = ContactFilter(request.GET, queryset=queryset)

    paginator = Paginator(contacts_filter.qs, items_per_page)


    try:
        paginated_items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        paginated_items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        paginated_items = paginator.page(paginator.num_pages)


    context={
        "paginated_items":paginated_items,
        'filter': contacts_filter,
        'query_params': request.GET.urlencode()
    }
    return render(request,'contacts.html',context)


