from django.db import models

class Personal_Info_table(models.Model):
    display_name = models.CharField(max_length = 100)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email_address = models.CharField(max_length = 100)
    contact_no = models.IntegerField(default = 0)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.display_name

class Current_Position_table(models.Model):
    current_position = models.IntegerField(default = 0)
    current_prize_money_pos = models.IntegerField(default = 0)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.current_position

class Members_table(models.Model):
    personal_info = models.ForeignKey(Personal_Info_table, on_delete = models.CASCADE)
    current_position = models.ForeignKey(Current_Position_table, on_delete = models.CASCADE)
    team_name = models.CharField(max_length = 50)
    # player_sold
    # player_bought
    calculate_team_points = models.IntegerField(default = 0)
    credits_left = models.IntegerField(default = 0)
    total_cost_players_bought = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    profit_gained_players_sold = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    prize_money_minus_bought_sold = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.pk
