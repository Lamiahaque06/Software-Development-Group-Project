from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
ALTER TABLE "HealthCheckCard"
  ADD COLUMN "eval_prompt" TEXT NOT NULL DEFAULT '';
ALTER TABLE "HealthCheckCard"
  ADD COLUMN "traj_prompt" TEXT NOT NULL DEFAULT '';
UPDATE "HealthCheckCard"
   SET eval_prompt =
         'How do you evaluate ' || title || '?',
       traj_prompt =
         'How do you perceive the trajectory of ' || title || '?';
""",
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
