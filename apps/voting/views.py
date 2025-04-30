# apps/voting/views.py
from django.shortcuts import render, redirect
from django.db import connection

def vote_session(request, session_id):
    """Render all cards and handle vote submission for a session."""
    # Fetch cards and prompts
    with connection.cursor() as cursor:
        cursor.execute(
            '''
            SELECT card_id, title, eval_prompt, traj_prompt
            FROM "HealthCheckCard"
            ORDER BY card_id
            '''
        )
        cards = [
            {
                'id': row[0],
                'title': row[1],
                'eval_prompt': row[2],
                'traj_prompt': row[3],
            }
            for row in cursor.fetchall()
        ]

    if request.method == 'POST':
        user_id = request.session.get('user_id', 1)
        with connection.cursor() as cursor:
            for card in cards:
                vote_val = request.POST.get(f'vote_{card["id"]}')
                prog     = request.POST.get(
                              f'progress_{card["id"]}'
                           )
                feedback_eval = request.POST.get(
                    f'feedback_eval_{card["id"]}', ''
                )
                feedback_traj = request.POST.get(
                    f'feedback_traj_{card["id"]}', ''
                )
                # Remove existing vote
                cursor.execute(
                    '''
                    DELETE FROM "Vote"
                    WHERE "user_id" = ? AND "session_id" = ?
                      AND "card_id" = ?
                    ''',
                    [user_id, session_id, card['id']]
                )
                # Insert new vote
                cursor.execute(
                    '''
                    INSERT INTO "Vote"
                      ("user_id","session_id","card_id",
                       "vote_value","progress_status")
                    VALUES (?, ?, ?, ?, ?)
                    ''',
                    [user_id, session_id,
                     card['id'], vote_val, prog]
                )
        return redirect(
            'voting:session_vote',
            session_id=session_id
        )

    return render(
        request,
        'voting/vote_session.html',
        {'session_id': session_id, 'cards': cards}
    )
