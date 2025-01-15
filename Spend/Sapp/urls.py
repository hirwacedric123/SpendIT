from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home_view, name='home'),
    path('add-account/', views.add_account_view, name='add_account'),
    path('add-transaction/', views.add_transaction_view, name='add_transaction'),
   
    path('logout/', views.logout_view, name='logout'),
]
