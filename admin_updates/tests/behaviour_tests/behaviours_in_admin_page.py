from django.test import TestCase, RequestFactory, Client
from admin_updates.saving_points import Saving_Points
from members.members_team import GetMembersTeam
from nose.tools import nottest
from members.models import *
from players.models import *
from members.forms import *
import datetime
from test_database_tables import Fixtures_and_Weeks
'''
Scenario:-
Admin will always update fixtures and week manually
Admin will always update players points into the players statistics tables

1 - Connect fixtures to its correct week before displaying - test_database_tables.Fixtures_and_Weeks class
2 - Show all Weeks in Week_table and display in Admin page - show is_current_week - so admin can check which one should be current
3 - Show admin all the weeks for the season and future competitions within the season
4 - Get Admin to check (using radio button) the most current week save it to all statistics tables -> forms, goals, goal_assist, red_cards etc
4(i) - Get all players id add first time or again in all statistics table with new pk and new week number
5 - Enter new points to the right player in the right week for example if week 8, then make sure it is week 8, right player id, then add points
6 - Sort players in their position, goalkeeper, defender, midfielder and striker, then save into json files
6(i) - When admin chooses a new week, admin will update
7 - From squad tables get members IDs and Player IDs
7(i) - Go to player table, get players points according to ID of players
7(ii) - Get point and save into Squad tables player_points according to user ID
'''
class Behaviours_In_Admin_Page(TestCase):
    def setUp(self):
        self.test = Fixtures_and_Weeks()
        self.admin_get_goals = GetMembersTeam()
        self.factory = RequestFactory()
        self.week_fixture_0 = {'end_date': datetime.date(2018, 8, 11), 'fixture': 'Chelsea vs Fiorentina', 'date_of_game': datetime.date(2018, 8, 8), 'start_date': datetime.date(2018, 8, 5), 'week_no': 1, 'competition': 'cl'}
        self.week_fixture_1 = {'end_date': datetime.date(2018, 8, 11), 'fixture': 'Chelsea vs Arsenal', 'date_of_game': datetime.date(2018, 8, 10), 'start_date': datetime.date(2018, 8, 5), 'week_no': 1, 'competition': 'pl'}
        self.week_fixture_2 = {'end_date': datetime.date(2018, 8, 18), 'fixture': 'Liverpool vs Everton', 'date_of_game': datetime.date(2018, 8, 10), 'start_date': datetime.date(2018, 8, 12), 'week_no': 2, 'competition': 'pl'}
        self.week_fixture_3 = {'fixture': 'Chelsea vs Fiorentina', 'week_no': 1, 'competition': 'cl', 'start_date': datetime.date(2018, 8, 5), 'date_of_game': datetime.date(2018, 8, 8), 'end_date': datetime.date(2018, 8, 11)}
        self.week_fixture_4 = {'fixture': 'Chelsea vs Arsenal', 'week_no': 2, 'competition': 'pl', 'start_date': datetime.date(2018, 8, 12), 'date_of_game': datetime.date(2018, 8, 10), 'end_date': datetime.date(2018, 8, 18)}
        self.week_fixture_5 = {'fixture': 'Liverpool vs Everton', 'week_no': 2, 'competition': 'pl', 'start_date': datetime.date(2018, 8, 12), 'date_of_game': datetime.date(2018, 8, 10), 'end_date': datetime.date(2018, 8, 18)}
        self.week_fixture_6 = {'start_date': datetime.date(2018, 8, 12), 'end_date': datetime.date(2018, 8, 18), 'week_no': 2, 'date_of_game': datetime.date(2018, 8, 8), 'competition': 'cl', 'fixture': 'Chelsea vs Fiorentina'}
        self.week_fixture_7 = {'start_date': datetime.date(2018, 8, 12), 'end_date': datetime.date(2018, 8, 18), 'week_no': 2, 'date_of_game': datetime.date(2018, 8, 10), 'competition': 'pl', 'fixture': 'Chelsea vs Arsenal'}
        self.week_fixture_8 = {'start_date': datetime.date(2018, 8, 19), 'end_date': datetime.date(2018, 8, 26), 'week_no': 3, 'date_of_game': datetime.date(2018, 8, 10), 'competition': 'pl', 'fixture': 'Liverpool vs Everton'}
    '''
    1 - Connect fixtures to its correct week before displaying - test_database_tables.Fixtures_and_Weeks class
    '''
    def test_00_show_that_a_fixture_is_connected_to_a_week(self):
        get_week = self.test.week_fixture_table_00()
        get_week_fixture = self.test.set_fixtures_and_week(get_week)
        self.assertDictEqual(self.week_fixture_0, get_week_fixture[0])
        self.assertDictEqual(self.week_fixture_1, get_week_fixture[1])
        self.assertDictEqual(self.week_fixture_2, get_week_fixture[2])

    def test_01_show_that_a_fixture_is_connected_to_a_week(self):
        get_week = self.test.week_fixture_table_01()
        get_week_fixture = self.test.set_fixtures_and_week(get_week)
        self.assertDictEqual(self.week_fixture_3, get_week_fixture[0])
        self.assertDictEqual(self.week_fixture_4, get_week_fixture[1])
        self.assertDictEqual(self.week_fixture_5, get_week_fixture[2])

    def test_02_show_that_a_fixture_is_connected_to_a_week(self):
        get_week = self.test.week_fixture_table_02()
        get_week_fixture = self.test.set_fixtures_and_week(get_week)
        self.assertDictEqual(self.week_fixture_6, get_week_fixture[0])
        self.assertDictEqual(self.week_fixture_7, get_week_fixture[1])
        self.assertDictEqual(self.week_fixture_8, get_week_fixture[2])
    '''
    4 - Get Admin to check (using radio button) the most current week save it to all statistics tables -> forms, goals, goal_assist, red_cards etc
    '''
    def test_03_check_if_goals_table_is_null(self):
        get_goals_table = self.test.stats_goals_table00()
        self.assertEqual(None, get_goals_table[0].get('player_id'))
        self.assertEqual(0, get_goals_table[0].get('points'))

    def test_04_check_if_goals_table_is_null(self):
        get_points_from_goals_table = self.test.stats_goals_table01(1, 20)
        self.assertEqual(20, get_points_from_goals_table[0].get('points'))

    def test_05_testing_admin(self):
        self.test.week_table_for_client()
        user = Client()
        response = user.get('/admin_update/')
        self.assertEqual(200, response.status_code)

    def test_06_testing_admin(self):
        self.test.week_table_for_client()
        response = self.factory.post('/admin_update/8/', {'csrfmiddlewaretoken': ['PfVXhnxP0Ygj7xp0hlmQMlwqp061vW92xeen5ws5lFskTAkT5mNrodNgJIuD70i8', 'PfVXhnxP0Ygj7xp0hlmQMlwqp061vW92xeen5ws5lFskTAkT5mNrodNgJIuD70i8', 'PfVXhnxP0Ygj7xp0hlmQMlwqp061vW92xeen5ws5lFskTAkT5mNrodNgJIuD70i8', 'PfVXhnxP0Ygj7xp0hlmQMlwqp061vW92xeen5ws5lFskTAkT5mNrodNgJIuD70i8'], 'which_check_week': ['8']})
        self.assertEqual(8, int(response.POST['which_check_week']))

    def test_07_testing_admin(self):
        self.test.week_table_for_client()
        response = self.factory.post('/admin_update/9/', {'csrfmiddlewaretoken': ['PfVXhnxP0Ygj7xp0hlmQMlwqp061vW92xeen5ws5lFskTAkT5mNrodNgJIuD70i8', 'PfVXhnxP0Ygj7xp0hlmQMlwqp061vW92xeen5ws5lFskTAkT5mNrodNgJIuD70i8', 'PfVXhnxP0Ygj7xp0hlmQMlwqp061vW92xeen5ws5lFskTAkT5mNrodNgJIuD70i8', 'PfVXhnxP0Ygj7xp0hlmQMlwqp061vW92xeen5ws5lFskTAkT5mNrodNgJIuD70i8'], 'which_check_week': ['9']})
        self.assertEqual(9, int(response.POST['which_check_week']))

    def test_08_testing_admin(self):
        self.test.week_table_for_admin()
        saving_points = Saving_Points()
        request = self.factory.post('/admin_update/8/admin_get_goals/', {'player_id': ['1', '2', '3', '4', '5', '6', '7'], 'goals': ['5', '5', '5', '5', '5', '6', '6'], 'csrfmiddlewaretoken': ['PfVXhnxP0Ygj7xp0hlmQMlwqp061vW92xeen5ws5lFskTAkT5mNrodNgJIuD70i8', 'PfVXhnxP0Ygj7xp0hlmQMlwqp061vW92xeen5ws5lFskTAkT5mNrodNgJIuD70i8', 'PfVXhnxP0Ygj7xp0hlmQMlwqp061vW92xeen5ws5lFskTAkT5mNrodNgJIuD70i8', 'PfVXhnxP0Ygj7xp0hlmQMlwqp061vW92xeen5ws5lFskTAkT5mNrodNgJIuD70i8', 'PfVXhnxP0Ygj7xp0hlmQMlwqp061vW92xeen5ws5lFskTAkT5mNrodNgJIuD70i8', 'PfVXhnxP0Ygj7xp0hlmQMlwqp061vW92xeen5ws5lFskTAkT5mNrodNgJIuD70i8', 'PfVXhnxP0Ygj7xp0hlmQMlwqp061vW92xeen5ws5lFskTAkT5mNrodNgJIuD70i8'], 'week_no': ['8']})
        # print(dir(response))
        # print()
        # print(response.POST.getlist('goals'))
        goals_player = []
        goals_player.append({'week_no': request.POST.get('week_no')})
        goals_assists = request.POST.getlist('goals')
        player_id = request.POST.getlist('player_id')
        points_is_saved = saving_points.save_points(goals_player, goals_assists, player_id, Goals_table)
        # points_is_saved = self.admin_get_goals.admin_get_goals_view_post({'week_no': request.POST.get('week_no')}, request.POST.getlist('goals'), request.POST.getlist('player_id'))
        print(points_is_saved)
