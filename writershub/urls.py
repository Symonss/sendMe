from django.contrib import admin
from django.urls import path, include
from coreapp.views import coreapp, employer, worker


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coreapp.urls')), #redirecting urls requests to coreapp.urls

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', coreapp.SignUpView.as_view(), name='signup'),
    path('accounts/signup/employer/', employer.EmployerSignUpView.as_view(), name='employer_signup'),
    path('accounts/signup/worker/', worker.WorkerSignUpView.as_view(), name='worker_signup'),

]
