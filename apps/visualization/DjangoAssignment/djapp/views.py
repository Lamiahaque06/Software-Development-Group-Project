from django.contrib.auth.decorators import login_required
from django.core.paginator        import Paginator
from django.contrib.auth.views    import LoginView
from django.urls                  import reverse
from django.shortcuts             import render
from .models                      import Question, Response, Team, Department


class RoleBasedLoginView(LoginView):
    template_name       = 'djapp/login.html'
    redirect_field_name = None   

    def get_success_url(self):
        role = self.request.user.profile.role
        if role in ('dept_leader', 'senior_manager'):
            return reverse('dept_summary')
        return reverse('team_summary')


@login_required
def team_summary(request):
    role = request.user.profile.role

    if role == 'engineer':
        # engineers are only allowed to see their own
        sel_team = request.user.profile.team_id
        teams    = []
    else:
        sel_team = request.GET.get('team')
        teams    = Team.objects.all()

    qs = Response.objects.all()
    if sel_team:
        qs = qs.filter(team_id=sel_team)

    summaries = []
    for q in Question.objects.all():
        r     = qs.filter(question=q)
        total = r.count() or 1
        a     = r.filter(choice='agree').count()
        n     = r.filter(choice='neutral').count()
        summaries.append({
            'question':     q.text,
            'agree_pct':    round(a/total*100),
            'neutral_pct':  round(n/total*100),
            'disagree_pct': 100 - round(a/total*100) - round(n/total*100),
        })

    page = Paginator(summaries, 2).get_page(request.GET.get('page'))

    return render(request, 'djapp/team_summary.html', {
        'role':             role,
        'teams':            teams,
        'selected_team_id': sel_team or '',
        'page_summaries':   page,
    })

@login_required
def card_progress(request):
    card_id = request.GET.get('card')
    team_id = request.GET.get('team')
    dept_id = request.GET.get('dept')
    questions = Question.objects.all()

    
    if card_id:
        selected_card = Question.objects.filter(pk=card_id).first()
    else:
        selected_card = questions.first()

    # drodown options
    role = request.user.profile.role
    teams = Team.objects.all() if role != 'engineer' else []
    depts = Department.objects.all() if role in ('team_leader','dept_leader','senior_manager') else []


    qs = Response.objects.all()
    if selected_card:
        qs = qs.filter(question=selected_card)
    if team_id:
        qs = qs.filter(team_id=team_id)
    if dept_id:
        qs = qs.filter(team__department_id=dept_id)

    total = qs.count() or 1
    agree_pct    = round(qs.filter(choice='agree').count()    / total * 100)
    neutral_pct  = round(qs.filter(choice='neutral').count()  / total * 100)
    disagree_pct = 100 - agree_pct - neutral_pct

    return render(request, 'djapp/card_progress.html', {
        'role':           role,
        'questions':      questions,
        'selected_card':  selected_card,
        'teams':          teams,
        'depts':          depts,
        'agree_pct':      agree_pct,
        'neutral_pct':    neutral_pct,
        'disagree_pct':   disagree_pct,
    })


@login_required
def dept_summary(request):
    role      = request.user.profile.role
    depts     = Department.objects.all()
    sel_dept  = request.GET.get('dept')
    sel_team  = request.GET.get('team')

    if role in ('dept_leader', 'senior_manager'):
        teams = Team.objects.all()
    else:
        teams = []

    qs = Response.objects.all()
    if sel_dept:
        qs = qs.filter(team__department_id=sel_dept)
    if sel_team:
        qs = qs.filter(team_id=sel_team)

    summaries = []
    for q in Question.objects.all():
        r     = qs.filter(question=q)
        total = r.count() or 1
        a     = r.filter(choice='agree').count()
        n     = r.filter(choice='neutral').count()
        summaries.append({
            'question':     q.text,
            'agree_pct':    round(a/total*100),
            'neutral_pct':  round(n/total*100),
            'disagree_pct': 100 - round(a/total*100) - round(n/total*100),
        })

# 2 questions per page since they are linked
    page = Paginator(summaries, 2).get_page(request.GET.get('page'))

    return render(request, 'djapp/department_summary.html', {
        'role':               role,
        'depts':              depts,
        'selected_dept_id':   sel_dept or '',
        'teams':              teams,
        'selected_team_id':   sel_team or '',
        'page_summaries':     page,
    })
