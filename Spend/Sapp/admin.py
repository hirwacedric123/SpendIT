from django.contrib import admin

# Register your models here.
from . models import Account, Transaction, Budget, Category

admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Budget)
admin.site.register(Category)

admin.site.site_header = "Spend Admin"