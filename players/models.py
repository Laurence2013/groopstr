from django.db import models
from members.models import *

class Player_table(models.Model):
    player_name = models.CharField(max_length = 100)
    current_player_value = models.IntegerField(default = 0)
    real_football_team = models.CharField(max_length = 100)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.player_name

class Form_table(models.Model):
    points = models.IntegerField(default = 0)
    player_id = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.pk

class Clean_Sheets_table(models.Model):
    points = models.IntegerField(default = 0)
    player_id = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.pk

class Goals_Assist_table(models.Model):
    points = models.IntegerField(default = 0)
    player_id = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.pk

class Goals_table(models.Model):
    points = models.IntegerField(default = 0)
    player_id = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.pk

class Man_of_Match_table(models.Model):
    points = models.IntegerField(default = 0)
    player_id = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.pk

class Own_Goals_table(models.Model):
    minus_points = models.IntegerField(default = 0)
    player_id = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.pk

class Yellow_Card_table(models.Model):
    minus_points = models.IntegerField(default = 0)
    player_id = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.pk

class Red_Card_table(models.Model):
    minus_points = models.IntegerField(default = 0)
    player_id = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.pk

class Team_table(models.Model):
    position = models.CharField(max_length = 50)
    points = models.IntegerField(default = 0)
    members_id = models.ForeignKey(Members_table, on_delete = models.CASCADE)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.pk

class Player_Team_table(models.Model):
    player_id = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    team_id = models.ForeignKey(Team_table, on_delete = models.CASCADE)
    members_id = models.ForeignKey(Members_table, on_delete = models.CASCADE)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.pk
