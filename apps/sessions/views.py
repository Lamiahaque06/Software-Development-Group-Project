# apps/sessions/views.py

from django.shortcuts import render, redirect
from django.utils import timezone
from apps.core.models import Session
from .forms import TeamSelectForm

def team_select(request):
    """
    Let the user pick a Team. On POST we auto-create an Active Session
    for today, and store both IDs in request.session.
    """
    if request.method == 'POST':
        form = TeamSelectForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            new_sess = Session.objects.create(
                date=timezone.localdate(),
                team=team,
                session='Active'
            )
            request.session['team_id']    = team.team_id
            request.session['session_id'] = new_sess.session_id
            return redirect('voting:card_list')
    else:
        form = TeamSelectForm()

    return render(request, 'sessions/select.html', {'form': form})
