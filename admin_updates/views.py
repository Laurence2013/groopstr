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

class AdminUpdateView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'get_week': True if Week_table.objects.all().count() > 0 else False,
            'get_fixtures': True if Fixtures_table.objects.all().count() > 0 else False,
            'get_goals_table': True if kwargs.get('week_no') else False,
            'get_goals_assist_table': True if kwargs.get('week_no') else False,
            'get_man_of_the_match_table': True if kwargs.get('week_no') else False,
            'get_own_goals': True if kwargs.get('week_no') else False,
            'get_yellow_cards': True if kwargs.get('week_no') else False,
            'get_red_cards': True if kwargs.get('week_no') else False,
            'get_clean_sheets': True if kwargs.get('week_no') else False,
            'get_form': True if kwargs.get('week_no') else False,
            'get_goalkeepers': True,
        }
        return render(request, 'admin_update.html', context)

class AdminGetGoalkeepers(View):
    def get(self, request, *args, **kwargs):
        '''
        6 - Sort players in their position, goalkeeper, defender, midfielder and striker, then save into json files
        '''
        get_json = Saving_And_Getting_Json()
        get_goalkeeper = Player_table.objects.filter(player_position_1 = 'Goalkeeper').values('id','player_name','current_player_value',
        'real_football_team','player_position_1','is_player_not_playing','total_points')

        get_form_points = get_json.get_sum_of_points(get_goalkeeper, Form_table)
        # get_goals_points = get_json.get_sum_of_points(get_goalkeeper, Goals_table)
        # get_goals_assist_points = get_json.get_sum_of_points(get_goalkeeper, Goals_Assist_table)
        # get_man_of_match_points = get_json.get_sum_of_points(get_goalkeeper, Man_of_Match_table)
        # get_own_goal_points = get_json.get_sum_of_points(get_goalkeeper, Own_Goals_table)
        # get_yellow_card_points = get_json.get_sum_of_points(get_goalkeeper, Yellow_Card_table)
        # get_red_card_points = get_json.get_sum_of_points(get_goalkeeper, Red_Card_table)
        # get_clena_sheets_points = get_json.get_sum_of_points(get_goalkeeper, Clean_Sheets_table)

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
        get_defender = Player_table.objects.filter(player_position_1 = 'Defender').values('id','player_name','current_player_value',
        'real_football_team','player_position_1','is_player_not_playing','total_points')

        get_df = get_json.get_players_positions(get_defender)
        get_json.save_json(get_df, 'defenders')
        return HttpResponse('Defenders')

class AdminGetMidfielders(View):
    def get(self, request, *args, **kwargs):
        '''
        6 - Sort players in their position, goalkeeper, defender, midfielder and striker, then save into json files
        '''
        get_json = Saving_And_Getting_Json()
        get_midfielder = Player_table.objects.filter(player_position_1 = 'Midfielder').values('id','player_name','current_player_value',
        'real_football_team','player_position_1','is_player_not_playing','total_points')

        get_mid = get_json.get_players_positions(get_midfielder)
        get_json.save_json(get_mid, 'midfielders')
        return HttpResponse('Midfielders')

class AdminGetForwards(View):
    def get(self, request, *args, **kwargs):
        '''
        6 - Sort players in their position, goalkeeper, defender, midfielder and striker, then save into json files
        '''
        get_json = Saving_And_Getting_Json()
        get_forward = Player_table.objects.filter(player_position_1 = 'Forward').values('id','player_name','current_player_value',
        'real_football_team','player_position_1','is_player_not_playing','total_points')

        get_for = get_json.get_players_positions(get_forward)
        get_json.save_json(get_for, 'forwards')
        return HttpResponse('Forwards')

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
        5 - Enter new points to the right player in the right week for example if week 8, then make sure it is week 8, right player id, then ad points
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

        return redirect('admin_update', week_no = kwargs.get('week_no'))

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
        2 - Show all Weeks in Week_table and display in Admin page - show is_current_week - so admin can check which one should be current
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
        get_weeks = Week_table.objects.all().values('id','week_no','start_date','end_date','is_current_week')
        for i in range(0, len(get_weeks)):
            context = {
                'id': get_weeks[i].get('id'),
                'week_no': get_weeks[i].get('week_no'),
                'start_date': get_weeks[i].get('start_date'),
                'end_date': get_weeks[i].get('end_date'),
                'is_current_week': get_weeks[i].get('is_current_week'),
            }
            week.append(context)
        return week

    def __get_weekly_fixtures(self):
        '''
        1 - Connect fixtures to its correct week before displaying - test_database_tables.Fixtures_and_Weeks class
        '''
        get_weeks = Week_table.objects.all().values('id','week_no','start_date','end_date','is_current_week')
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
                        'is_current_week': get_week_fixtures[0][i].get('is_current_week'),
                        'week_id': get_week_fixtures[0][i].get('id'),
                    }
                    week_fixture.append(context)
        return week_fixture
