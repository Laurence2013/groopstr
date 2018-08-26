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
