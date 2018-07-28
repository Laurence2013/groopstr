from django.contrib.auth import (
    authenticate, get_user_model, login, logout
)
from django.views.generic import View, TemplateView, FormView
from django.shortcuts import HttpResponse, render
from members.forms import UserRegisterForm

class RegisterView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        title = 'Register'
        form = UserRegisterForm(request.POST or None)
        context = {
            'form': form,
            'title': title
        }
        return render(request, 'register.html', self.get_context_data(**context))

    def post(self, request, *args, **kwargs):
        print(request.method == 'POST')
        print(request.POST)
        title = 'Register'
        form = UserRegisterForm(request.POST or None)
        context = {
            'form': form,
            'title': title
        }
        return render(request, 'register.html', self.get_context_data(**context))

class LoginView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', self.get_context_data(**kwargs))

class LogoutView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(LogoutView, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return render(request, 'logout.html', self.get_context_data(**kwargs))
