from members.models import *
from players.models import *

class Weeks_Table:
    def __init__(self, weeks, week_table, weekss):
        self.__weeks = weeks
        self.__week_table = week_table
        self.__weekss = weekss

    def set_weeks(self):
        return self.__get_all_weeks() if self.__weeks is None else self.__get_specific_week()

    def set_to_save(self, weeks):
        return self.__set_to_save(weeks) if weeks else False

    def __get_all_weeks(self):
        return self.__week_table.objects.values('id','week_no','start_date','end_date','has_this_week_passed')

    def __get_specific_week(self):
        pass

    def __set_to_save(self, weeks):
        weeks_list = []
        weeks_name_context = {'name': self.__weekss,}
        weeks_list.append(weeks_name_context)
        for i in range(0, len(weeks)):
            weeks_context = {str(i): weeks[i],}
            weeks_list.append(weeks_context)
        return weeks_list
