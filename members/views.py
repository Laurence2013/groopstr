from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.contrib.auth.models import User
from django.views.generic import View, TemplateView, FormView
from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages
from members.forms import *
from members.models import *

class MembersView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated is False:
            return redirect('login')
        if request.user.is_staff:
            return redirect('logout')
        if Personal_Info_table.objects.filter(has_username = request.user.id):
            context = {'username': request.user}
            return render(request, 'members.html', context)
        return redirect('personal_info')

class PersonalinfoView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated is False:
            return redirect('login')
        if Personal_Info_table.objects.filter(has_username = request.user.id):
            print('hello')
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
        # return redirect('login')
