from members.models import *
from players.models import *

class Statistics_Tables:
    def __init__(self, set_table_name, table_name, table_as_list):
        self.__set_table_name = set_table_name
        self.__table_name = table_name
        self.__table_as_list = table_as_list

    def set_stats_table(self):
        return self.__save_stats_table(self.__set_table_name, self.__table_name, self.__table_as_list)

    def set_to_save(self, table_name, name, table_as_list):
        return self.__set_to_save_to_json(table_name, name, table_as_list)

    def __save_stats_table(self, set_table_name, table_name, table_as_list):
        current_weeks_goals_context = {
            'name': table_name,
            table_as_list: list(set_table_name.objects.values('id','points','player_id','week_no_id_id')),
        }
        return current_weeks_goals_context

    def __set_to_save_to_json(self, save_list, name, table_as_list):
        list_context = []
        name_context = {'name': save_list.get(name),}
        list_context.append(name_context)

        for j in range(0, len(save_list.get(table_as_list))):
            table_name_context = {'table': save_list.get(table_as_list)[j],}
            list_context.append(table_name_context)
        return list_context
