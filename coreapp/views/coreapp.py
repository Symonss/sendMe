from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..decorators import admin_required, employee_required

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_employer:
            return redirect('clients:employer_dashboard')
        elif request.user.is_admin:
            return redirect('admins:admins_dashboard')
        elif request.user.is_regional_admin:
            return redirect('admins:admins_dashboard')
        else:
            return redirect('writers:employees_dashboard')
    return render(request, 'coreapp/home.html')
