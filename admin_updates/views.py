import os
import json
from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect
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
from django.contrib import messages

class AdminUpdateView(View):
    def get(self, request, *args, **kwargs):
        print(kwargs.get('week_no'))
        context = {
            'get_week': True if Week_table.objects.all().count() > 0 else False,
            'get_fixtures': True if Fixtures_table.objects.all().count() > 0 else False,
            'get_goals_table': True if kwargs.get('week_no') else False,
            'get_goals_assist_table': True if kwargs.get('week_no') else False,
        }
        return render(request, 'admin_update.html', context)

class AdminGetGoalsView(View):
    def get(self, request, *args, **kwargs):
        get_json = Saving_And_Getting_Json()
        get_main_json = get_json.get_json_file('goals_stats_tables')
        return JsonResponse(get_main_json, safe = False)

class AdminGetGoalsAssistView(View):
    def get(self, request, *args, **kwargs):
        get_json = Saving_And_Getting_Json()
        get_main_json = get_json.get_json_file('goals_assist_stats_tables')
        return JsonResponse(get_main_json, safe = False)

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

        get_goals = self.__get_stats_goals_table(goals, 'Goals')
        get_goals_assist = self.__get_stats_goals_table(goals_assists, 'Goals Assist')

        get_json.save_json(get_goals, 'goals_stats_tables')
        get_json.save_json(get_goals_assist,'goals_assist_stats_tables')

        return redirect('admin_update', week_no = kwargs.get('week_no'))
        # return HttpResponseRedirect(reverse('admin_update', kwargs = context))

    def __get_stats_goals_table(self, goals, table_name):
        goals_table = []
        goals_table.append({'table_name': table_name})
        for i in range(0, len(goals)):
            context = {
                'id': goals[i].get('id'),
                'player_id': goals[i].get('player_id'),
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
