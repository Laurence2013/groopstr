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
    # player_sold
    # player_bought
    calculate_team_points = models.IntegerField(default = 0)
    boolean_team_points = models.BooleanField(default = True)
    credits_left = models.IntegerField(default = 0)
    total_cost_players_bought = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
    profit_gained_players_sold = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
    prize_money_minus_bought_sold = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)
