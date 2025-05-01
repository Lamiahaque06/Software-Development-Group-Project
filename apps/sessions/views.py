<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.utils import timezone
from apps.core.models import Team, Session

def team_select(request):
    teams = Team.objects.all().order_by('team_id')

    # “team” chosen via GET
    selected_team_id = request.GET.get('team')
    sessions = []
    if selected_team_id:
        try:
            tid = int(selected_team_id)
            sessions = Session.objects.filter(
                team_id=tid
            ).order_by('-date', '-session_id')
            # remember the team across POST
            request.session['team_id'] = tid
        except ValueError:
            selected_team_id = None

    # Handle Continue vs New
    if request.method == 'POST':
        action = request.POST.get('action')
        team_id = request.session.get('team_id')
        if action == 'continue':
            # use chosen past session
            sess_id = request.POST.get('session')
            if sess_id and sessions and sessions.filter(
                session_id=sess_id
            ).exists():
                request.session['session_id'] = int(sess_id)
                return redirect('voting:session_vote',
                                session_id=sess_id)
        elif action == 'new' and team_id:
            # start a brand‐new session
            new_sess = Session.objects.create(
                date=timezone.localdate(),
                team_id=team_id,
                session='Active'
            )
            request.session['session_id'] = new_sess.session_id
            return redirect('voting:session_vote',
                            session_id=new_sess.session_id)

    return render(request, 'sessions/select.html', {
        'teams':             teams,
        'sessions':          sessions,
        'selected_team_id':  selected_team_id,
    })
session_home = team_select
=======
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
>>>>>>> ibtisam
