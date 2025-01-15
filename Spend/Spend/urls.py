from django.contrib import admin
from django.urls import path, include  # Import `include` function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Sapp.urls')),  # Replace `myapp` with your app's name
]
