# Generated by Django 5.1.3 on 2024-11-10 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CDM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccsds_cdm_version', models.CharField(max_length=10)),
                ('creation_date', models.DateTimeField()),
                ('originator', models.CharField(max_length=50)),
                ('message_id', models.CharField(max_length=100, unique=True)),
                ('tca', models.DateTimeField()),
                ('miss_distance', models.FloatField()),
                ('sat1_object', models.CharField(max_length=50)),
                ('sat1_object_designator', models.CharField(max_length=50)),
                ('sat1_maneuverable', models.CharField(max_length=3)),
                ('sat1_x', models.FloatField()),
                ('sat1_y', models.FloatField()),
                ('sat1_z', models.FloatField()),
                ('sat1_x_dot', models.FloatField()),
                ('sat1_y_dot', models.FloatField()),
                ('sat1_z_dot', models.FloatField()),
                ('sat2_object', models.CharField(max_length=50)),
                ('sat2_object_designator', models.CharField(max_length=50)),
                ('sat2_maneuverable', models.CharField(max_length=3)),
                ('sat2_x', models.FloatField()),
                ('sat2_y', models.FloatField()),
                ('sat2_z', models.FloatField()),
                ('sat2_x_dot', models.FloatField()),
                ('sat2_y_dot', models.FloatField()),
                ('sat2_z_dot', models.FloatField()),
            ],
        ),
    ]
