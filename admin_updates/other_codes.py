def __group_ids(self, week):
    week_right = []
    week_left = []
    is_end_week = 1
    for i in range(0, len(week)):
        if is_end_week < len(week):
            if week[i] == week[i+1]:
                week_right.append(week[i].get('week_no'))
                week_left.append(week[i+1].get('week_no'))
            is_end_week += 1
    final_week = week_right + week_left
    print(final_week)
    is_end_week2 = 1
    for j in range(0, len(week)):
        if is_end_week2 < len(final_week):
            if week[j].get('week_no') == final_week[is_end_week2]:
                print(week[j].get('week_no'), final_week[is_end_week2])
        is_end_week2 += 1

def __group_ids_1(self, week):
    group_week = []
    is_end_week = 1
    for i in range(0, len(week)):
        if is_end_week < len(week):
            if week[i] == week[i+1]:
                group_week.append(week[i+1].get('week_no'))
        is_end_week += 1
    print(group_week)
    return group_week

def __group_ids_2(self, group_week):
    is_end_week = 1
    for i in range(0, len(group_week)):
        if is_end_week < len(group_week):
            if group_week[i] == group_week[i+1]:
                return True
            is_end_week += 1
    return False

def __group_ids_3(self, group_week):
    group_week2 = []
    is_end_week2 = 1
    for j in range(0, len(group_week)):
        if is_end_week2 < len(group_week):
            if group_week[j] == group_week[j+1]:
                group_week2.append(group_week[j])
                break
            else:
                group_week2.append(group_week[j])
        is_end_week2 += 1
    print(group_week2)



class GetMostCurrentWeekView(View):
    get_context = Context()
    get_json = Saving_And_Getting_Json()

    def get(self, request, *args, **kwargs):
        get_main_json = self.get_json.get_json_file('get_most_current_weeks_for_stats_table')
        return JsonResponse(get_main_json, safe = False)

    def post(self, request, *args, **kwargs):
        if_is_current_week = self.__save_current_weeks_stats_table(request.POST['get_current_week'])
        self.get_json.save_json(if_is_current_week, 'get_most_current_weeks_for_stats_table')
        context = self.get_context.get_context_most_current_week(request.POST['most_current_week'])
        return render(request, 'admin_update.html', context)

    def __save_current_weeks_stats_table(self, most_current_week):
        current_weeks_all_stats_tables = []
        current_weeks_goals_context = {
            'name': 'current_weeks_goals',
            'current_weeks_goals_stats': list(Goals_table.objects.filter(week_no_id_id = most_current_week).values('id','points','player_id','week_no_id_id')),
        }
        current_weeks_clean_sheets_context = {
            'name': 'current_weeks_clean_sheets',
            'current_weeks_clean_sheets_stats': list(Clean_Sheets_table.objects.filter(week_no_id_id = most_current_week).values('id','points','player_id','week_no_id_id')),
        }
        current_weeks_form_context = {
            'name': 'current_weeks_form',
            'current_weeks_form_stats': list(Form_table.objects.filter(week_no_id_id = most_current_week).values('id','points','player_id','week_no_id_id')),
        }
        current_weeks_goals_assists_context = {
            'name': 'current_weeks_goals_assists',
            'current_weeks_goals_assists_stats': list(Goals_Assist_table.objects.filter(week_no_id_id = most_current_week).values('id','points','player_id','week_no_id_id')),
        }
        current_weeks_man_of_match_context = {
            'name': 'current_weeks_man_of_match',
            'current_weeks_man_of_match_stats': list(Man_of_Match_table.objects.filter(week_no_id_id = most_current_week).values('id','points','player_id','week_no_id_id')),
        }
        current_weeks_own_goals_context = {
            'name': 'current_weeks_own_goals',
            'current_weeks_own_goals_stats': list(Own_Goals_table.objects.filter(week_no_id_id = most_current_week).values('id','points','player_id','week_no_id_id')),
        }
        current_weeks_red_cards_context = {
            'name': 'current_weeks_red_cards',
            'current_weeks_red_cards_stats': list(Red_Card_table.objects.filter(week_no_id_id = most_current_week).values('id','points','player_id','week_no_id_id')),
        }
        current_weeks_yellow_cards_context = {
            'name': 'current_weeks_yellow_cards',
            'current_weeks_yellow_cards_stats': list(Yellow_Card_table.objects.filter(week_no_id_id = most_current_week).values('id','points','player_id','week_no_id_id')),
        }
        current_weeks_all_stats_tables.append(current_weeks_goals_context)
        current_weeks_all_stats_tables.append(current_weeks_clean_sheets_context)
        current_weeks_all_stats_tables.append(current_weeks_form_context)
        current_weeks_all_stats_tables.append(current_weeks_goals_assists_context)
        current_weeks_all_stats_tables.append(current_weeks_man_of_match_context)
        current_weeks_all_stats_tables.append(current_weeks_own_goals_context)
        current_weeks_all_stats_tables.append(current_weeks_red_cards_context)
        current_weeks_all_stats_tables.append(current_weeks_yellow_cards_context)
        return current_weeks_all_stats_tables
