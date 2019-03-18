from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from ..decorators import employer_required
from ..forms import EmployeeSignUpForm
from ..models import Employer, User

class EmployerSignUpView(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('admins:employer_dashboard')

@method_decorator([login_required, employer_required], name='dispatch')
class E_EmployerDashboardView(ListView):
    model = Employer
    context_object_name = 'nothing'
    template_name = 'coreapp/clients/my_dashboard.html'
