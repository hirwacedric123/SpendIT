from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('bank', 'Bank'),
        ('mobile_money', 'Mobile Money'),
        ('cash', 'Cash'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link account to a user
    name = models.CharField(max_length=100)  # e.g., "My Bank Account"
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=12, decimal_places=0, default=0)  # Rwf balance

    def __str__(self):
        return f"{self.name} ({self.get_account_type_display()}) - {self.balance} Rwf"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE)  # Link to an account
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=0)
    description = models.TextField(blank=True, null=True)  # Optional
    date = models.DateTimeField(auto_now_add=True)  # Automatically record the date

    def __str__(self):
        return f"{self.get_transaction_type_display()}: {self.amount} Rwf on {self.date}"
