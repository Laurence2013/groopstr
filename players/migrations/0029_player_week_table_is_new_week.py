# Generated by Django 2.0.6 on 2018-08-16 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0028_player_week_table_date_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='player_week_table',
            name='is_new_week',
            field=models.BooleanField(default=False),
        ),
    ]
