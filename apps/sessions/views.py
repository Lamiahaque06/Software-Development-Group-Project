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
