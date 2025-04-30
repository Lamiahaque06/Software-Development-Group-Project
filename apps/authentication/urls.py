from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/engineer/', views.engineer_signup, name='engineer_signup'),
    path('signup/team_leader/', views.team_leader_signup, name='team_leader_signup'),
    path('signup/department_leader/', views.department_leader_signup, name='department_leader_signup'),
    path('signup/senior_manager/', views.senior_manager_signup, name='senior_manager_signup'),
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
]
