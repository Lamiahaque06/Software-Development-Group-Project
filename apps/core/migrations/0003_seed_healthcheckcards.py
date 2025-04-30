from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0002_add_card_prompts'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
-- Insert the six HealthCheck cards with their dynamic prompts
INSERT OR IGNORE INTO "HealthCheckCard"
  (card_id, title, eval_prompt, traj_prompt) VALUES
  (1, 'Value Delivered',
     'How do you evaluate Value Delivered?',
     'How do you perceive the trajectory of Value Delivered?'),
  (2, 'Team Morale',
     'How do you evaluate Team Morale?',
     'How do you perceive the trajectory of Team Morale?'),
  (3, 'Process Efficiency',
     'How do you evaluate Process Efficiency?',
     'How do you perceive the trajectory of Process Efficiency?'),
  (4, 'Technical Quality',
     'How do you evaluate Technical Quality?',
     'How do you perceive the trajectory of Technical Quality?'),
  (5, 'Delivery Speed',
     'How do you evaluate Delivery Speed?',
     'How do you perceive the trajectory of Delivery Speed?'),
  (6, 'Technical Debt',
     'How do you evaluate Technical Debt?',
     'How do you perceive the trajectory of Technical Debt?');
""",
            reverse_sql="""
DELETE FROM "HealthCheckCard"
 WHERE card_id IN (1,2,3,4,5,6);
"""
        )
    ]
