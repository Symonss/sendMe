from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from coreapp.models import Jobs
from django.utils import timezone


def home(request):
    jobs = Jobs.objects.filter(deadline__lte=timezone.now()).order_by('deadline')
    return render(request, 'coreapp/home.html', {'jobs':jobs})

def login(request):

    return render(request, 'coreapp/login.html')

def edb(request):

    return render(request, 'coreapp/Employeebd.html')
