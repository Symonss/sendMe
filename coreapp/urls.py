
from django.urls import include, path

from .views import coreapp

urlpatterns = [
    path('', coreapp.home, name='home'),
    # path('create', coreapp.create_order, name='create_order'),




]
