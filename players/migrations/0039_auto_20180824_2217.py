# Generated by Django 2.0.6 on 2018-08-24 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0038_auto_20180824_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_table',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='players.Player_table'),
        ),
        migrations.AlterField(
            model_name='form_table',
            name='points',
            field=models.IntegerField(default=0, null=True),
        ),
    ]