from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from .models import Account,Transaction, Budget, Category, Subcategory

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Passwords do not match.")
        return cleaned_data

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")  # Use email as username


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'account_type', 'balance']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'account_type': forms.Select(attrs={'class': 'form-control'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'transaction_type', 'amount', 'description', 'category', 'subcategory']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['subcategory'].queryset = Subcategory.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass  # Invalid input; ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategories.all()
    

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['total_budget']
        widgets = {
            'total_budget': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['type', 'name']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
        }
        labels = {
            'type': 'Transaction Type',
            'name': 'Category Name',
        }