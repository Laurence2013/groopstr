from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.contrib.auth.models import User
from django.views.generic import View, TemplateView, FormView
from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages
from members.forms import *
from members.models import *
from players.models import *

class MembersView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated is False:
            return redirect('login')
        if request.user.is_staff:
            return redirect('logout')
        if Personal_Info_table.objects.filter(has_username = request.user.id):
            if not Members_table.objects.filter(user_id = request.user.id):
                new_member = Members_table.objects.create(calculate_team_points = 0, credits_left = 200, total_cost_players_bought = 0.00, profit_gained_players_sold = 0.00, prize_money_minus_bought_sold = 0.00, user_id = request.user)
                new_member.save()
            get_member = Members_table.objects.all()
            for i in get_member.values('user_id'):
                if i.get('user_id') is request.user.id:
                    member_info = Members_table.objects.filter(user_id = i.get('user_id')).values()
            if not Squad_table.objects.filter(user_id = request.user.id):
                team_name = Personal_Info_table.objects.filter(has_username = request.user.id).values_list('team_name')
                get_team_name = team_name[0][0]
                get_players = None
            else:
                get_team_name = None
                get_squad = Squad_table.objects.filter(user_id = request.user.id).values_list('player_id', flat = True)
                for i in range(0, len(get_squad)):
                    get_players.append(list(Player_table.objects.filter(id = get_squad[i]).values_list('player_name','player_position_1','player_position_2','player_position_3','current_player_value')))
                
            context = {
                'username': request.user,
                'members': member_info,
                'team_name': get_team_name,
                'players': get_players,
            }
            return render(request, 'members.html', context)
        messages.success(request, 'You need to setup your team name and personal info')
        return redirect('personal_info')

class SquadView(View):
    def get(self, request, *args, **kwargs):
        team_name = Personal_Info_table.objects.filter(has_username = request.user.id).values_list('team_name')
        credits = Members_table.objects.filter(user_id = request.user.id).values_list('credits_left')
        players = Player_table.objects.all().values('id','player_name','player_position_1','player_position_2','player_position_3','current_player_value')
        context = {
            'username': request.user.username,
            'team_name': team_name[0][0],
            'players': players,
            'credits': credits[0][0],
        }
        return render(request, 'squad.html', context)

    def post(self, request, *args, **kwargs):
        if (request.method == 'POST'):
            list_of_players = request.POST.getlist('player')
            for i in range(0, len(list_of_players)):
                if Player_table.objects.filter(id = list_of_players[i]):
                    get_id = Player_table.objects.filter(id = list_of_players[i]).values_list('id', flat=True)[0]
                    # save_players = Squad_table.objects.create(player_id = get_id, user_id = request.user.id)
                    # save_players.save()
        return redirect('members')

class PersonalinfoView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated is False:
            return redirect('login')
        title = 'Personal Info'
        form = PersonalInfoForm()
        return render(request, 'personal_info.html', {'form': form, 'title': title})

    def post(self, request, *args, **kwargs):
        form = PersonalInfoForm(request.POST or None)
        if form.is_valid():
            team_name = form.cleaned_data.get('team_name')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            personal_info = Personal_Info_table.objects.create(team_name=team_name, first_name=first_name, last_name=last_name, has_username=request.user)
            personal_info.save()
            messages.success(request, 'Your team and personal info was successfully added')
            context = {'username': request.user}
            return render(request, 'members.html', context)
        messages.error(request, 'Team name is already in use, choose another one')
        return render(request, 'personal_info.html', {'form': PersonalInfoForm(), 'title': 'Personal Info'})

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        title = 'Register'
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form, 'title': title})

    def post(self, request, *args, **kwargs):
        title = 'Login'
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit = False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username = user.username, password = password)
            login(request, new_user)
            return redirect('login')
        return render(request, 'register.html', context = {'form': form,'title': title,})

class LoginView(View):
    def get(self, request, *args, **kwargs):
        title = 'Login'
        form = UserLoginForm()
        context = {'form': form, 'title': title,}
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            login(request, user)
            if request.user.is_authenticated:
                return redirect('members')
        return render(request, 'login.html', {'form': form})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'logout.html', {})
