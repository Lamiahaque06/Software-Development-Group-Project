from django.urls import path

urlpatterns = [
   
    path('', lambda request: HttpResponse("Voting app root")),
]
