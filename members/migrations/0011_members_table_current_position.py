# Generated by Django 2.0.6 on 2018-07-30 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_remove_members_table_current_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='members_table',
            name='current_position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.Current_Position_table'),
        ),
    ]
