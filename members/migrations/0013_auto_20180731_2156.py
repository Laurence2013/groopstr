# Generated by Django 2.0.6 on 2018-07-31 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_auto_20180730_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members_table',
            old_name='personal_info',
            new_name='user_id',
        ),
    ]
