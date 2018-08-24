"""groopstr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from members.views import *
from admin_updates.views import *

urlpatterns = [
    path('admin_update/', AdminUpdateView.as_view(), name='admin_update'),
    path('admin_update/<int:week_no>/', AdminUpdateView.as_view(), name='admin_update'),
    path('admin_update/get_stats_table/<int:week_no>/', AdminGetStatsTables.as_view(), name='get_stats_table'),
    path('admin_update/admin_get_weekly_fixtures/', AdminGetWeeklyFixtures.as_view(), name='admin_get_weekly_fixtures'),
    path('admin_update/<int:week_no>/admin_get_weekly_fixtures/', AdminGetWeeklyFixtures.as_view(), name='admin_get_weekly_fixtures'),
    path('admin_update/admin_get_fixtures/', AdminGetFixtures.as_view(), name='admin_get_fixtures'),
    path('admin_update/<int:week_no>/admin_get_fixtures/', AdminGetFixtures.as_view(), name='admin_get_fixtures'),
    path('admin_update/admin_get_current_week/', AdminGetCurrentWeek.as_view(), name='admin_get_current_week'),
    path('admin_update/<int:week_no>/admin_get_current_week/', AdminGetCurrentWeek.as_view(), name='admin_get_current_week'),
    path('personal_info/', PersonalinfoView.as_view(), name='personal_info'),
    path('members/', MembersView.as_view(), name='members'),
    path('squad/', SquadView.as_view(), name='squad'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
