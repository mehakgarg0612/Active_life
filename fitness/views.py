from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password != confirm_password:
            error_message = "Passwords do not match."
            return render(request, 'signup.html', {'error_message': error_message})

        if UserProfile.objects.filter(email=email).exists():
            error_message = "Email is already registered."
            return render(request, 'signup.html', {'error_message': error_message})
        
        user = UserProfile(name=name, email=email, phone=phone, password=password)
        user.save()

        return redirect('login')  

    return render(request, 'signup.html')


def home(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'aboutus.html')

def services(request):
    return render(request, 'services.html')

def membership(request):
    return render(request, 'membership.html')

def shop(request):
    return render(request, 'shop.html')
def blog(request):
    return render(request, 'blog.html')

from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact_message = ContactMessage(name=name, email=email, phone=phone, message=message)
        contact_message.save()

        return redirect('contact_success')  

    return render(request, 'contactus.html')
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = UserProfile.objects.filter(email=email, password=password).first()

        if user:
           return render(request, 'loginsuccess.html', {'username': user.name})
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials. Please try again.'})
    else:
        return render(request, 'login.html')


def forgotpass(request):
    return render(request,'forgotpassword.html')
def login_success(request):
    return render(request, 'loginsuccess.html')

def thirty_day_challenge(request):
    return render(request, '30days.html')

def success_join_challenge(request):
    return render(request, 'success_join_challenge.html')
def eating_view(request):
    return render(request, 'eating.html')
def reach(request):
    return render(request, 'reach.html')
def silver_membership(request):
    return render(request, 'silver.html')
def success_silver(request):
    return render(request, 'successsilver.html')
def gold_membership(request):
    return render(request, 'gold.html')
def success_gold(request):
    return render(request, 'successgold.html')
def contact_success(request):
    return render(request, 'contact_success.html')