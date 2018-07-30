# Generated by Django 2.0.6 on 2018-07-29 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0002_auto_20180729_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_info_table',
            name='has_username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]