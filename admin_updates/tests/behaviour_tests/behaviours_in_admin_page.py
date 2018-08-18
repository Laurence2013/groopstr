from django.test import TestCase
from nose.tools import nottest
from members.models import *
from members.forms import *
import datetime
from test_database_tables import Fixtures_and_Weeks
'''
Scenario:-
Admin will always update fixtures and week manually
Admin will always update players points into the players statistics tables

1 - Connect fixtures to its correct week before displaying - test_database_tables.Fixtures_and_Weeks class
2 - Show all Weeks in Week_table and display in Admin page
3 - Show all Fixtures linked to week
4 - Get Admin to check the most current week
'''
class Behaviours_In_Admin_Page(TestCase):
    def setUp(self):
        self.test = Fixtures_and_Weeks()
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
    Show a fixture, for example. Chelsea vs Fiorentina is connected to Week 1, its week_no_id is 11
    Show a fixture, for example. Chelsea vs Arsenal is connected to Week 1, its week_no_id is 11
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
