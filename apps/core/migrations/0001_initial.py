# Generated by Django 5.2 on 2025-05-01 00:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=200, unique=True)),
                ('department_leader_id', models.IntegerField(blank=True, null=True)),
                ('department_leader', models.CharField(max_length=200)),
                ('department_location', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Department',
            },
        ),
        migrations.CreateModel(
            name='HealthCheckCard',
            fields=[
                ('card_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'HealthCheckCard',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=200, unique=True)),
                ('team_leader', models.CharField(max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.department')),
            ],
            options={
                'db_table': 'Team',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('session', models.CharField(choices=[('Active', 'Active'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], max_length=10)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.team')),
            ],
            options={
                'db_table': 'Session',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('vote_id', models.AutoField(primary_key=True, serialize=False)),
                ('vote_value', models.CharField(choices=[('Green', 'Green'), ('Amber', 'Amber'), ('Red', 'Red')], max_length=5)),
                ('progress_status', models.CharField(blank=True, max_length=50, null=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.healthcheckcard')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Vote',
            },
        ),
    ]
