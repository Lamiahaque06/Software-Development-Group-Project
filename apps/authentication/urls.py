from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('engineers/', views.engineers_view, name='engineers'),
    path('team-leaders/', views.team_leaders_view, name='team_leaders'),
    path('department-leaders/', views.department_leaders_view, name='department_leaders'),
    path('senior-managers/', views.senior_managers_view, name='senior_managers'), 
]
