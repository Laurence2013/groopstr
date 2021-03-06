# Generated by Django 2.0.6 on 2018-08-20 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0030_auto_20180817_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals_table',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='players.Player_table'),
        ),
        migrations.AlterField(
            model_name='goals_table',
            name='points',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='goals_table',
            name='total_points',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
