from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Sum
from django.utils.timezone import localtime, now
from datetime import timedelta

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('bank', 'Bank'),
        ('mobile_money', 'Mobile Money'),
        ('cash', 'Cash'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=12, decimal_places=0, default=0)

    def __str__(self):
        return f"{self.name} ({self.get_account_type_display()}) - {self.balance:,} Rwf"


class Category(models.Model):
    CATEGORY_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=10, choices=CATEGORY_TYPES)  # Income or Expense
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category.name} > {self.name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'category'], name='unique_subcategory_per_category')
        ]


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    TRANSACTION_STATUSES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=0)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(default=now)  # Automatically set to the current datetime
    status = models.CharField(max_length=10, choices=TRANSACTION_STATUSES, default='completed')
    is_deleted = models.BooleanField(default=False)  # For soft deletion

    def clean(self):
        # Validate category type matches transaction type
        if self.category.type != self.transaction_type:
            raise ValidationError("Category type must match the transaction type.")

        # Validate expense does not exceed account balance
        if self.transaction_type == 'expense' and self.amount > self.account.balance:
            raise ValidationError("Expense cannot exceed the account balance.")

    def __str__(self):
        return f"{self.transaction_type.title()} - {self.amount:,} Rwf"

    class Meta:
        indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['transaction_type']),
        ]


class Budget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_budget = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    categories = models.ManyToManyField(Category, through='CategoryBudget')
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(default=now)  # Optional: Add periodic budgets
    end_date = models.DateField(null=True, blank=True)

    @property
    def remaining_budget(self):
        expenses = Transaction.objects.filter(
            account__user=self.user,
            category__in=self.categories.all(),
            transaction_type='expense',
            is_deleted=False
        ).aggregate(total=Sum('amount'))['total'] or 0
        return self.total_budget - expenses

    def __str__(self):
        return f"{self.user.username}'s Budget: {self.total_budget:,} Rwf"


class CategoryBudget(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    budget_amount = models.DecimalField(max_digits=12, decimal_places=0, default=0)

    def __str__(self):
        return f"{self.category.name} Budget: {self.budget_amount:,} Rwf"



def get_daily_summary(user):
    today = localtime(now()).date()
    daily_transactions = Transaction.objects.filter(
        account__user=user,
        date__date=today,
        is_deleted=False
    )
    summary = daily_transactions.values('transaction_type').annotate(
        total_amount=Sum('amount')
    )
    return {item['transaction_type']: item['total_amount'] for item in summary}


def get_weekly_summary(user):
    today = localtime(now()).date()
    start_of_week = today - timedelta(days=7)
    weekly_transactions = Transaction.objects.filter(
        account__user=user,
        date__date__gte=start_of_week,
        date__date__lte=today,
        is_deleted=False
    )
    summary = weekly_transactions.values('transaction_type').annotate(
        total_amount=Sum('amount')
    )
    return {item['transaction_type']: item['total_amount'] for item in summary}

def get_monthly_summary(user):
    today = localtime(now()).date()
    first_day_of_month = today.replace(day=1)
    monthly_transactions = Transaction.objects.filter(
        account__user=user,
        date__date__gte=first_day_of_month,
        date__date__lte=today,
        is_deleted=False
    )
    summary = monthly_transactions.values('transaction_type').annotate(
        total_amount=Sum('amount')
    )
    return {item['transaction_type']: item['total_amount'] for item in summary}

