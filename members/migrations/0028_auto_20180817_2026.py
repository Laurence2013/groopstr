# Generated by Django 2.0.6 on 2018-08-17 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0027_remove_week_table_current_week'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='week_table',
            name='fixture_no',
        ),
        migrations.AddField(
            model_name='fixtures_table',
            name='date_of_game',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fixtures_table',
            name='week_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.Week_table'),
        ),
        migrations.AddField(
            model_name='week_table',
            name='current_week',
            field=models.BooleanField(default=False),
        ),
    ]
