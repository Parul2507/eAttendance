from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignupForm
from .models import UserProfile
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

def index_view(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_profile = UserProfile.objects.filter(email=email).first()
            if user_profile and check_password(password, user_profile.password):
                request.session['username'] = user_profile.name
                request.session['userid'] = user_profile.id
                request.session['loggedin'] = True
                return redirect('/')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    request.session['username'] = ""
    request.session['userid'] = ""
    request.session['loggedin'] = False
    return redirect('/')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                if UserProfile.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!!!')
                else:
                    password = make_password(password)
                    user_profile = UserProfile.objects.create(name=name, email=email, password=password)
                    return redirect('/')
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})
