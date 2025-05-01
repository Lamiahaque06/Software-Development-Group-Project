<<<<<<< HEAD
# apps/authentication/urls.py
from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path(
        'role/<slug:role>/',
        views.choose_auth,
        name='choose_auth'
    ),
    path(
        'role/<slug:role>/login/',
        views.login_view,
        name='login'
    ),
    path(
        'role/<slug:role>/signup/',
        views.signup_view,
        name='signup'
    ),
    path('logout/', views.logout_view, name='logout'),
=======
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('engineers/', views.engineers_view, name='engineers'),
    path('team-leaders/', views.team_leaders_view, name='team_leaders'),
    path('department-leaders/', views.department_leaders_view, name='department_leaders'),
    path('senior-managers/', views.senior_managers_view, name='senior_managers'),
     
>>>>>>> ibtisam
]
