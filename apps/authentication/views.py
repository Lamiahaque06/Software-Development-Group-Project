<<<<<<< HEAD
# apps/authentication/views.py
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from apps.authentication.forms import LoginForm, SignupForm
from apps.core.models import User

ROLE_SLUGS = {
    'engineer': 'Engineer',
    'team-leader': 'Team Leader',
    'department-leader': 'Department Leader',
    'senior-manager': 'Senior Manager',
}


def welcome(request):
    """
    Landing page: choose your role.
    """
    return render(request, 'authentication/welcome.html', {
        'roles': ROLE_SLUGS.items()
    })


def choose_auth(request, role):
    """
    After role click: choose login or signup.
    """
    if role not in ROLE_SLUGS:
        raise Http404()
    return render(request, 'authentication/choose_auth.html', {
        'role': role,
        'role_label': ROLE_SLUGS[role],
    })


def signup_view(request, role):
    if role not in ROLE_SLUGS:
        raise Http404()
    role_label = ROLE_SLUGS[role]
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # uniqueness checks
            if User.objects.filter(username=cd['username']).exists():
                form.add_error('username', 'Username already taken')
            elif User.objects.filter(email=cd['email']).exists():
                form.add_error('email', 'Email already registered')
            else:
                is_leader = True if role_label == 'Team Leader' else False
                user = User.objects.create(
                    name=cd['name'],
                    username=cd['username'],
                    email=cd['email'],
                    password=make_password(cd['password1']),
                    role=role_label,
                    is_team_leader=is_leader,
                )
                request.session['user_id'] = user.user_id
                request.session['role'] = role_label
                messages.success(request, 'Signup successful.')
                return redirect('sessions:team_select')
    else:
        form = SignupForm()
    return render(request, 'authentication/signup.html', {
        'form': form,
        'role': role,
        'role_label': role_label,
    })


def login_view(request, role):
    if role not in ROLE_SLUGS:
        raise Http404()
    role_label = ROLE_SLUGS[role]
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user = User.objects.get(
                    username=cd['username'],
                    role=role_label
                )
                if check_password(cd['password'], user.password):
                    request.session['user_id'] = user.user_id
                    request.session['role'] = role_label
                    messages.success(request, 'Login successful.')
                    return redirect('sessions:team_select')
                else:
                    form.add_error(None, 'Invalid credentials')
            except User.DoesNotExist:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {
        'form': form,
        'role': role,
        'role_label': role_label,
    })


def logout_view(request):
    request.session.flush()
    return redirect('authentication:welcome')
=======
from django.shortcuts import render

def engineers_view(request):
    return render(request, 'engineers.html')

def team_leaders_view(request):
    return render(request, 'team_leaders.html')

def department_leaders_view(request):
    return render(request, 'department_leaders.html')

def senior_managers_view(request):
    return render(request, 'senior_managers.html')
>>>>>>> ibtisam
