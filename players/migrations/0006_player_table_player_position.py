# Generated by Django 2.0.6 on 2018-07-30 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_auto_20180726_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='player_table',
            name='player_position',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
