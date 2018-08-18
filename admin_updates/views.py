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
from admin_updates.saving_and_getting_json import Saving_And_Getting_Json

class AdminUpdateView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'get_week': True if Week_table.objects.all().count() > 0 else False,
            'get_fixtures': True if Fixtures_table.objects.all().count() > 0 else False,
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
    def get(self, *args, **kwargs):
        get_json = Saving_And_Getting_Json()
        get_weekly_fixtures = 'get_weekly_fixtures'
        get_all_weeks = 'get_all_weeks'
        get_week_fixtures = self.__get_weekly_fixtures()
        week_fixture = self.__set_fixtures_and_week(get_week_fixtures)
        '''
        2 - Show all Weeks in Week_table and display in Admin page - show is_current_week - so admin can check which one should be current
        2a - Save into json format
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
                        'week_no': get_week_fixtures[0][i].get('week_no'),
                    }
                    week_fixture.append(context)
        return week_fixture
