# Generated by Django 2.0.6 on 2018-08-12 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0022_fixtures_table_competition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixtures_table',
            name='competition',
            field=models.CharField(choices=[('pl', 'Premier League'), ('cl', 'Champions League')], max_length=50),
        ),
    ]
