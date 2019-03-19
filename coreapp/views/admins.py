from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.utils import timezone
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..decorators import admin_required, employer_required, regional_admin_required
from ..forms import AdminSignUpForm
from ..models import User,Admin

class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admins'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('admins:admins_dashboard')

@method_decorator([login_required, admin_required], name='dispatch')
class AdminDashboardView(ListView):
    model = Admin
    context_object_name = 'nothing_yet'
    template_name = 'coreapp/admins/my_dashboard.html'

@method_decorator([login_required, regional_admin_required], name='dispatch')
class R_AdminDashboardView(ListView):
    model = Admin
    context_object_name = 'muyy'
    template_name = 'coreapp/sub_admin/my_dashboard.html'