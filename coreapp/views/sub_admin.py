from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..decorators import regional_admin_required, admin_required
from ..forms import RegionalAdminSignUpForm
from ..models import User

class RegionalAdminSignUpView(CreateView):
    model = User
    form_class = RegionalAdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('admins:r_admins_dashboard')

@method_decorator([login_required, regional_admin_required], name='dispatch')
class R_AdminDashboardView(ListView):
    model = User
    context_object_name = 'orders'
    template_name = 'coreapp/sub_admin/my_dashboard.html'
