# apps/sessions/views.py
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from apps.core.models import Session
from .forms import TeamSelectForm

# @login_required
def team_select(request):
    if request.method == 'POST':
        form = TeamSelectForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            new_sess = Session.objects.create(
                date=timezone.localdate(),
                team=team,
                session='Active'
            )
            request.session['team_id'] = team.team_id
            request.session['session_id'] = new_sess.session_id

            return redirect(
                'voting:session_vote',
                session_id=new_sess.session_id
            )
    else:
        form = TeamSelectForm()

    return render(request, 'sessions/select.html', {'form': form})
