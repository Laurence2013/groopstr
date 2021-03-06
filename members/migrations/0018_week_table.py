# Generated by Django 2.0.6 on 2018-08-12 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0017_fixtures_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Week_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_no', models.IntegerField(default=0)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('fixture_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.Fixtures_table')),
            ],
        ),
    ]
