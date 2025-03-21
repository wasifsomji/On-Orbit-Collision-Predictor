# Generated by Django 5.1.3 on 2024-12-07 01:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collision',
            name='conjunction_id',
        ),
        migrations.RemoveField(
            model_name='probabilitycalc',
            name='conjuction_id',
        ),
        migrations.AddField(
            model_name='collision',
            name='cdm',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='collisions', to='api.cdm'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='probabilitycalc',
            name='cdm',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='probability_calcs', to='api.cdm'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Conjunction',
        ),
    ]
