# apps/sessions/forms.py

from django import forms
from apps.core.models import Team

class TeamSelectForm(forms.Form):
    """
    A simple form that lets the user pick their Team.
    Upon submission, a new Session is auto‑created in the view.
    """
    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        label="Select your team",
        empty_label="– select a team –",
        widget=forms.Select(attrs={
            'class': 'w-full bg-lavender-100 text-purple-500 border-none shadow-md p-2'
        })
    )
