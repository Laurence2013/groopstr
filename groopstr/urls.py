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
    path('admin_update/view_fixtures/<slug:fixtures>/', AdminUpdateView.as_view(), name='view_fixtures'),
    path('admin_update/statistics/<slug:statistics>/', AdminUpdateView.as_view(), name='statistics'),

    path('admin_update/statistics/<slug:statistics>/get_most_current_week/', GetMostCurrentWeekView.as_view(), name='get_most_current_week'),
    path('admin_update/statistics/statistics/most_current_week/', GetMostCurrentWeekView.as_view(), name='most_current_week'),

    path('admin_update/get_stats_table/<int:week_no>/', AdminGetStatsTables.as_view(), name='get_stats_table'),

    path('admin_update/admin_get_weekly_fixtures/', AdminGetWeeklyFixtures.as_view(), name='admin_get_weekly_fixtures'),
    path('admin_update/view_fixtures/<slug:fixtures>/admin_get_weekly_fixtures/', AdminGetWeeklyFixtures.as_view(), name='admin_get_weekly_fixtures'),
    path('admin_update/<int:week_no>/admin_get_weekly_fixtures/', AdminGetWeeklyFixtures.as_view(), name='admin_get_weekly_fixtures'),

    path('admin_update/admin_get_fixtures/', AdminGetFixtures.as_view(), name='admin_get_fixtures'),
    path('admin_update/view_fixtures/<slug:fixtures>/admin_get_fixtures/', AdminGetFixtures.as_view(), name='admin_get_fixtures'),
    path('admin_update/<int:week_no>/admin_get_fixtures/', AdminGetFixtures.as_view(), name='admin_get_fixtures'),

    path('admin_update/admin_get_current_week/', AdminGetCurrentWeek.as_view(), name='admin_get_current_week'),
    path('admin_update/<int:week_no>/admin_get_current_week/', AdminGetCurrentWeek.as_view(), name='admin_get_current_week'),

    path('admin_update/admin_get_goals/', AdminGetGoalsView.as_view(), name='admin_get_goals'),
    path('admin_update/<int:week_no>/admin_get_goals/', AdminGetGoalsView.as_view(), name='admin_get_goals'),
    path('admin_update/statistics/<slug:statistics>/admin_get_goals/', AdminGetGoalsView.as_view(), name='admin_get_goals'),

    path('admin_update/admin_get_goals_assist/', AdminGetGoalsAssistView.as_view(), name='admin_get_goals_assist'),
    path('admin_update/<int:week_no>/admin_get_goals_assist/', AdminGetGoalsAssistView.as_view(), name='admin_get_goals_assist'),
    path('admin_update/statistics/<slug:statistics>/admin_get_goals_assist/', AdminGetGoalsAssistView.as_view(), name='admin_get_goals_assist'),
    #
    path('admin_update/admin_man_of_the_match/', AdminManOfTheMatchView.as_view(), name='admin_man_of_the_match'),
    path('admin_update/<int:week_no>/admin_man_of_the_match/', AdminManOfTheMatchView.as_view(), name='admin_man_of_the_match'),
    path('admin_update/statistics/<slug:statistics>/admin_man_of_the_match/', AdminManOfTheMatchView.as_view(), name='admin_man_of_the_match'),
    #
    # path('admin_update/admin_own_goals/', AdminOwnGoalsView.as_view(), name='admin_own_goals'),
    # path('admin_update/<int:week_no>/admin_own_goals/', AdminOwnGoalsView.as_view(), name='admin_own_goals'),
    #
    # path('admin_update/admin_yellow_cards/', AdminYellowCardsView.as_view(), name='admin_yellow_cards'),
    # path('admin_update/<int:week_no>/admin_yellow_cards/', AdminYellowCardsView.as_view(), name='admin_yellow_cards'),
    #
    # path('admin_update/admin_red_cards/', AdminRedCardsView.as_view(), name='admin_red_cards'),
    # path('admin_update/<int:week_no>/admin_red_cards/', AdminRedCardsView.as_view(), name='admin_red_cards'),
    #
    # path('admin_update/admin_clean_sheets/', AdminCleanSheetsView.as_view(), name='admin_clean_sheets'),
    # path('admin_update/<int:week_no>/admin_clean_sheets/', AdminCleanSheetsView.as_view(), name='admin_clean_sheets'),
    #
    # path('admin_update/admin_form/', AdminFormView.as_view(), name='admin_form'),
    # path('admin_update/<int:week_no>/admin_form/', AdminFormView.as_view(), name='admin_form'),
    #
    # path('admin_update/admin_get_goalkeepers/', AdminGetGoalkeepers.as_view(), name='admin_get_goalkeepers'),
    # path('admin_update/<int:week_no>/admin_get_goalkeepers/', AdminGetGoalkeepers.as_view(), name='admin_get_goalkeepers'),
    #
    # path('admin_update/admin_get_defenders/', AdminGetDefenders.as_view(), name='admin_get_defenders'),
    # path('admin_update/<int:week_no>/admin_get_defenders/', AdminGetDefenders.as_view(), name='admin_get_defenders'),
    #
    # path('admin_update/admin_get_midfielders/', AdminGetMidfielders.as_view(), name='admin_get_midfielders'),
    # path('admin_update/<int:week_no>/admin_get_midfielders/', AdminGetMidfielders.as_view(), name='admin_get_midfielders'),
    #
    # path('admin_update/admin_get_forwards/', AdminGetForwards.as_view(), name='admin_get_forwards'),
    # path('admin_update/<int:week_no>/admin_get_forwards/', AdminGetForwards.as_view(), name='admin_get_forwards'),

    path('admin_update/admin_sort_points_players/', SortPointsForPlayers.as_view(), name='admin_sort_points_players'),
    path('admin_update/<int:week_no>/admin_sort_points_players/', SortPointsForPlayers.as_view(), name='admin_sort_points_players'),

    path('admin_update/admin_calc_user_points/', CalculateUserTotalPoints.as_view(), name='admin_calc_user_points'),
    path('admin_update/<int:week_no>/admin_calc_user_points/', CalculateUserTotalPoints.as_view(), name='admin_calc_user_points'),

    path('personal_info/', PersonalinfoView.as_view(), name='personal_info'),
    path('members/', MembersView.as_view(), name='members'),

    path('members/get_right_member/', GetRightMemberView.as_view(), name='get_right_member'),

    path('squad/', SquadView.as_view(), name='squad'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
