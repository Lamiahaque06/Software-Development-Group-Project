from django.contrib.auth.decorators import login_required
from django.core.paginator        import Paginator
from django.contrib.auth.views    import LoginView
from django.urls                  import reverse
from django.shortcuts             import render
from .models                      import Question, Response, Team, Department


class RoleBasedLoginView(LoginView):
    template_name       = 'djapp/login.html'
    redirect_field_name = None   # ignore “next=…” param

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
