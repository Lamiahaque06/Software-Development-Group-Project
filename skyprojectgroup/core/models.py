from django.db import models

# Create your models here.
from django.db import models

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=200, unique=True)
    department_leader_id = models.IntegerField(null=True, blank=True)
    department_leader = models.CharField(max_length=200)
    department_location = models.CharField(max_length=200)

    class Meta:
        db_table = 'Department'

    def __str__(self):
        return self.department_name

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=200, unique=True)
    team_leader = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Team'

    def __str__(self):
        return self.team_name

class HealthCheckCard(models.Model):
    card_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)

    class Meta:
        db_table = 'HealthCheckCard'

    def __str__(self):
        return self.title

class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    date = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    session = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        db_table = 'Session'

    def __str__(self):
        return f"{self.team} – {self.date} ({self.session})"

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    ROLE_CHOICES = [('Engineer', 'Engineer'), ('Team Leader', 'Team Leader')]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    is_team_leader = models.BooleanField()

    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.username

class Vote(models.Model):
    vote_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    card = models.ForeignKey(HealthCheckCard, on_delete=models.CASCADE)
    VOTE_CHOICES = [('Green', 'Green'), ('Amber', 'Amber'), ('Red', 'Red')]
    vote_value = models.CharField(max_length=5, choices=VOTE_CHOICES)
    progress_status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'Vote'

    def __str__(self):
        return f"{self.user} → {self.card}: {self.vote_value}"
