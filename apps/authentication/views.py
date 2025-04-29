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

def engineer_signup(request):
    if request.method == 'POST':
        form = EngineerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = EngineerSignUpForm()
    return render(request, 'accounts/engineer_signup.html', {'form': form})

def team_leader_signup(request):
    if request.method == 'POST':
        form = TeamLeaderSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = TeamLeaderSignUpForm()
    return render(request, 'accounts/team_leader_signup.html', {'form': form})

def department_leader_signup(request):
    if request.method == 'POST':
        form = DepartmentLeaderSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = DepartmentLeaderSignUpForm()
    return render(request, 'accounts/department_leader_signup.html', {'form': form})

def senior_manager_signup(request):
    if request.method == 'POST':
        form = SeniorManagerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SeniorManagerSignUpForm()
    return render(request, 'accounts/senior_manager_signup.html', {'form': form})

# Login / Logout / Profile remain same as you have, small fix below:
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
