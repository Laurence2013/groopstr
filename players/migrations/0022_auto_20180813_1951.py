# Generated by Django 2.0.6 on 2018-08-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0021_defender_table_goalkeeper_table_midfielder_table_striker_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player_table',
            name='player_position_1',
            field=models.CharField(choices=[('gk', 'Goalkeeper'), ('def', 'Defender'), ('mid', 'Midfielder'), ('str', 'Striker')], default=None, max_length=100),
        ),
    ]
