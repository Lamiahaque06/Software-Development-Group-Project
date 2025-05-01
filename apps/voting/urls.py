<<<<<<< HEAD
# apps/voting/urls.py
from django.urls import path
from . import views

app_name = 'voting'

urlpatterns = [
    path(
        '<int:session_id>/',
        views.vote_session,
        name='session_vote'
    ),
=======
from django.urls import path

urlpatterns = [
   
    path('', lambda request: HttpResponse("Voting app root")),
>>>>>>> ibtisam
]
