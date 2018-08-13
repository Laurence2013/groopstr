from django.contrib.auth.models import User
from django.db import models

class Personal_Info_table(models.Model):
    team_name = models.CharField(max_length = 100)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    has_username = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.team_name

class Current_Position_table(models.Model):
    current_position = models.IntegerField(default = 0)
    current_prize_money_pos = models.IntegerField(default = 0)
    personal_info = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.current_position

class Members_table(models.Model):
    calculate_team_points = models.IntegerField(default = 0)
    boolean_team_points = models.BooleanField(default = False)
    credits_left = models.IntegerField(default = 0)
    total_cost_players_bought = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
    profit_gained_players_sold = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
    prize_money_minus_bought_sold = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)

class Fixtures_table(models.Model):
    COMPETITION_TYPES = (
        ('pl', 'Premier League'),
        ('cl', 'Champions League'),
    )
    fixture = models.CharField(max_length = 200)
    competition = models.CharField(max_length = 50, choices = COMPETITION_TYPES, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.fixture

class Week_table(models.Model):
    week_no = models.IntegerField(default = 0)
    current_week = models.BooleanField(default = False)
    fixture_no = models.ForeignKey(Fixtures_table, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)

class Formations_table(models.Model):
    FORMATION_TYPES = (
        ('formation_1', '4-4-2'),
        ('formation_2', '4-3-3'),
        ('formation_3', '4-5-1'),
        ('formation_4', '5-3-2'),
        ('formation_5', '5-4-1'),
        ('formation_6', '3-5-2'),
        ('formation_7', '3-4-3'),
    )
    formation = models.CharField(max_length = 11, choices = FORMATION_TYPES)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    week_no_id = models.ForeignKey(Week_table, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.formation
