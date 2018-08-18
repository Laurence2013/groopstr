from django.test import TestCase
from nose.tools import nottest
from members.models import *
from members.forms import *
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
    '''
    Show that a fixture Chelsea vs Fiorentina is connected to Week 1, its week_no_id is 11
    Show that a fixture Chelsea vs Arsenal is connected to Week 1, its week_no_id is 11
    '''
    def test_00_show_that_a_fixture_is_connected_to_a_week(self):
        get_week = self.test.week_fixture_table()
        self.test.set_fixtures_and_week(get_week)
        # print()
        # for i in range(0, len(get_week[0])):
        #     for j in range(0, len(get_week[1])):
        #         if get_week[0][i].get('id') == get_week[1][j].get('week_no_id'):
        #             print(get_week[1][j].get('fixture'))
