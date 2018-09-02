from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import View, TemplateView, FormView
from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages
from members.forms import *
from members.models import *
from players.models import *
from members.members_team import GetMembersTeam
from admin_updates.saving_and_getting_json import Saving_And_Getting_Json

class MembersView(View):
    def get(self, request, *args, **kwargs):
        get_members_team = GetMembersTeam()
        get_user_id = request.user.id
        request_user = request.user
        if request.user.is_authenticated is False:
            return redirect('login')
        if request.user.is_staff:
            return redirect('logout')
        if Personal_Info_table.objects.filter(has_username = get_user_id):
            check_squad_exist = self.__check_if_squad_exist(get_user_id)
            context = {
                'members_info': True,
                'has_squad': True if len(check_squad_exist) == int(4) else False,
            }
            return render(request, 'members.html', context)
        messages.success(request, 'You need to setup your team name and personal info')
        return redirect('personal_info')

    def __check_if_squad_exist(self, get_user_id):
        check_squad_exist = []
        check_squad_exist.append(1) if Goalkeeper_table.objects.filter(user_id_id = get_user_id) else False
        check_squad_exist.append(1) if Defender_table.objects.filter(user_id_id = get_user_id) else False
        check_squad_exist.append(1) if Midfielder_table.objects.filter(user_id_id = get_user_id) else False
        check_squad_exist.append(1) if Striker_table.objects.filter(user_id_id = get_user_id) else False
        return check_squad_exist

class GetRightMemberView(View):
    def get(self, request, *args, **kwargs):
        get_main_json = []
        get_members_team = GetMembersTeam()
        save_to_json = Saving_And_Getting_Json()
        get_members_team.check_request(request.user.id, request.user)
        get_member = Members_table.objects.all()
        return_get_member = get_members_team.get_right_member(get_member, request.user.id)
        get_latest_week = Week_table.objects.latest('week_no')
        context = {
            'username': str(request.user),
            'user_id': return_get_member[0][0].get('user_id_id'),
            'profit_gained_players_sold': return_get_member[0][0].get('profit_gained_players_sold'),
            'boolean_team_points': return_get_member[0][0].get('boolean_team_points'),
            'date_updated': return_get_member[0][0].get('date_updated'),
            'total_cost_players_bought': return_get_member[0][0].get('total_cost_players_bought'),
            'credits_left': return_get_member[0][0].get('credits_left'),
            'prize_money_minus_bought_sold': return_get_member[0][0].get('prize_money_minus_bought_sold'),
            'calculate_team_points': return_get_member[0][0].get('calculate_team_points'),
        }
        context_player = {
            'player_1': return_get_member[2][0],
            'player_2': return_get_member[2][1],
            'player_3': return_get_member[2][2],
            'player_4': return_get_member[2][3],
        }
        context_latest_week = {'week': str(get_latest_week),}
        save_to_json.save_json(context, 'members_team_info')
        save_to_json.save_json(context_player, 'members_player_info')
        save_to_json.save_json(context_latest_week, 'get_latest_week')
        get_main_json.append(save_to_json.get_json_file('members_team_info'))
        get_main_json.append(save_to_json.get_json_file('members_player_info'))
        get_main_json.append(save_to_json.get_json_file('get_latest_week'))
        return JsonResponse(get_main_json, safe = False)

    def post(self, request, *args, **kwargs):
        '''
        This has to do with team formation
        '''
        player_ids = request.POST.getlist('player_id')
        print(player_ids)
        return HttpResponse('Hello')

class SquadView(View):
    def get(self, request, *args, **kwargs):
        team_name = Personal_Info_table.objects.filter(has_username = request.user.id).values_list('team_name')
        credits = Members_table.objects.filter(user_id = request.user.id).values_list('credits_left')
        players = Player_table.objects.all().values('id','player_name','player_position_1','player_position_2','player_position_3','current_player_value','is_player_not_playing')
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
            self.__setup_squad(list_of_players, request.user.id)
            messages.success(request, 'You have successfully added your team')
        return redirect('members')

    def __setup_squad(self, list_of_players, get_user_id):
        for i in range(0, len(list_of_players)):
            if Player_table.objects.filter(id = list_of_players[i]):
                get_position = Player_table.objects.filter(id = list_of_players[i]).values_list('player_position_1')[0]
            if str(get_position[0]) == str('Goalkeeper'):
                save_players = Goalkeeper_table.objects.create(player_id_id = list_of_players[i], user_id_id = get_user_id)
                save_players.save()
            if str(get_position[0]) == str('Defender'):
                save_players = Defender_table.objects.create(player_id_id = list_of_players[i], user_id_id = get_user_id)
                save_players.save()
            if str(get_position[0]) == str('Midfielder'):
                save_players = Midfielder_table.objects.create(player_id_id = list_of_players[i], user_id_id = get_user_id)
                save_players.save()
            if str(get_position[0]) == str('Forward'):
                save_players = Striker_table.objects.create(player_id_id = list_of_players[i], user_id_id = get_user_id)
                save_players.save()


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
