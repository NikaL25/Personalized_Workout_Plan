# Generated by Django 4.1.7 on 2024-03-13 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_alter_workoutplan_session_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutplan',
            name='session_duration',
            field=models.DurationField(),
        ),
    ]
