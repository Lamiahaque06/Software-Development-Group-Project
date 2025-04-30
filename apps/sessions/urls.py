# apps/sessions/urls.py
from django.urls import path
from . import views

app_name = 'sessions'

urlpatterns = [
    path(
        'select/',
        views.team_select,
        name='team_select'
    ),
]
