# apps/sessions/forms.py
from django import forms
<<<<<<< HEAD
from apps.core.models import Team

class TeamSelectForm(forms.Form):
    """
    Let the user pick their Team.
    """
    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        label="Select your team",
        empty_label="– select a team –",
        widget=forms.Select(attrs={
            'class': 'w-full bg-lavender-100 text-purple-500 '
                     'border-none shadow-md p-2'
        })
    )
=======
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username']

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
