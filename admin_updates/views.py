from django.contrib.auth.models import User
from django.views.generic import View
from django.shortcuts import HttpResponse, render
from django.contrib import messages
from members.models import *
from players.models import *

class AdminUpdateView(View):
    def get(self, request, *args, **kwargs):
        week = Week_table.objects.values('week_no').latest('week_no')
        print(week.get('week_no'))
        return HttpResponse('Hello')

    
