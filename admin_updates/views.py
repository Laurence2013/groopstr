import os
import json
from django.conf import settings
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User
from django.views.generic import View
from django.shortcuts import HttpResponse, render
from django.contrib import messages
from members.models import *
from players.models import *

class AdminUpdateView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'admin_get_fixtures': True,
        }
        return render(request, 'admin_update.html', context)

class AdminGetFixturesView(View):
    base_dir = settings.BASE_DIR

    def get(self, request, *args, **kwargs):
        week_no = Week_table.objects.values('week_no').latest('week_no')
        self.__save_weekly_fixtures(week_no)
        main_json_file = self.base_dir + '/static/json/get_weekly_fixtures.json'
        try:
            main_json_file_size = os.path.getsize(main_json_file)
            if main_json_file_size > 0:
                 with open(main_json_file) as json_file:
                     weekly_fixtures = json.load(json_file)
        except FileNotFoundError as e:
            print(e)
        return JsonResponse(weekly_fixtures, safe = False)

    def __save_weekly_fixtures(self, week_no):
        fixtures = list(Fixtures_table.objects.all().values('id','fixture')) + list(Week_table.objects.filter(week_no = week_no.get('week_no')).values('week_no','start_date','end_date','fixture_no_id'))
        weekly_fixtures = json.dumps(fixtures, ensure_ascii=False, indent=4, cls=DjangoJSONEncoder)
        with open(self.base_dir + '/static/json/get_weekly_fixtures.json', 'w') as f:
            f.write(weekly_fixtures)
