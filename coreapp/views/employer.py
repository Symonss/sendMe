from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import CreateView
from ..forms import EmployerSignUpForm
from ..models import User, Employer, Jobs
from ..decorators import employer_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

class EmployerSignUpView(CreateView):
    model = User
    form_class = EmployerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

@method_decorator([login_required, employer_required], name='dispatch')
class JobCreateView(CreateView):
    model = Jobs
    fields = ('title','job_description','lower_range','upper_range','location','deadline' )
    template_name = 'coreapp/job_add_form.html'

    def form_valid(self, form):
        job = form.save(commit=False)
        job.Employer = self.request.user.employer
        job.save()
        messages.success(self.request, 'The appointment was created succesfully.')
        return redirect('edb')
