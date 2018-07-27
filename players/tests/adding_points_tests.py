from django.test import TestCase
from nose.tools import nottest
from players.models import *

'''
Create by adding new players.
A scenario would be updating players points in the stats tables for each player, player_id acting as the foreign key
Individually add points or delete points for each player in the Form Table
This is for an imaginary 3 games into the season
'''

class Adding_Points_Tests(TestCase):
    def setUp(self):
        Player_table.objects.create(id=1, player_name='Leonel Messi', current_player_value=99, real_football_team='Barcelona')
        Player_table.objects.create(id=2, player_name='Christiano Ronaldo', current_player_value=100, real_football_team='Juventus')
        Player_table.objects.create(id=3, player_name='Jesse Lingard', current_player_value=79, real_football_team='Manchester United')

        self.get_players = Player_table.objects.all()

    def test_00_add_points_for_a_game_in_the_1st_week(self):
        Form_table.objects.create(id=1, points=7, total_points=0, player_id=self.get_players[1])
        Form_table.objects.create(id=2, points=8, total_points=0, player_id=self.get_players[0])
        Form_table.objects.create(id=3, points=6, total_points=0, player_id=self.get_players[2])
        self.get_form_table = Form_table.objects.values()

        self.assertEqual(7, self.get_form_table[0].get('points'))
        self.assertEqual(0, self.get_form_table[0].get('total_points'))

        self.assertEqual(8, self.get_form_table[1].get('points'))
        self.assertEqual(0, self.get_form_table[1].get('total_points'))

        self.assertEqual(6, self.get_form_table[2].get('points'))
        self.assertEqual(0, self.get_form_table[2].get('total_points'))

    def test_01_update_points_for_a_game_in_the_2nd_week(self):
        Form_table.objects.create(id=1, points=7, total_points=14, player_id=self.get_players[1])
        Form_table.objects.create(id=2, points=7, total_points=15, player_id=self.get_players[0])
        Form_table.objects.create(id=3, points=6, total_points=12, player_id=self.get_players[2])
        self.get_form_table = Form_table.objects.values()

        self.assertEqual(7, self.get_form_table[0].get('points'))
        self.assertEqual(14, self.get_form_table[0].get('total_points'))

        self.assertEqual(7, self.get_form_table[1].get('points'))
        self.assertEqual(15, self.get_form_table[1].get('total_points'))

        self.assertEqual(6, self.get_form_table[2].get('points'))
        self.assertEqual(12, self.get_form_table[2].get('total_points'))

    def test_02_update_points_for_a_game_in_the_3rd_week(self):
        Form_table.objects.create(id=1, points=9, total_points=23, player_id=self.get_players[1])
        Form_table.objects.create(id=2, points=7, total_points=22, player_id=self.get_players[0])
        Form_table.objects.create(id=3, points=6, total_points=18, player_id=self.get_players[2])
        self.get_form_table = Form_table.objects.values()

        self.assertEqual(9, self.get_form_table[0].get('points'))
        self.assertEqual(23, self.get_form_table[0].get('total_points'))

        self.assertEqual(7, self.get_form_table[1].get('points'))
        self.assertEqual(22, self.get_form_table[1].get('total_points'))

        self.assertEqual(6, self.get_form_table[2].get('points'))
        self.assertEqual(18, self.get_form_table[2].get('total_points'))
