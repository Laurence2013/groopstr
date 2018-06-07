from django.db import models

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

class Yellow_Car_table(models.Model):
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
