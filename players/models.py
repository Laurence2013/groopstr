from django.db import models
from members.models import *

class Player_table(models.Model):
    POSITIONS = (
        ('Goalkeeper', 'Goalkeeper'),
        ('Defender', 'Defender'),
        ('Midfielder', 'Midfielder'),
        ('Forward', 'Forward'),
    )

    player_name = models.CharField(max_length = 100)
    player_position_1 = models.CharField(max_length = 100, choices = POSITIONS, default = None)
    player_position_2 = models.CharField(max_length = 100, blank = True, null=True)
    player_position_3 = models.CharField(max_length = 100, blank = True, null=True)
    current_player_value = models.DecimalField(max_digits = 6, decimal_places = 2, null=True)
    total_points = models.IntegerField(default = 0)
    is_player_playing = models.BooleanField(default = False)
    real_football_team = models.CharField(max_length = 100)
    week_no_id = models.ForeignKey(Week_table, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.player_name

class Form_table(models.Model):
    points = models.IntegerField(default = 0)
    total_points = models.IntegerField(default = 0)
    player = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    week_no_id = models.ForeignKey(Week_table, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)

    # class ReadonlyMeta:
    #     readonly = ['total_points']

class Clean_Sheets_table(models.Model):
    points = models.IntegerField(default = 0)
    total_points = models.IntegerField(default = 0)
    player = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    week_no_id = models.ForeignKey(Week_table, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)

class Goals_Assist_table(models.Model):
    points = models.IntegerField(default = 0)
    total_points = models.IntegerField(default = 0)
    player = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    week_no_id = models.ForeignKey(Week_table, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)

class Goals_table(models.Model):
    points = models.IntegerField(default = 0)
    total_points = models.IntegerField(default = 0)
    player = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    week_no_id = models.ForeignKey(Week_table, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)

class Man_of_Match_table(models.Model):
    points = models.IntegerField(default = 0)
    total_points = models.IntegerField(default = 0)
    player = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    week_no_id = models.ForeignKey(Week_table, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)

class Own_Goals_table(models.Model):
    points = models.IntegerField(default = 0)
    total_points = models.IntegerField(default = 0)
    player = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    week_no_id = models.ForeignKey(Week_table, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)

class Yellow_Card_table(models.Model):
    points = models.IntegerField(default = 0)
    total_points = models.IntegerField(default = 0)
    player = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    week_no_id = models.ForeignKey(Week_table, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)

class Red_Card_table(models.Model):
    points = models.IntegerField(default = 0)
    total_points = models.IntegerField(default = 0)
    player = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    week_no_id = models.ForeignKey(Week_table, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)

class Squad_table(models.Model):
    player = models.ForeignKey(Player_table, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)

class Goalkeeper_table(models.Model):
    is_subbed = models.BooleanField(default = False)
    is_playing = models.BooleanField(default = False)
    players_points = models.IntegerField(default = 0)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    player_id = models.ForeignKey(Player_table, on_delete = models.CASCADE, null=True, blank=True)
    week_no_id = models.ForeignKey(Week_table, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)

class Defender_table(models.Model):
    is_subbed = models.BooleanField(default = False)
    is_playing = models.BooleanField(default = False)
    players_points = models.IntegerField(default = 0)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    player_id = models.ForeignKey(Player_table, on_delete = models.CASCADE, null=True, blank=True)
    week_no_id = models.ForeignKey(Week_table, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)

class Midfielder_table(models.Model):
    is_subbed = models.BooleanField(default = False)
    is_playing = models.BooleanField(default = False)
    players_points = models.IntegerField(default = 0)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    player_id = models.ForeignKey(Player_table, on_delete = models.CASCADE, null=True, blank=True)
    week_no_id = models.ForeignKey(Week_table, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)

class Striker_table(models.Model):
    is_subbed = models.BooleanField(default = False)
    is_playing = models.BooleanField(default = False)
    players_points = models.IntegerField(default = 0)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    player_id = models.ForeignKey(Player_table, on_delete = models.CASCADE, null=True, blank=True)
    week_no_id = models.ForeignKey(Week_table, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)
