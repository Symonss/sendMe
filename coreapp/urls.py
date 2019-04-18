
from django.urls import include, path

from .views import coreapp, employer

urlpatterns = [
    path('', coreapp.home, name='home'),
    path('login', coreapp.login, name='login'),
    path('employee/home', coreapp.edb, name='edb'),
    path('job/add', employer.JobCreateView.as_view(), name='job_add'),

    # path('create', coreapp.create_order, name='create_order'),




]
