# Generated by Django 2.0.6 on 2018-08-04 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0014_auto_20180804_2038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clean_sheets_table',
            old_name='player_id',
            new_name='player',
        ),
        migrations.RenameField(
            model_name='form_table',
            old_name='player_id',
            new_name='player',
        ),
        migrations.RenameField(
            model_name='goals_assist_table',
            old_name='player_id',
            new_name='player',
        ),
        migrations.RenameField(
            model_name='goals_table',
            old_name='player_id',
            new_name='player',
        ),
        migrations.RenameField(
            model_name='man_of_match_table',
            old_name='player_id',
            new_name='player',
        ),
        migrations.RenameField(
            model_name='own_goals_table',
            old_name='player_id',
            new_name='player',
        ),
        migrations.RenameField(
            model_name='red_card_table',
            old_name='player_id',
            new_name='player',
        ),
        migrations.RenameField(
            model_name='squad_table',
            old_name='player_id',
            new_name='player',
        ),
        migrations.RenameField(
            model_name='squad_table',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='yellow_card_table',
            old_name='player_id',
            new_name='player',
        ),
    ]
