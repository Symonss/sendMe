
from django.urls import include, path

from .views import coreapp

urlpatterns = [
    path('', coreapp.home, name='home'),
    path('login', coreapp.login, name='login'),
    path('employee/home', coreapp.edb, name='edb'),

    # path('create', coreapp.create_order, name='create_order'),




]
