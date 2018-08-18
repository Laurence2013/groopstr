import os
import json
from django.conf import settings
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User
from django.views.generic import View
from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages
from members.models import *
from players.models import *

class AdminUpdateView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'admin_get_fixtures': True,
            'admin_get_form': True,
        }
        return render(request, 'admin_update.html', context)

class AdminGetFixturesView(View):
    base_dir = settings.BASE_DIR

    def get(self, request, *args, **kwargs):
        week_no = Week_table.objects.values('week_no').latest('week_no')
        fixture_no = Week_table.objects.filter(week_no = week_no.get('week_no')).values('fixture_no_id')
        self.__save_weekly_fixtures(week_no, fixture_no)
        main_json_file = self.base_dir + '/static/json/get_weekly_fixtures.json'
        try:
            main_json_file_size = os.path.getsize(main_json_file)
            if main_json_file_size > 0:
                 with open(main_json_file) as json_file:
                     weekly_fixtures = json.load(json_file)
        except FileNotFoundError as e:
            print(e)
        return JsonResponse(weekly_fixtures, safe = False)

    def __save_weekly_fixtures(self, week_no, fixture_no):
        weekly_fixtures = []
        for i in range(0, len(fixture_no)):
            weekly_fixtures.append(Fixtures_table.objects.filter(id = fixture_no[i].get('fixture_no_id')).values('fixture','id')[0])

        fixtures = weekly_fixtures + list(Week_table.objects.filter(week_no = week_no.get('week_no',)).values('week_no','start_date','end_date','fixture_no_id'))
        weekly_fixtures = json.dumps(fixtures, ensure_ascii=False, indent=4, cls=DjangoJSONEncoder)
        with open(self.base_dir + '/static/json/get_weekly_fixtures.json', 'w') as f:
            f.write(weekly_fixtures)

class AdminGetFormView(View):
    base_dir = settings.BASE_DIR

    def get(self, request, *args, **kwargs):
        get_players = []
        get_form = Form_table.objects.values('player_id','points','total_points','week_no_id_id')
        for i in range(0, len(get_form)):
            get_player = Player_table.objects.filter(id = get_form[i].get('player_id')).values('id','player_name')
            get_players.append(get_player[0])
        self.__save_statistics_table(get_form, get_players)
        main_json_file = self.base_dir + '/static/json/get_weekly_form.json'
        try:
            main_json_file_size = os.path.getsize(main_json_file)
            if main_json_file_size > 0:
                 with open(main_json_file) as json_file:
                     weekly_fixtures = json.load(json_file)
        except FileNotFoundError as e:
            print(e)
        return JsonResponse(weekly_fixtures, safe = False)

    def __save_statistics_table(self, stats_table, get_players):
        for i in range(0, len(stats_table)):
            if stats_table[i].get('id') == get_players[i].get('player_id'):
                stats_table[i].update({'player_name': get_players[i].get('player_name')})

        stats = list(stats_table)
        weekly_stats = json.dumps(stats, ensure_ascii=False, indent=4, cls=DjangoJSONEncoder)
        with open(self.base_dir + '/static/json/get_weekly_form.json', 'w') as f:
            f.write(weekly_stats)

class AdminGetWeeklyFixtures(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Hello')

    def __get_weekly_fixtures(self):
        '''
        1 - Connect fixtures to its correct week before displaying - test_database_tables.Fixtures_and_Weeks class
        '''
        get_weeks = Week_table.object.all().values('id','week_no','start_date','end_date','is_current_week')
        get_fixtures = Fixtures_table.objects.all().values('id','fixture','competition','date_of_game','week_no_id')
