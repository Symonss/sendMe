
from django.urls import include, path

from .views import coreapp, clients, admins, writers, sub_admin

urlpatterns = [
    path('', coreapp.home, name='home'),
    # path('create', coreapp.create_order, name='create_order'),

    path('employer/', include(([

    ], 'coreapp'), namespace='employer')),


    path('RegionalAdmin/', include(([

    ], 'coreapp'), namespace='regional_admin')),


    path('sAdmin/', include(([
        path('', admins.AdminDashboardView.as_view(), name='admins_dashboard'),
        path('employer', clients.E_EmployerDashboardView.as_view(), name='employer_dashboard'),
        path('radmin', sub_admin.R_AdminDashboardView.as_view(), name='r_admins_dashboard'),

    ], 'coreapp'), namespace='sAdmins')),


    path('employees/', include(([
        path('', writers.EmployeeDashboardView.as_view(), name='employees_dashboard'),
        # path('quiz/add/', teachers.QuizCreateView.as_view(), name='quiz_add'),
        # path('quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
        # path('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='quiz_delete'),
        # path('quiz/<int:pk>/results/', teachers.QuizResultsView.as_view(), name='quiz_results'),
        # path('quiz/<int:pk>/question/add/', teachers.question_add, name='question_add'),
        # path('quiz/<int:quiz_pk>/question/<int:question_pk>/', teachers.question_change, name='question_change'),
        # path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', teachers.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'coreapp'), namespace='employee')),
]
