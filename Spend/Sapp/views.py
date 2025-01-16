from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm, AccountForm,TransactionForm, BudgetForm, CategoryForm,SubcategoryForm


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Account, Transaction, Budget
from django.db.models import Sum



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
    accounts = Account.objects.filter(user=request.user)
    transactions = Transaction.objects.filter(account__user=request.user).order_by('-date')
    
    # Get the user's budget if it exists
    try:
        budget = Budget.objects.get(user=request.user)
    except Budget.DoesNotExist:
        budget = None

    # Aggregate total expenses
    total_expenses = Transaction.objects.filter(
        account__user=request.user, transaction_type='expense'
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    remaining_budget = budget.total_budget - total_expenses if budget else None

    # Create a notification for budget overrun
    budget_overrun = False
    if remaining_budget and remaining_budget < 0:
        budget_overrun = True

    context = {
        'accounts': accounts,
        'transactions': transactions,
        'budget': budget,
        'total_expenses': total_expenses,
        'remaining_budget': remaining_budget,
        'budget_overrun': budget_overrun,
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



@login_required
def manage_budget_view(request):
    try:
        budget = Budget.objects.get(user=request.user)
    except Budget.DoesNotExist:
        budget = None

    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('home')
    else:
        form = BudgetForm(instance=budget)

    context = {
        'form': form,
    }
    return render(request, 'manage_budget.html', context)

@login_required
def add_category_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('home')  # Redirect back to the dashboard
    else:
        form = CategoryForm()

    context = {
        'form': form,
    }
    return render(request, 'add_category.html', context)


@login_required
def add_subcategory(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subcategory added successfully!')
            return redirect('home')  # Redirect to the home or another page
    else:
        form = SubcategoryForm()
    return render(request, 'add_subcategory.html', {'form': form})

