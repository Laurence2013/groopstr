# Generated by Django 2.0.6 on 2018-08-12 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0016_auto_20180810_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixtures_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixture', models.CharField(max_length=200)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
