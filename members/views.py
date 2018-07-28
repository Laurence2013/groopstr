from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.views.generic import View, TemplateView, FormView
from django.shortcuts import HttpResponse, render, redirect
from members.forms import *

class MembersView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated is False:
            return redirect('login')
        context = {'username': request.user}
        return render(request, 'members.html', context)

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
        context = {
            'form': form,
            'title': title,
        }
        return render(request, 'register.html', context)

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
                    # return render(request, 'members.html', {'username': username})
        return render(request, 'login.html', {'form': form})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
