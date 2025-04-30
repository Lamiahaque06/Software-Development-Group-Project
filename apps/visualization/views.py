# apps/visualization/views.py
from django.shortcuts import render, redirect
from django.db.models import Count, Avg, Case, When, FloatField
from django.db.models.functions import ExtractQuarter
from apps.core.models import (
    Session, Vote, Team, Department,User
)

def _require_session(request):
    sess_id = request.session.get('session_id')
    if not sess_id:
        return False, redirect('sessions:team_select')
    return True, sess_id

def profile(request):
    ok, resp = _require_session(request)
    if not ok:
        return resp
    session_id = resp
    user_id = request.session.get('user_id')
    session_obj = Session.objects.select_related('team').get(
        pk=session_id
    )
    votes = Vote.objects.filter(
        session_id=session_id,
        user_id=user_id
    ).select_related('card')
    return render(request, 'visualization/profile.html', {
        'session': session_obj,
        'votes': votes,
    })

def team_summary(request):
    ok, resp = _require_session(request)
    if not ok:
        return resp
    session_id = resp
    team_id = request.session.get('team_id')
    # aggregate vote counts per card
    qs = Vote.objects.filter(
        session_id=session_id,
        session__team_id=team_id
    )
    raw = qs.values('card__title','vote_value').annotate(
        count=Count('vote_value')
    )
    # restructure into dict per card
    summary = {}
    for row in raw:
        title = row['card__title']
        val   = row['vote_value']
        cnt   = row['count']
        summary.setdefault(title, {'Green':0,'Amber':0,'Red':0})
        summary[title][val] = cnt
    return render(request, 'visualization/team_summary.html', {
        'summary': summary,
        'team': Team.objects.get(pk=team_id)
    })

def department_summary(request):
    ok, resp = _require_session(request)
    if not ok:
        return resp
    session_id = resp
    team_id = request.session.get('team_id')
    dept = Team.objects.select_related('department').get(
        pk=team_id
    ).department
    qs = Vote.objects.filter(
        session_id=session_id,
        session__team__department_id=dept.department_id
    )
    raw = qs.values('card__title','vote_value').annotate(
        count=Count('vote_value')
    )
    summary = {}
    for row in raw:
        title = row['card__title']
        val   = row['vote_value']
        cnt   = row['count']
        summary.setdefault(title, {'Green':0,'Amber':0,'Red':0})
        summary[title][val] = cnt
    return render(request, 'visualization/department_summary.html', {
        'summary': summary,
        'department': dept
    })

def card_progress(request):
    ok, resp = _require_session(request)
    if not ok:
        return resp
    team_id = request.session.get('team_id')
    # average scoring per quarter
    qs = Vote.objects.filter(
        session__team_id=team_id
    ).annotate(
        quarter=ExtractQuarter('session__date')
    ).annotate(
        score=Case(
            When(vote_value='Green', then=3),
            When(vote_value='Amber', then=2),
            When(vote_value='Red', then=1),
            output_field=FloatField()
        )
    ).values('quarter').annotate(
        avg_score=Avg('score')
    ).order_by('quarter')
    return render(request, 'visualization/card_progress.html', {
        'progress': qs,
        'team': Team.objects.get(pk=team_id)
    })


def profile(request):
    ok, resp = _require_session(request)
    if not ok:
        return resp
    session_id = resp
    user_id    = request.session.get('user_id')

    # fetch session + team
    session_obj = Session.objects.select_related('team').get(
        pk=session_id
    )
    # fetch this user’s votes (you may not need these for the form)
    votes = Vote.objects.filter(
        session_id=session_id,
        user_id=user_id
    ).select_related('card')

    # fetch the User record so we can prefill the form
    user_obj = User.objects.get(pk=user_id)

    return render(request, 'visualization/profile.html', {
        'session': session_obj,
        'votes':   votes,
        'user':    user_obj,
    })