from django.test import TestCase
from nose.tools import nottest
from players.models import *

'''
Create by adding new playersself.
This here is to test by creating new players and adding points and deleting points. Every player will have be displayed many
'''

class Adding_Deleting_Points_Tests(TestCase):
    def setUp(self):
        Player_table.objects.create(id=1, player_name='Leonel Messi', current_player_value=99, real_football_team='Barcelona')
        Player_table.objects.create(id=2, player_name='Christiano Ronaldo', current_player_value=100, real_football_team='Juventus')
        Player_table.objects.create(id=3, player_name='Jesse Lingard', current_player_value=79, real_football_team='Manchester United')

    def test_00_add_first_points_for_messi(self):
        pass

    def test_01_add_first_points_for_ronald(self):
        pass

    def test_02_add_first_points_for_lingard(self):
        pass
