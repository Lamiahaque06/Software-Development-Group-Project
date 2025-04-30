from django.urls import path
from . import views

app_name = 'sessions'

urlpatterns = [
    path('', views.session_home, name='session_home'),
   
    path('select/', views.team_select, name='team_select'),
]
