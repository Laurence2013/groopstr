# Generated by Django 2.0.6 on 2018-08-12 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0018_week_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formations_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formation', models.CharField(choices=[('formation_1', '4-4-2'), ('formation_2', '4-3-3'), ('formation_3', '4-5-1'), ('formation_4', '5-3-2'), ('formation_5', '5-4-1'), ('formation_6', '3-5-2'), ('formation_7', '3-4-3')], max_length=11)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
