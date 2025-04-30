# apps/visualization/urls.py
from django.urls import path
from . import views

app_name = 'visualization'

urlpatterns = [
    path(
        'profile/',
        views.profile,
        name='profile'
    ),
    path(
        'team-summary/',
        views.team_summary,
        name='team_summary'
    ),
    path(
        'department-summary/',
        views.department_summary,
        name='department_summary'
    ),
    path(
        'card-progress/',
        views.card_progress,
        name='card_progress'
    ),
]
