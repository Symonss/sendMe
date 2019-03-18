from django.contrib import admin
from django.urls import path, include
from coreapp.views import coreapp, clients, admins, writers, sub_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coreapp.urls')), #redirecting urls requests to coreapp.urls
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', coreapp.SignUpView.as_view(), name='signup'),
    path('accounts/signup/employer/', clients.EmployerSignUpView.as_view(), name='employer_signup'),
    path('accounts/signup/employee/', writers.EmployeeSignUpView.as_view(), name='employee_signup'),
    path('accounts/signup/admin/', admins.AdminSignUpView.as_view(), name='admin_signup'),
    path('accounts/signup_regional_admin/', sub_admin.RegionalAdminSignUpView.as_view(), name='regional_admin_signup'),
]
