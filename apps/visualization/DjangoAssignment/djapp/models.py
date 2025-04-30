from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class Department(models.Model):
    name    = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True,    null=True, blank=True)

    def __str__(self):
        return self.name

        
class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Response(models.Model):
    CHOICES = [
        ('agree',    'Agree'),
        ('neutral',  'Neutral'),
        ('disagree', 'Disagree'),
    ]

    user     = models.ForeignKey(User,     on_delete=models.CASCADE)
    team     = models.ForeignKey(Team,     on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice   = models.CharField(max_length=8, choices=CHOICES)
    created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} – {self.question} – {self.choice}"


class Profile(models.Model):
    ROLE_CHOICES = [
        ('engineer',       'Engineer'),
        ('team_leader',    'Team Leader'),
        ('dept_leader',    'Department Leader'),
        ('senior_manager', 'Senior Manager'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
