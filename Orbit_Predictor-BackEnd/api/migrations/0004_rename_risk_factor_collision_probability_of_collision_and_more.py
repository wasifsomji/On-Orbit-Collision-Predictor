# Generated by Django 5.1.3 on 2024-12-07 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_collision_conjunction_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collision',
            old_name='risk_factor',
            new_name='probability_of_collision',
        ),
        migrations.RemoveField(
            model_name='collision',
            name='collision_date',
        ),
    ]
