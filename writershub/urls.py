from django.contrib import admin
from django.urls import path, include
from coreapp.views import coreapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coreapp.urls')), #redirecting urls requests to coreapp.urls
    
]
