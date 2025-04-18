# Generated by Django 5.1.3 on 2025-02-15 23:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_cdm_sat1_catalog_name_cdm_sat1_covariance_method_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('alert_threshold', models.FloatField(default=1e-09)),
                ('users', models.ManyToManyField(related_name='organizations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
