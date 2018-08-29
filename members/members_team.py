from members.models import *
from players.models import *

class GetMembersTeam:
    def check_request(self, get_user_id, request_user):
        if not Members_table.objects.filter(user_id = get_user_id):
            new_member = Members_table.objects.create(calculate_team_points = 0, credits_left = 10000, total_cost_players_bought = 0.00, profit_gained_players_sold = 0.00, prize_money_minus_bought_sold = 0.00, user_id = request_user)
            new_member.save()

    def get_right_member(self, get_member, get_user_id):
        for i in get_member.values('user_id'):
            if i.get('user_id') is get_user_id:
                member_info = Members_table.objects.filter(user_id = i.get('user_id')).values()
        if not Goalkeeper_table.objects.filter(user_id = get_user_id):
            team_name = Personal_Info_table.objects.filter(has_username = get_user_id).values_list('team_name')
            get_team_name = team_name[0][0]
            get_players = None
        else:
            get_team_name = None
            boolean_credits = Members_table.objects.filter(user_id_id = get_user_id).values('boolean_team_points')
            get_credits_left = Members_table.objects.filter(user_id = get_user_id).values_list('credits_left', flat = True)
            get_gk = Goalkeeper_table.objects.filter(user_id_id = get_user_id).values_list('player_id_id', flat = True)
            get_def = Defender_table.objects.filter(user_id_id = get_user_id).values_list('player_id_id', flat = True)
            get_mid = Midfielder_table.objects.filter(user_id_id = get_user_id).values_list('player_id_id', flat = True)
            get_for = Striker_table.objects.filter(user_id_id = get_user_id).values_list('player_id_id', flat = True)
            get_gk_players = self.__get_squad(get_gk, boolean_credits, get_user_id, get_credits_left)
            get_def_players = self.__get_squad(get_def, boolean_credits, get_user_id, get_credits_left)
            get_mid_players = self.__get_squad(get_mid, boolean_credits, get_user_id, get_credits_left)
            get_for_players = self.__get_squad(get_for, boolean_credits, get_user_id, get_credits_left)
            get_players = [get_gk_players[0][0], get_def_players[0][0], get_mid_players[0][0], get_for_players[0][0]]
            self.__calc_points_left(boolean_credits[0]['boolean_team_points'], get_user_id)
        return member_info, get_team_name, get_players

    def __get_squad(self, get_squad, boolean_credits, get_user_id, get_credits_left):
        get_players = []
        value = 0
        for i in range(0, len(get_squad)):
            get_players.append(list(Player_table.objects.filter(id = get_squad[i]).values_list('player_name','player_position_1','player_position_2','player_position_3','current_player_value')))
        return get_players

    def __calc_points_left(self, boolean_credits, get_user_id):
        value = 0
        get_player_ids = []
        get_player_ids.append(Goalkeeper_table.objects.filter(user_id_id = get_user_id).values_list('player_id_id', flat = True)[0])
        get_player_ids.append(Defender_table.objects.filter(user_id_id = get_user_id).values_list('player_id_id', flat = True)[0])
        get_player_ids.append(Midfielder_table.objects.filter(user_id_id = get_user_id).values_list('player_id_id', flat = True)[0])
        get_player_ids.append(Striker_table.objects.filter(user_id_id = get_user_id).values_list('player_id_id', flat = True)[0])
        if boolean_credits is False:
            for j in range(0, len(get_player_ids)):
                total_valuation = Player_table.objects.filter(id = get_player_ids[j]).values_list('current_player_value', flat = True)
                value = value + total_valuation[0]
            credits_left = Members_table.objects.filter(user_id_id = get_user_id).values('credits_left')
            Members_table.objects.filter(user_id_id = get_user_id).update(credits_left = credits_left[0]['credits_left'] - value)
            Members_table.objects.filter(user_id_id = get_user_id).update(boolean_team_points = True)
