# Generated by Django 2.0.6 on 2018-08-13 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0024_auto_20180812_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members_table',
            name='boolean_team_points',
            field=models.BooleanField(default=False),
        ),
    ]
