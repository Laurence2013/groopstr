# Generated by Django 2.0.6 on 2018-08-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0022_auto_20180813_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player_table',
            name='player_position_1',
            field=models.CharField(choices=[('gk', 'Goalkeeper'), ('def', 'Defender'), ('mid', 'Midfielder'), ('for', 'Forward')], default=None, max_length=100),
        ),
    ]
