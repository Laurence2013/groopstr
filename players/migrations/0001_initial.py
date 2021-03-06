# Generated by Django 2.0.6 on 2018-07-25 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clean_Sheets_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Form_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goals_Assist_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goals_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Man_of_Match_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Own_Goals_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minus_points', models.IntegerField(default=0)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100)),
                ('current_player_value', models.IntegerField(default=0)),
                ('real_football_team', models.CharField(max_length=100)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player_Team_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('members_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Members_table')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player_table')),
            ],
        ),
        migrations.CreateModel(
            name='Red_Card_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minus_points', models.IntegerField(default=0)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player_table')),
            ],
        ),
        migrations.CreateModel(
            name='Team_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50)),
                ('points', models.IntegerField(default=0)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('members_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Members_table')),
            ],
        ),
        migrations.CreateModel(
            name='Yellow_Card_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minus_points', models.IntegerField(default=0)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player_table')),
            ],
        ),
        migrations.AddField(
            model_name='player_team_table',
            name='team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Team_table'),
        ),
        migrations.AddField(
            model_name='own_goals_table',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player_table'),
        ),
        migrations.AddField(
            model_name='man_of_match_table',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player_table'),
        ),
        migrations.AddField(
            model_name='goals_table',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player_table'),
        ),
        migrations.AddField(
            model_name='goals_assist_table',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player_table'),
        ),
        migrations.AddField(
            model_name='form_table',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player_table'),
        ),
        migrations.AddField(
            model_name='clean_sheets_table',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player_table'),
        ),
    ]
