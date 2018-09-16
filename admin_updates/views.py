import os
import json
from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User
from django.views.generic import View
from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages
from members.models import *
from players.models import *
from admin_updates.saving_and_getting_json import Saving_And_Getting_Json
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.utils.decorators import method_decorator
from admin_updates.saving_points import Saving_Points
from admin_updates.context import Context
from admin_updates.statistics_tables import Statistics_Tables
from admin_updates.weeks_table import Weeks_Table
from admin_updates.group_tables import Group_Tables

class AdminUpdateView(View):
    get_context = Context()
    get_json = Saving_And_Getting_Json()

    def get(self, request, *args, **kwargs):
        url = request.get_raw_uri()
        is_weeks_set_to = False
        has_this_week_passed = Week_table.objects.values('has_this_week_passed')
        self.__save_most_current_weeks_to_json()
        get_has_week_passed = [has_this_week_passed[i].get('has_this_week_passed') for i in range(0, len(has_this_week_passed))]

        for i in range(0, len(get_has_week_passed)):
            if get_has_week_passed[i] == True:
                is_weeks_set_to = True
                break

        if is_weeks_set_to is True:
            context = self.get_context.get_context(kwargs, kwargs.get('fixtures'), kwargs.get('statistics'))
        if is_weeks_set_to is False:
            context = self.get_context.get_context_false_not_uri(kwargs, kwargs.get('fixtures'))
        if is_weeks_set_to is False and url == "http://localhost:8000/admin_update/statistics/statistics/":
            context = self.get_context.get_context_false(kwargs, kwargs.get('fixtures'), True)
        return render(request, 'admin_update.html', context)

    def __save_most_current_weeks_to_json(self):
        get_weeks = []
        try:
            get_most_current_week = Week_table.objects.filter(has_this_week_passed = 1).values('id','week_no').latest('week_no')
            get_all_passed_week = Week_table.objects.filter(has_this_week_passed = 1).values('id','week_no')
            current_week_context = {'name': 'most_current_week','get_most_current_week': get_most_current_week,}
            get_weeks.append(current_week_context)
            for i in range(0, len(get_all_passed_week)):
                all_weeks_context = {
                    'all_weeks_id': get_all_passed_week[i].get('id'),
                    'all_weeks_week_no': get_all_passed_week[i].get('week_no'),
                }
                get_weeks.append(all_weeks_context)
            self.get_json.save_json(get_weeks, 'get_most_current_weeks_for_stats_table')
        except Exception as e:
            print('Week table has_this_week_passed field are all set to 0 - ',e)

class SetAllStatsTable(View):
    get_json = Saving_And_Getting_Json()

    def get(self, request, *args, **kwargs):
        get_goals_tbl = Statistics_Tables(Goals_table, 'goals_table', 'goals_as_list')
        goals_tbl = get_goals_tbl.set_stats_table()
        get_goalss_tbl = get_goals_tbl.set_to_save(goals_tbl, 'name', 'goals_as_list')

        get_clean_sheets_tbl = Statistics_Tables(Clean_Sheets_table, 'clean_sheets_table', 'clean_sheets_as_list')
        clean_sheets_tbl = get_clean_sheets_tbl.set_stats_table()
        get_clean_sheetss_tbl = get_clean_sheets_tbl.set_to_save(clean_sheets_tbl, 'name', 'clean_sheets_as_list')

        get_form_tbl = Statistics_Tables(Form_table, 'form_table', 'form_as_list')
        form_tbl = get_form_tbl.set_stats_table()
        get_formm_tbl = get_form_tbl.set_to_save(form_tbl, 'name', 'form_as_list')

        get_goals_assist_tbl = Statistics_Tables(Goals_Assist_table, 'goals_assist_table', 'goals_assist_as_list')
        goals_assist_tbl = get_goals_assist_tbl.set_stats_table()
        get_goals_assistt_tbl = get_goals_assist_tbl.set_to_save(goals_assist_tbl, 'name', 'goals_assist_as_list')

        get_man_of_the_match_tbl = Statistics_Tables(Man_of_Match_table, 'man_of_the_match_table', 'man_of_the_match_as_list')
        man_of_the_match_tbl = get_man_of_the_match_tbl.set_stats_table()
        get_man_of_the_matchh_tbl = get_man_of_the_match_tbl.set_to_save(man_of_the_match_tbl, 'name', 'man_of_the_match_as_list')

        get_own_goals_tbl = Statistics_Tables(Own_Goals_table, 'own_goals_table', 'own_goals_as_list')
        own_goals_tbl = get_own_goals_tbl.set_stats_table()
        get_own_goalss_tbl = get_own_goals_tbl.set_to_save(own_goals_tbl, 'name', 'own_goals_as_list')

        get_red_card_tbl = Statistics_Tables(Red_Card_table, 'red_card_table', 'red_card_as_list')
        red_card_tbl = get_red_card_tbl.set_stats_table()
        get_red_cardd_tbl = get_red_card_tbl.set_to_save(red_card_tbl, 'name', 'red_card_as_list')

        get_yellow_card_tbl = Statistics_Tables(Yellow_Card_table, 'yellow_card_table', 'yellow_card_as_list')
        yellow_card_tbl = get_yellow_card_tbl.set_stats_table()
        get_yellow_cardd_tbl = get_yellow_card_tbl.set_to_save(yellow_card_tbl, 'name', 'yellow_card_as_list')

        get_all_weeks = Weeks_Table(None, Week_table, 'weeks')
        all_weeks = get_all_weeks.set_weeks()
        get_all_weekss = get_all_weeks.set_to_save(all_weeks)

        group_tbl = Group_Tables(get_goalss_tbl, get_clean_sheetss_tbl, get_formm_tbl, get_goals_assistt_tbl, get_man_of_the_matchh_tbl, get_own_goalss_tbl, get_red_cardd_tbl, get_yellow_cardd_tbl, get_all_weekss, 'statistics_page')
        group_tbll =  group_tbl.set_group_table()
        if group_tbll is False:
            messages.error(request, 'Something went wrong!')
        return render(request, 'admin_update.html', {'get_all_stats': True})
        # return redirect('admin_update', weeks_stats='get_all_stats')

class GetAllStatsTable(View):
    get_json = Saving_And_Getting_Json()

    def get(self, request, *args, **kwargs):
        get_main_json = self.get_json.get_json_file('statistics_page')
        return JsonResponse(get_main_json, safe = False)

class GetMostCurrentWeekView(View):
    get_json = Saving_And_Getting_Json()

    def get(self, request, *args, **kwargs):
        get_main_json = self.get_json.get_json_file('get_most_current_weeks_for_stats_table')
        return JsonResponse(get_main_json, safe = False)

class CalculateUserTotalPoints(View):
    get_json = Saving_And_Getting_Json()

    def get(self, request, *args, **kwargs):
        user_players_points = []
        get_all_user_ids = User.objects.filter(is_superuser = 0).values('id','username')
        for i in range(0 ,len(get_all_user_ids)):
            if Goalkeeper_table.objects.filter(user_id_id = get_all_user_ids[i].get('id')) and Defender_table.objects.filter(user_id_id = get_all_user_ids[i].get('id')) and Midfielder_table.objects.filter(user_id_id = get_all_user_ids[i].get('id')) and Striker_table.objects.filter(user_id_id = get_all_user_ids[i].get('id')):
                get_gk_points = Goalkeeper_table.objects.filter(user_id_id = get_all_user_ids[i].get('id')).values('players_points')[0]
                get_df_points = Defender_table.objects.filter(user_id_id = get_all_user_ids[i].get('id')).values('players_points')[0]
                get_mf_points = Midfielder_table.objects.filter(user_id_id = get_all_user_ids[i].get('id')).values('players_points')[0]
                get_fw_points = Striker_table.objects.filter(user_id_id = get_all_user_ids[i].get('id')).values('players_points')[0]
                total_player_points = get_gk_points.get('players_points') + get_df_points.get('players_points') + get_mf_points.get('players_points') + get_fw_points.get('players_points')
                context = {
                    'user_id': get_all_user_ids[i].get('id'),
                    'total_players_points': total_player_points,
                }
                user_players_points.append(context)
        is_saved = self.__save_players_total_points(user_players_points)
        if is_saved is False:
            messages.error(request, 'Something went wrong when calculating all players points')
            return redirect('admin_update')
        self.__save_to_json_file('user_total_players_points')
        get_main_json = self.get_json.get_json_file('user_total_players_points')
        return JsonResponse(get_main_json, safe = False)

    def __save_to_json_file(self, json_file_name):
        user_total_points = []
        get_user_points = Members_table.objects.values('id','user_id_id','calculate_team_points')
        for i in range(0, len(get_user_points)):
            context = {
                'id': get_user_points[i].get('id'),
                'user_id': get_user_points[i].get('user_id_id'),
                'user_team_points': get_user_points[i].get('calculate_team_points'),
            }
            user_total_points.append(context)
        self.get_json.save_json(user_total_points, json_file_name)

    def __save_players_total_points(self, total_points):
        for i in range(0, len(total_points)):
            if Members_table.objects.filter(user_id_id = total_points[i].get('user_id')):
                Members_table.objects.filter(user_id_id = total_points[i].get('user_id')).update(calculate_team_points = total_points[i].get('total_players_points'))
        '''
        Add some time update validation here when returning
        '''
        return True

class SortPointsForPlayers(View):
    get_json = Saving_And_Getting_Json()

    def get(self, request, *args, **kwargs):
        get_main_json = []
        self.__save_players_points(Goalkeeper_table)
        self.__save_players_points(Defender_table)
        self.__save_players_points(Midfielder_table)
        self.__save_players_points(Striker_table)
        '''
        Save Squad tables into json
        '''
        self.__save_squad_points_to_json(Goalkeeper_table.objects.values('id','user_id_id', 'player_id_id','players_points'), 'goalkeepers_points','Goalkeepers')
        self.__save_squad_points_to_json(Defender_table.objects.values('id','user_id_id', 'player_id_id','players_points'), 'defenders_points', 'Defenders')
        self.__save_squad_points_to_json(Midfielder_table.objects.values('id','user_id_id', 'player_id_id','players_points'), 'midfielders_points', 'Midfielders')
        self.__save_squad_points_to_json(Striker_table.objects.values('id','user_id_id', 'player_id_id','players_points'), 'forwards_points', 'Forwards')
        '''
        Show message here that it has been a success
        '''
        messages.success(request, 'All Goalkeepers, Defenders, Midfielders, Forwards table have been updated and saved into Json')
        get_main_json.append(self.get_json.get_json_file('goalkeepers_points'))
        get_main_json.append(self.get_json.get_json_file('defenders_points'))
        get_main_json.append(self.get_json.get_json_file('midfielders_points'))
        get_main_json.append(self.get_json.get_json_file('forwards_points'))
        return JsonResponse(get_main_json, safe = False)

    def __save_squad_points_to_json(self, squad_table, json_file_name, position):
        context_list = []
        for i in range(0, len(squad_table)):
            context = {
                'position': position,
                'id': squad_table[i].get('id'),
                'player_id_id': squad_table[i].get('player_id_id'),
                'user_id_id': squad_table[i].get('user_id_id'),
                'players_points': squad_table[i].get('players_points'),
            }
            context_list.append(context)
        self.get_json.save_json(context_list, json_file_name)

    def __save_players_points(self, stats_table_name):
        '''
        7 - From squad tables get members IDs and Player IDs
        '''
        get_points = stats_table_name.objects.all().values('player_id_id','user_id_id')
        '''
        7(i) - Go to player table, get players points according to ID of players
        '''
        for i in range(0, len(get_points)):
            get_player_points = Player_table.objects.filter(id = get_points[i].get('player_id_id')).values('total_points')
            '''
            7(ii) - Get point and save into Squad tables player_points according to user ID
            '''
            stats_table_name.objects.filter(user_id_id = get_points[i].get('user_id_id')).update(players_points = get_player_points[0].get('total_points'))

class AdminGetGoalkeepers(View):
    def get(self, request, *args, **kwargs):
        '''
        6 - Sort players in their position, goalkeeper, defender, midfielder and striker, then save into json files
        '''
        get_json = Saving_And_Getting_Json()
        goalkeeper = Player_table.objects.filter(player_position_1 = 'Goalkeeper').values('id')

        get_form_points = get_json.get_sum_of_points(goalkeeper, Form_table)
        get_goals_points = get_json.get_sum_of_points(goalkeeper, Goals_table)
        get_goals_assist_points = get_json.get_sum_of_points(goalkeeper, Goals_Assist_table)
        get_man_of_match_points = get_json.get_sum_of_points(goalkeeper, Man_of_Match_table)
        get_own_goal_points = get_json.get_sum_of_points(goalkeeper, Own_Goals_table)
        get_yellow_card_points = get_json.get_sum_of_points(goalkeeper, Yellow_Card_table)
        get_red_card_points = get_json.get_sum_of_points(goalkeeper, Red_Card_table)
        get_clean_sheets_points = get_json.get_sum_of_points(goalkeeper, Clean_Sheets_table)

        get_context = get_json.get_final_total_points(goalkeeper, get_form_points, get_goals_points, get_goals_assist_points, get_man_of_match_points, get_own_goal_points, get_yellow_card_points, get_red_card_points, get_clean_sheets_points)

        for i in range(0, len(get_context)):
            Player_table.objects.filter(id = get_context[i].get('id')).update(total_points = get_context[i].get('total_points'))

        get_goalkeeper = Player_table.objects.filter(player_position_1 = 'Goalkeeper').values('id','player_name','current_player_value',
        'real_football_team','player_position_1','is_player_not_playing','total_points')

        get_gk = get_json.get_players_positions(get_goalkeeper)
        get_json.save_json(get_gk, 'goalkeepers')

        get_main_json = get_json.get_json_file('goalkeepers')
        return JsonResponse(get_main_json, safe = False)

class AdminGetDefenders(View):
    def get(self, request, *args, **kwargs):
        '''
        6 - Sort players in their position, goalkeeper, defender, midfielder and striker, then save into json files
        '''
        get_json = Saving_And_Getting_Json()
        defenders = Player_table.objects.filter(player_position_1 = 'Defender').values('id')

        get_form_points = get_json.get_sum_of_points(defenders, Form_table)
        get_goals_points = get_json.get_sum_of_points(defenders, Goals_table)
        get_goals_assist_points = get_json.get_sum_of_points(defenders, Goals_Assist_table)
        get_man_of_match_points = get_json.get_sum_of_points(defenders, Man_of_Match_table)
        get_own_goal_points = get_json.get_sum_of_points(defenders, Own_Goals_table)
        get_yellow_card_points = get_json.get_sum_of_points(defenders, Yellow_Card_table)
        get_red_card_points = get_json.get_sum_of_points(defenders, Red_Card_table)
        get_clean_sheets_points = get_json.get_sum_of_points(defenders, Clean_Sheets_table)

        get_context = get_json.get_final_total_points(defenders, get_form_points, get_goals_points, get_goals_assist_points, get_man_of_match_points, get_own_goal_points, get_yellow_card_points, get_red_card_points, get_clean_sheets_points)

        for i in range(0, len(get_context)):
            Player_table.objects.filter(id = get_context[i].get('id')).update(total_points = get_context[i].get('total_points'))

        get_defenders = Player_table.objects.filter(player_position_1 = 'Defender').values('id','player_name','current_player_value',
        'real_football_team','player_position_1','is_player_not_playing','total_points')

        get_df = get_json.get_players_positions(get_defenders)
        get_json.save_json(get_df, 'defenders')

        get_main_json = get_json.get_json_file('defenders')
        return JsonResponse(get_main_json, safe = False)

class AdminGetMidfielders(View):
    def get(self, request, *args, **kwargs):
        '''
        6 - Sort players in their position, goalkeeper, defender, midfielder and striker, then save into json files
        '''
        get_json = Saving_And_Getting_Json()
        midfielders = Player_table.objects.filter(player_position_1 = 'Midfielder').values('id')

        get_form_points = get_json.get_sum_of_points(midfielders, Form_table)
        get_goals_points = get_json.get_sum_of_points(midfielders, Goals_table)
        get_goals_assist_points = get_json.get_sum_of_points(midfielders, Goals_Assist_table)
        get_man_of_match_points = get_json.get_sum_of_points(midfielders, Man_of_Match_table)
        get_own_goal_points = get_json.get_sum_of_points(midfielders, Own_Goals_table)
        get_yellow_card_points = get_json.get_sum_of_points(midfielders, Yellow_Card_table)
        get_red_card_points = get_json.get_sum_of_points(midfielders, Red_Card_table)
        get_clean_sheets_points = get_json.get_sum_of_points(midfielders, Clean_Sheets_table)

        get_context = get_json.get_final_total_points(midfielders, get_form_points, get_goals_points, get_goals_assist_points, get_man_of_match_points, get_own_goal_points, get_yellow_card_points, get_red_card_points, get_clean_sheets_points)

        for i in range(0, len(get_context)):
            Player_table.objects.filter(id = get_context[i].get('id')).update(total_points = get_context[i].get('total_points'))

        get_midfielders = Player_table.objects.filter(player_position_1 = 'Midfielder').values('id','player_name','current_player_value',
        'real_football_team','player_position_1','is_player_not_playing','total_points')

        get_md = get_json.get_players_positions(get_midfielders)
        get_json.save_json(get_md, 'midfielders')

        get_main_json = get_json.get_json_file('midfielders')
        return JsonResponse(get_main_json, safe = False)

class AdminGetForwards(View):
    def get(self, request, *args, **kwargs):
        '''
        6 - Sort players in their position, goalkeeper, defender, midfielder and striker, then save into json files
        '''
        get_json = Saving_And_Getting_Json()
        forwards = Player_table.objects.filter(player_position_1 = 'Forward').values('id')

        get_form_points = get_json.get_sum_of_points(forwards, Form_table)
        get_goals_points = get_json.get_sum_of_points(forwards, Goals_table)
        get_goals_assist_points = get_json.get_sum_of_points(forwards, Goals_Assist_table)
        get_man_of_match_points = get_json.get_sum_of_points(forwards, Man_of_Match_table)
        get_own_goal_points = get_json.get_sum_of_points(forwards, Own_Goals_table)
        get_yellow_card_points = get_json.get_sum_of_points(forwards, Yellow_Card_table)
        get_red_card_points = get_json.get_sum_of_points(forwards, Red_Card_table)
        get_clean_sheets_points = get_json.get_sum_of_points(forwards, Clean_Sheets_table)

        get_context = get_json.get_final_total_points(forwards, get_form_points, get_goals_points, get_goals_assist_points, get_man_of_match_points, get_own_goal_points, get_yellow_card_points, get_red_card_points, get_clean_sheets_points)

        for i in range(0, len(get_context)):
            Player_table.objects.filter(id = get_context[i].get('id')).update(total_points = get_context[i].get('total_points'))

        get_forwards = Player_table.objects.filter(player_position_1 = 'Forward').values('id','player_name','current_player_value',
        'real_football_team','player_position_1','is_player_not_playing','total_points')

        get_md = get_json.get_players_positions(get_forwards)
        get_json.save_json(get_md, 'forwards')

        get_main_json = get_json.get_json_file('forwards')
        return JsonResponse(get_main_json, safe = False)

class AdminGetGoalsView(View):
    def get(self, request, *args, **kwargs):
        get_json = Saving_And_Getting_Json()
        get_main_json = get_json.get_json_file('goals_stats_tables')
        return JsonResponse(get_main_json, safe = False)

    def post(self, request, *args, **kwargs):
        '''
        5 - Enter new points to the right player in the right week for example if week 8, then make sure it is week 8, right player id, then ad points
        '''
        saving_points = Saving_Points()
        goals_player = []
        goals_player.append({'week_no': request.POST.get('week_no')})
        goals = request.POST.getlist('goals')
        player_id = request.POST.getlist('player_id')
        points_is_saved = saving_points.save_points(goals_player, goals, player_id, Goals_table)
        if points_is_saved is True:
            messages.success(request, 'Goals table for week '+ request.POST.get('week_no') +' has been updated')
        else:
            messages.error(request, 'Something went wrong when updating '+ request.POST.get('week_no') +', please revisit the error')
        return redirect('admin_update')

class AdminGetGoalsAssistView(View):
    def get(self, request, *args, **kwargs):
        get_json = Saving_And_Getting_Json()
        get_main_json = get_json.get_json_file('goals_assist_stats_tables')
        return JsonResponse(get_main_json, safe = False)

    def post(self, request, *args, **kwargs):
        '''
        5 - Enter new points to the right player in the right week for example if week 8, then make sure it is week 8, right player id, then add points
        '''
        saving_points = Saving_Points()
        goals_player = []
        goals_player.append({'week_no': request.POST.get('week_no')})
        goals_assists = request.POST.getlist('goals_assists')
        player_id = request.POST.getlist('player_id')
        points_is_saved = saving_points.save_points(goals_player, goals_assists, player_id, Goals_Assist_table)
        if points_is_saved is True:
            messages.success(request, 'Goals Assists table for week '+ request.POST.get('week_no') +' has been updated')
        else:
            messages.error(request, 'Something went wrong when updating '+ request.POST.get('week_no') +', please revisit the error')
        return redirect('admin_update')

class AdminManOfTheMatchView(View):
    def get(self, request, *args, **kwargs):
        get_json = Saving_And_Getting_Json()
        get_main_json = get_json.get_json_file('man_of_the_match_tables')
        return JsonResponse(get_main_json, safe = False)

    def post(self, request, *args, **kwargs):
        '''
        5 - Enter new points to the right player in the right week for example if week 8, then make sure it is week 8, right player id, then ad points
        '''
        saving_points = Saving_Points()
        goals_player = []
        goals_player.append({'week_no': request.POST.get('week_no')})
        man_of_the_match = request.POST.getlist('man_of_the_match')
        player_id = request.POST.getlist('player_id')
        points_is_saved = saving_points.save_points(goals_player, man_of_the_match, player_id, Man_of_Match_table)
        if points_is_saved is True:
            messages.success(request, 'Man of the Match table for week '+ request.POST.get('week_no') +' has been updated')
        else:
            messages.error(request, 'Something went wrong when updating '+ request.POST.get('week_no') +', please revisit the error')
        return redirect('admin_update')

class AdminOwnGoalsView(View):
    def get(self, request, *args, **kwargs):
        get_json = Saving_And_Getting_Json()
        get_main_json = get_json.get_json_file('own_goals_tables')
        return JsonResponse(get_main_json, safe = False)

    def post(self, request, *args, **kwargs):
        '''
        5 - Enter new points to the right player in the right week for example if week 8, then make sure it is week 8, right player id, then ad points
        '''
        saving_points = Saving_Points()
        goals_player = []
        goals_player.append({'week_no': request.POST.get('week_no')})
        own_goals = request.POST.getlist('own_goals')
        player_id = request.POST.getlist('player_id')
        points_is_saved = saving_points.save_points(goals_player, own_goals, player_id, Own_Goals_table)
        if points_is_saved is True:
            messages.success(request, 'Own Goals table for week '+ request.POST.get('week_no') +' has been updated')
        else:
            messages.error(request, 'Something went wrong when updating '+ request.POST.get('week_no') +', please revisit the error')
        return redirect('admin_update')

class AdminYellowCardsView(View):
    def get(self, request, *args, **kwargs):
        get_json = Saving_And_Getting_Json()
        get_main_json = get_json.get_json_file('yellow_cards')
        return JsonResponse(get_main_json, safe = False)

    def post(self, request, *args, **kwargs):
        '''
        5 - Enter new points to the right player in the right week for example if week 8, then make sure it is week 8, right player id, then ad points
        '''
        saving_points = Saving_Points()
        goals_player = []
        goals_player.append({'week_no': request.POST.get('week_no')})
        yellow_cards = request.POST.getlist('yellow_cards')
        player_id = request.POST.getlist('player_id')
        points_is_saved = saving_points.save_points(goals_player, yellow_cards, player_id, Yellow_Card_table)
        if points_is_saved is True:
            messages.success(request, 'Yellow Card table for week '+ request.POST.get('week_no') +' has been updated')
        else:
            messages.error(request, 'Something went wrong when updating '+ request.POST.get('week_no') +', please revisit the error')
        return redirect('admin_update')

class AdminRedCardsView(View):
    def get(self, request, *args, **kwargs):
        get_json = Saving_And_Getting_Json()
        get_main_json = get_json.get_json_file('red_cards')
        return JsonResponse(get_main_json, safe = False)

    def post(self, request, *args, **kwargs):
        '''
        5 - Enter new points to the right player in the right week for example if week 8, then make sure it is week 8, right player id, then ad points
        '''
        saving_points = Saving_Points()
        goals_player = []
        goals_player.append({'week_no': request.POST.get('week_no')})
        red_cards = request.POST.getlist('red_cards')
        player_id = request.POST.getlist('player_id')
        points_is_saved = saving_points.save_points(goals_player, red_cards, player_id, Red_Card_table)
        if points_is_saved is True:
            messages.success(request, 'Red Card table for week '+ request.POST.get('week_no') +' has been updated')
        else:
            messages.error(request, 'Something went wrong when updating '+ request.POST.get('week_no') +', please revisit the error')
        return redirect('admin_update')

class AdminCleanSheetsView(View):
    def get(self, request, *args, **kwargs):
        get_json = Saving_And_Getting_Json()
        get_main_json = get_json.get_json_file('clean_sheets')
        return JsonResponse(get_main_json, safe = False)

    def post(self, request, *args, **kwargs):
        '''
        5 - Enter new points to the right player in the right week for example if week 8, then make sure it is week 8, right player id, then ad points
        '''
        saving_points = Saving_Points()
        goals_player = []
        goals_player.append({'week_no': request.POST.get('week_no')})
        clean_sheets = request.POST.getlist('clean_sheets')
        player_id = request.POST.getlist('player_id')
        points_is_saved = saving_points.save_points(goals_player, clean_sheets, player_id, Clean_Sheets_table)
        if points_is_saved is True:
            messages.success(request, 'Clean Sheets table for week '+ request.POST.get('week_no') +' has been updated')
        else:
            messages.error(request, 'Something went wrong when updating '+ request.POST.get('week_no') +', please revisit the error')
        return redirect('admin_update')

class AdminFormView(View):
    def get(self, request, *args, **kwargs):
        get_json = Saving_And_Getting_Json()
        get_main_json = get_json.get_json_file('form')
        return JsonResponse(get_main_json, safe = False)

    def post(self, request, *args, **kwargs):
        '''
        5 - Enter new points to the right player in the right week for example if week 8, then make sure it is week 8, right player id, then ad points
        '''
        saving_points = Saving_Points()
        goals_player = []
        goals_player.append({'week_no': request.POST.get('week_no')})
        form = request.POST.getlist('form')
        player_id = request.POST.getlist('player_id')
        points_is_saved = saving_points.save_points(goals_player, form, player_id, Form_table)
        if points_is_saved is True:
            messages.success(request, 'Form table for week '+ request.POST.get('week_no') +' has been updated')
        else:
            messages.error(request, 'Something went wrong when updating '+ request.POST.get('week_no') +', please revisit the error')
        return redirect('admin_update')

class AdminGetCurrentWeek(View):
    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        '''
        4 - Get Admin to check (using radio button) the most current week save it to all statistics tables -> forms, goals, goal_assist, red_cards etc
        '''
        try:
            get_week = request.POST['which_check_week']
            '''
            4(i) - Get all players id add first time or again in all statistics table with new pk and new week number
            '''
            get_players = Player_table.objects.all().values('id')
            # self.__save_into_stats_table(Goals_Assist_table, get_players, get_week)
            # self.__save_into_stats_table(Goals_table, get_players, get_week)
            # self.__save_into_stats_table(Man_of_Match_table, get_players, get_week)
            # self.__save_into_stats_table(Own_Goals_table, get_players, get_week)
            # self.__save_into_stats_table(Yellow_Card_table, get_players, get_week)
            # self.__save_into_stats_table(Red_Card_table, get_players, get_week)
            # self.__save_into_stats_table(Clean_Sheets_table, get_players, get_week)
            # self.__save_into_stats_table(Form_table, get_players, get_week)
            return redirect('get_stats_table', get_week)
        except Exception as e:
            print(e)
        messages.error(request, 'You need to choose which week should be current')
        return redirect('admin_update')

    def __save_into_stats_table(self, stats_table_name, get_players, get_week):
        for i in range(0, len(get_players)):
            save_players = stats_table_name.objects.create(points = None, player_id = get_players[i].get('id'), week_no_id_id = get_week)
            save_players.save()

class AdminGetStatsTables(View):
    def get(self, request, *args, **kwargs):
        get_week = Week_table.objects.filter(has_this_week_passed = 0).values('id','week_no')
        if len(get_week) >= 1:
            get_json = Saving_And_Getting_Json()
            '''
            4(i) - Get all players id add first time or again in all statistics table with new pk and new week number
            '''
            goals = Goals_table.objects.filter(week_no_id_id = kwargs.get('week_no')).values('id','points','player_id','week_no_id_id')
            goals_assists = Goals_Assist_table.objects.filter(week_no_id_id = kwargs.get('week_no')).values('id','points','player_id','week_no_id_id')
            man_of_the_match = Man_of_Match_table.objects.filter(week_no_id_id = kwargs.get('week_no')).values('id','points','player_id','week_no_id_id')
            own_goals = Own_Goals_table.objects.filter(week_no_id_id = kwargs.get('week_no')).values('id','points','player_id','week_no_id_id')
            yellow_cards = Yellow_Card_table.objects.filter(week_no_id_id = kwargs.get('week_no')).values('id','points','player_id','week_no_id_id')
            red_cards = Red_Card_table.objects.filter(week_no_id_id = kwargs.get('week_no')).values('id','points','player_id','week_no_id_id')
            clean_sheets = Clean_Sheets_table.objects.filter(week_no_id_id = kwargs.get('week_no')).values('id','points','player_id','week_no_id_id')
            form = Form_table.objects.filter(week_no_id_id = kwargs.get('week_no')).values('id','points','player_id','week_no_id_id')

            get_goals = self.__get_stats_goals_table(goals, 'Goals')
            get_goals_assist = self.__get_stats_goals_table(goals_assists, 'Goals Assist')
            get_man_of_the_match = self.__get_stats_goals_table(man_of_the_match, 'Man of the Match')
            get_own_goals = self.__get_stats_goals_table(own_goals, 'Own goals')
            get_yellow_cards = self.__get_stats_goals_table(yellow_cards, 'Yellow Cards')
            get_red_cards = self.__get_stats_goals_table(red_cards, 'Red Cards')
            get_clean_sheets = self.__get_stats_goals_table(clean_sheets, 'Clean Sheets')
            get_form = self.__get_stats_goals_table(form, 'Form')

            get_json.save_json(get_goals, 'goals_stats_tables')
            get_json.save_json(get_goals_assist,'goals_assist_stats_tables')
            get_json.save_json(get_man_of_the_match,'man_of_the_match_tables')
            get_json.save_json(get_own_goals,'own_goals_tables')
            get_json.save_json(get_yellow_cards,'yellow_cards')
            get_json.save_json(get_red_cards,'red_cards')
            get_json.save_json(get_clean_sheets,'clean_sheets')
            get_json.save_json(get_form,'form')

            Week_table.objects.filter(id = kwargs.get('week_no')).update(has_this_week_passed = 1)
            messages.success(request, 'Weeks have been currently updated')
            # return redirect('admin_update', week_no = kwargs.get('week_no'))
            return redirect('admin_update')
        messages.error(request, 'All the weeks had been checked, you need to go to the database in Weeks table to sort it out')
        return redirect('admin_update')

    def __get_stats_goals_table(self, goals, table_name):
        goals_table = []
        goals_table.append({'table_name': table_name})
        players = Player_table.objects.all().values('id','player_name')
        for i in range(0, len(goals)):
            for j in range(0, len(players)):
                if goals[i].get('player_id') == players[j].get('id'):
                    context = {
                        'id': goals[i].get('id'),
                        'player_id': goals[i].get('player_id'),
                        'player_name': players[j].get('player_name'),
                        'points': goals[i].get('points'),
                        'week_no_id_id': goals[i].get('week_no_id_id'),
                    }
            goals_table.append(context)
        return goals_table

class AdminGetFixtures(View):
    base_dir = settings.BASE_DIR

    def get(self, request, *args, **kwargs):
        get_json = Saving_And_Getting_Json()
        get_weekly_fixtures = 'get_weekly_fixtures'
        '''
        3 - Show admin all the weeks for the season and future competitions within the season
        '''
        get_main_json = get_json.get_json_file(get_weekly_fixtures)
        return JsonResponse(get_main_json, safe = False)

class AdminGetWeeklyFixtures(View):
    def get(self, request, *args, **kwargs):
        get_json = Saving_And_Getting_Json()
        get_weekly_fixtures = 'get_weekly_fixtures'
        get_all_weeks = 'get_all_weeks'
        get_week_fixtures = self.__get_weekly_fixtures()
        week_fixture = self.__set_fixtures_and_week(get_week_fixtures)
        '''
        2 - Show all Weeks in Week_table and display in Admin page - show has_this_week_passed - so admin can check which one should be current
        2(i) - Save into json format
        '''
        get_json.save_json(week_fixture, get_weekly_fixtures)
        '''
        3 - Show admin all the weeks for the season and future competitions within the season
        '''
        get_weeks = self.__show_all_weeks()
        get_json.save_json(get_weeks, get_all_weeks)
        get_main_json = get_json.get_json_file(get_all_weeks)
        return JsonResponse(get_main_json, safe = False)

    def __show_all_weeks(self):
        week = []
        get_weeks = Week_table.objects.all().values('id','week_no','start_date','end_date','has_this_week_passed')
        for i in range(0, len(get_weeks)):
            context = {
                'id': get_weeks[i].get('id'),
                'week_no': get_weeks[i].get('week_no'),
                'start_date': get_weeks[i].get('start_date'),
                'end_date': get_weeks[i].get('end_date'),
                'has_this_week_passed': get_weeks[i].get('has_this_week_passed'),
            }
            week.append(context)
        return week

    def __get_weekly_fixtures(self):
        '''
        1 - Connect fixtures to its correct week before displaying - test_database_tables.Fixtures_and_Weeks class
        '''
        get_weeks = Week_table.objects.all().values('id','week_no','start_date','end_date','has_this_week_passed')
        get_fixtures = Fixtures_table.objects.all().values('id','fixture','competition','date_of_game','week_no_id')
        return get_weeks, get_fixtures

    def __set_fixtures_and_week(self, get_week_fixtures):
        '''
        1 - Connect fixtures to its correct week before displaying - test_database_tables.Fixtures_and_Weeks.set_fixtures_and_week()
        '''
        week_fixture = []
        for i in range(0, len(get_week_fixtures[0])):
            for j in range(0, len(get_week_fixtures[1])):
                if get_week_fixtures[0][i].get('id') == get_week_fixtures[1][j].get('week_no_id'):
                    context = {
                        'fixture': get_week_fixtures[1][j].get('fixture'),
                        'date_of_game': get_week_fixtures[1][j].get('date_of_game'),
                        'competition': get_week_fixtures[1][j].get('competition'),
                        'week_no': get_week_fixtures[0][i].get('week_no'),
                        'start_date': get_week_fixtures[0][i].get('start_date'),
                        'end_date': get_week_fixtures[0][i].get('end_date'),
                        'has_this_week_passed': get_week_fixtures[0][i].get('has_this_week_passed'),
                        'week_id': get_week_fixtures[0][i].get('id'),
                    }
                    week_fixture.append(context)
        return week_fixture
