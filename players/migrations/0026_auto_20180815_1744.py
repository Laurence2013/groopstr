# Generated by Django 2.0.6 on 2018-08-15 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0025_auto_20180814_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player_table',
            old_name='is_player_playing',
            new_name='is_player_not_playing',
        ),
    ]
