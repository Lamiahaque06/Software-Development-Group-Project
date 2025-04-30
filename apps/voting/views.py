from django.shortcuts import render, redirect
from apps.core.models import HealthCheckCard, Vote

def vote_session(request, session_id):
    cards = HealthCheckCard.objects.order_by('card_id')
    EVAL_CHOICES = [
        ('Green',    'Excellent',   'green'),
        ('Amber',    'Average',     'yellow'),
        ('Red',      'Bad',         'red'),
    ]
    PROG_CHOICES = [
        ('Improving',    '↑',     'green'),
        ('Stable',       '→',     'yellow'),
        ('Deteriorating','↓',     'red'),
    ]

    if request.method == 'POST':
        user_id = request.session.get('user_id', 1)
        for card in cards:
            vote_val = request.POST.get(f'vote_{card.card_id}')
            prog     = request.POST.get(f'progress_{card.card_id}')
            if vote_val and prog:
                Vote.objects.update_or_create(
                    user_id=user_id,
                    session_id=session_id,
                    card_id=card.card_id,
                    defaults={
                        'vote_value': vote_val,
                        'progress_status': prog
                    }
                )
        return redirect('voting:session_vote', session_id=session_id)

    return render(request, 'voting/vote_session.html', {
        'session_id':  session_id,
        'cards':       cards,
        'eval_choices':EVAL_CHOICES,
        'prog_choices':PROG_CHOICES,
    })
