import os
from django.conf import settings
from admin_updates.saving_and_getting_json import Saving_And_Getting_Json

class Group_Tables:
    def __init__(self, goals_tbl, clean_sheets_tbl, form_tbl, goals_assist_tbl, man_of_the_match_tbl, own_goals_tbl, red_card_tbl, yellow_card_tbl, all_weeks, get_all_players, json_file_name):
        self.__saving_to_json = Saving_And_Getting_Json()
        self.__goals_table = goals_tbl
        self.__clean_sheets_table = clean_sheets_tbl
        self.__form_table = form_tbl
        self.__goals_assist_table = goals_assist_tbl
        self.__man_of_the_match_table = man_of_the_match_tbl
        self.__own_goals_table = own_goals_tbl
        self.__red_card_table = red_card_tbl
        self.__yello_card_table = yellow_card_tbl
        self.__all_weeks_table = all_weeks
        self.__get_all_players = get_all_players
        self.__json_file_name = json_file_name

    def set_group_table(self):
        tables_list = []
        tables_list.append(self.__goals_table)
        tables_list.append(self.__clean_sheets_table)
        tables_list.append(self.__form_table)
        tables_list.append(self.__goals_assist_table)
        tables_list.append(self.__man_of_the_match_table)
        tables_list.append(self.__own_goals_table)
        tables_list.append(self.__red_card_table)
        tables_list.append(self.__yello_card_table)
        tables_list.append(self.__all_weeks_table)
        tables_list.append(self.__get_players())
        return True if self.__save_list_to_json(tables_list) is True else False

    def __get_players(self):
        get_players = []
        context_name = {'name': 'players_name'}
        get_players.append(context_name)
        for i in range(0, len(self.__get_all_players)):
            context = {
                'player_id': self.__get_all_players[i].get('id'),
                'player_name': self.__get_all_players[i].get('player_name')
            }
            get_players.append(context)
        return get_players

    def __save_list_to_json(self, tables_list):
        self.__saving_to_json.save_json(tables_list, self.__json_file_name)
        json_file_path = settings.BASE_DIR + '/static/json/'+ self.__json_file_name +'.json'
        return os.path.getsize(json_file_path) > 0
