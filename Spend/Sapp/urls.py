from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home_view, name='home'),
    path('add-account/', views.add_account_view, name='add_account'),
    path('add-transaction/', views.add_transaction_view, name='add_transaction'),
    path('manage-budget/', views.manage_budget_view, name='manage_budget'),
    path('add-category/', views.add_category_view, name='add_category'),
    path('add-subcategory/', views.add_subcategory, name='add_subcategory'),
    path('load-subcategories/', views.load_subcategories, name='load_subcategories'),
    path('transaction-summary/', views.transaction_summary_view, name='transaction_summary'),

    path('api/transaction-summary/', views.transaction_summary_data, name='transaction_summary_data'),
   
    path('logout/', views.logout_view, name='logout'),
]
