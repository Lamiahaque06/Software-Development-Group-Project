from django.db import models
from apps.core.models import Team, Session

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    

