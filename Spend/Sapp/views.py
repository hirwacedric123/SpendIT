from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create the user
            user = User.objects.create_user(
                username=form.cleaned_data['email'],  # Use email as the username
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password'],
            )
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')  # Redirect to the login page
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request, 
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                messages.success(request, f"Welcome back, {user.first_name}!")
                return redirect('home')  # Redirect to a homepage/dashboard
            else:
                messages.error(request, "Invalid credentials.")
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

@login_required
def home_view(request):
    # Placeholder context for now; we will expand it as we add features
    context = {
        'user': request.user,
    }
    return render(request, 'home.html', context)