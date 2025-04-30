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
]
