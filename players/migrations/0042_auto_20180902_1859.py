# Generated by Django 2.0.6 on 2018-09-02 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0041_auto_20180827_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defender_table',
            name='is_playing',
        ),
        migrations.RemoveField(
            model_name='defender_table',
            name='week_no_id',
        ),
        migrations.RemoveField(
            model_name='goalkeeper_table',
            name='is_playing',
        ),
        migrations.RemoveField(
            model_name='goalkeeper_table',
            name='week_no_id',
        ),
        migrations.RemoveField(
            model_name='midfielder_table',
            name='is_playing',
        ),
        migrations.RemoveField(
            model_name='midfielder_table',
            name='week_no_id',
        ),
        migrations.RemoveField(
            model_name='striker_table',
            name='is_playing',
        ),
        migrations.RemoveField(
            model_name='striker_table',
            name='week_no_id',
        ),
    ]
