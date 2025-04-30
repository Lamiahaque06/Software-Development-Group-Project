# apps/sessions/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import (
    CustomUserCreationForm, CustomUserChangeForm,
    EngineerSignUpForm, TeamLeaderSignUpForm,
    DepartmentLeaderSignUpForm, SeniorManagerSignUpForm,
    UserUpdateForm
)
from django.contrib import messages

def role_signup(request, role):
    role_form_mapping = {
        'engineer': EngineerSignUpForm,
        'team_lead': TeamLeaderSignUpForm,
        'dept_lead': DepartmentLeaderSignUpForm,
        'senior_manager': SeniorManagerSignUpForm,
    }

    if role not in role_form_mapping:
        return redirect('login') 
    
    form_class = role_form_mapping[role]

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = form_class()

    return render(request, f'accounts/{role}_signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/profile_update.html', {'form': form})
