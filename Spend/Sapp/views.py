from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm, AccountForm,TransactionForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Account, Transaction


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
    # Fetch accounts for the logged-in user
    accounts = Account.objects.filter(user=request.user)

    # Fetch the latest 5 transactions for the logged-in user
    transactions = Transaction.objects.filter(account__user=request.user).order_by('-date')[:5]

    context = {
        'accounts': accounts,
        'transactions': transactions,
    }
    return render(request, 'home.html', context)

@login_required
def add_account_view(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user  # Link the account to the logged-in user
            account.save()
            return redirect('home')  # Redirect to the homepage after adding
    else:
        form = AccountForm()

    context = {
        'form': form,
    }
    return render(request, 'add_account.html', context)


@login_required
def add_transaction_view(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.account.user = request.user  # Ensure the account belongs to the logged-in user
            transaction.save()

            # Update the account balance based on transaction type
            if transaction.transaction_type == 'income':
                transaction.account.balance += transaction.amount
            elif transaction.transaction_type == 'expense':
                transaction.account.balance -= transaction.amount

            transaction.account.save()
            return redirect('home')  # Redirect to dashboard after adding
    else:
        form = TransactionForm()

    context = {
        'form': form,
    }
    return render(request, 'add_transaction.html', context)