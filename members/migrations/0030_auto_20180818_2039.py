# Generated by Django 2.0.6 on 2018-08-18 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0029_auto_20180817_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixtures_table',
            name='competition',
            field=models.CharField(blank=True, choices=[('Premier League', 'Premier League'), ('Champions League', 'Champions League')], max_length=50, null=True),
        ),
    ]
