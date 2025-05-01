# apps/authentication/forms.py
<<<<<<< HEAD
from django import forms
from apps.core.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full border rounded p-2',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full border rounded p-2',
            'placeholder': 'Password'
        })
    )


class SignupForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'w-full border rounded p-2',
            'placeholder': 'Full Name'
        })
    )
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full border rounded p-2',
            'placeholder': 'Username'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full border rounded p-2',
            'placeholder': 'Email'
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full border rounded p-2',
            'placeholder': 'Password'
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full border rounded p-2',
            'placeholder': 'Confirm Password'
        })
    )

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password1')
        p2 = cleaned.get('password2')
        if p1 and p2 and p1 != p2:
            self.add_error('password2', 'Passwords must match')
        return cleaned
=======
from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.sessions.models import CustomUser  # so its still importing from sessions

class RoleBasedSignUpForm(UserCreationForm):
    role_value = None  

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.role_value
        if commit:
            user.save()
        return user

class EngineerSignUpForm(RoleBasedSignUpForm):
    role_value = 'engineer'

class TeamLeaderSignUpForm(RoleBasedSignUpForm):
    role_value = 'team_lead'

class DepartmentLeaderSignUpForm(RoleBasedSignUpForm):
    role_value = 'dept_lead'

class SeniorManagerSignUpForm(RoleBasedSignUpForm):
    role_value = 'senior_manager'
>>>>>>> ibtisam
