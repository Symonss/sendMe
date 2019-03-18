from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django import forms
from coreapp.models import  (User, Employer, Admin, RegionalAdmin)

class EmployeeSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ('first_name', 'last_name', 'phone','email', )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employee = True
        if commit:
            user.save()
        return user

class EmployerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ('first_name', 'last_name', 'phone','email', )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employer = True
        user.save()
        employer = Employer.objects.create(user=user)
        return user

class RegionalAdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ('first_name', 'last_name', 'phone','email', )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_regional_admin = True
        user.save()
        regionaladmin= RegionalAdmin.objects.create(user=user)
        return user

class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ('first_name', 'last_name', 'phone','email', )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        admin = Admin.objects.create(user=user)
        return user
