# Generated by Django 2.0.6 on 2018-07-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20180725_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player_table',
            name='current_player_value',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]