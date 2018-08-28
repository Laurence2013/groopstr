import os
import json
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder

class Saving_And_Getting_Json:
    def __init__(self):
        self.base_dir = settings.BASE_DIR

    def get_json_file(self, get_json):
        main_json_file = self.base_dir + '/static/json/'+ get_json +'.json'
        try:
            main_json_file_size = os.path.getsize(main_json_file)
            if main_json_file_size > 0:
                 with open(main_json_file) as json_file:
                     get_main_json = json.load(json_file)
        except FileNotFoundError as e:
            print(e)
        return get_main_json

    def save_json(self, save_file_to_json, get_json):
        json_file = json.dumps(save_file_to_json, ensure_ascii=False, indent=4, cls=DjangoJSONEncoder)
        with open(self.base_dir + '/static/json/'+ get_json +'.json', 'w') as f:
            f.write(json_file)

    def get_players_positions(self, positions):
        positions_list = []
        for i in range(0, len(positions)):
            context = {
                'id': positions[i].get('id'),
                'player_name': positions[i].get('player_name'),
                'current_player_value': positions[i].get('current_player_value'),
                'real_football_team': positions[i].get('real_football_team'),
                'player_position_1': positions[i].get('player_position_1'),
                'is_player_not_playing': positions[i].get('is_player_not_playing'),
                'total_points': positions[i].get('total_points'),
            }
            positions_list.append(context)
        return positions_list

    def get_sum_of_points(self, a_stat_table, table_name):
        final_points = []
        sum_points = []
        for i in range(0, len(a_stat_table)):
            for j in table_name.objects.all().values('player_id', 'points'):
                if a_stat_table[i].get('id') == j.get('player_id'):
                    sum_points.append(j.get('points'))
            context = {
                'id': a_stat_table[i].get('id'),
                'points': sum(sum_points)
            }
            final_points.append(context)
            sum_points = []
        return final_points

    def get_final_total_points(self, get_player, get_form_points, get_goals_points, get_goals_assist_points, get_man_of_match_points, get_own_goal_points, get_yellow_card_points, get_red_card_points, get_clean_sheets_points):
        get_context = []
        for i in range(0, len(get_player)):
            if get_player[i].get('id') == get_form_points[i].get('id') == get_goals_points[i].get('id') == get_goals_assist_points[i].get('id') == get_man_of_match_points[i].get('id') == get_own_goal_points[i].get('id') == get_yellow_card_points[i].get('id') == get_red_card_points[i].get('id') == get_clean_sheets_points[i].get('id'):
                context = {
                    'id': get_player[i].get('id'),
                    'total_points': get_form_points[i].get('points') + get_goals_points[i].get('points') + get_goals_assist_points[i].get('points') + get_man_of_match_points[i].get('points') + get_own_goal_points[i].get('points') + get_yellow_card_points[i].get('points') + get_red_card_points[i].get('points') + get_clean_sheets_points[i].get('points')
                }
                get_context.append(context)
        return get_context
