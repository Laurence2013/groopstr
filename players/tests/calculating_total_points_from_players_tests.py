from django.test import TestCase
from nose.tools import nottest
from players.models import *

'''
This test is to calculate points from players stats tables
Scenario:- Collectively add points for each players into the stats tables, for 3 weeks into the season, and add all the collective points for each player
This is for an imaginary 3 games into the season
'''

class Calculating_Total_Points_From_Players_Tests(TestCase):
    def setUp(self):
        Player_table.objects.create(id=1, player_name='Leonel Messi', current_player_value=99, real_football_team='Barcelona')
        Player_table.objects.create(id=2, player_name='Christiano Ronaldo', current_player_value=100, real_football_team='Juventus')
        Player_table.objects.create(id=3, player_name='Jesse Lingard', current_player_value=79, real_football_team='Manchester United')

        self.get_players = Player_table.objects.all()
    '''
    This test is not including Jesse Lingard
    '''
    def test_00_add_points_for_a_game_in_the_1st_week(self):
        Man_of_Match_table.objects.create(id=1, points=7, total_points=0, player_id=self.get_players[0])
        Man_of_Match_table.objects.create(id=2, points=8, total_points=0, player_id=self.get_players[1])
        self.man_of_match_table = Man_of_Match_table.objects.values()
        Goals_Assist_table.objects.create(id=1, points=5, total_points=0, player_id=self.get_players[0])
        Goals_Assist_table.objects.create(id=2, points=5, total_points=0, player_id=self.get_players[1])
        self.goals_assist_table = Goals_Assist_table.objects.values()

        self.assertEqual(7, self.man_of_match_table[0].get('points'))
        self.assertEqual(0, self.man_of_match_table[0].get('total_points'))
        self.assertEqual(5, self.goals_assist_table[0].get('points'))
        self.assertEqual(0, self.goals_assist_table[0].get('total_points'))

        self.assertEqual(8, self.man_of_match_table[1].get('points'))
        self.assertEqual(0, self.man_of_match_table[1].get('total_points'))
        self.assertEqual(5, self.goals_assist_table[1].get('points'))
        self.assertEqual(0, self.goals_assist_table[1].get('total_points'))
    '''
    This test is including Jesse Lingard
    '''
    def test_01_add_points_for_a_game_in_the_2nd_week(self):
        Man_of_Match_table.objects.create(id=1, points=6, total_points=7, player_id=self.get_players[0])
        Man_of_Match_table.objects.create(id=2, points=6, total_points=8, player_id=self.get_players[1])
        Man_of_Match_table.objects.create(id=3, points=7, total_points=0, player_id=self.get_players[2])
        self.man_of_match_table = Man_of_Match_table.objects.values()
        Goals_Assist_table.objects.create(id=1, points=5, total_points=5, player_id=self.get_players[0])
        Goals_Assist_table.objects.create(id=2, points=5, total_points=5, player_id=self.get_players[1])
        Goals_Assist_table.objects.create(id=3, points=5, total_points=0, player_id=self.get_players[2])
        self.goals_assist_table = Goals_Assist_table.objects.values()

        self.assertEqual(6, self.man_of_match_table[0].get('points'))
        self.assertEqual(7, self.man_of_match_table[0].get('total_points'))
        self.assertEqual(5, self.goals_assist_table[0].get('points'))
        self.assertEqual(5, self.goals_assist_table[0].get('total_points'))

        self.assertEqual(6, self.man_of_match_table[1].get('points'))
        self.assertEqual(8, self.man_of_match_table[1].get('total_points'))
        self.assertEqual(5, self.goals_assist_table[1].get('points'))
        self.assertEqual(5, self.goals_assist_table[1].get('total_points'))

        self.assertEqual(7, self.man_of_match_table[2].get('points'))
        self.assertEqual(0, self.man_of_match_table[2].get('total_points'))
        self.assertEqual(5, self.goals_assist_table[2].get('points'))
        self.assertEqual(0, self.goals_assist_table[2].get('total_points'))
    '''
    This test is not including Ronaldo
    '''
    def test_02_add_points_for_a_game_in_the_3rd_week(self):
        Man_of_Match_table.objects.create(id=1, points=6, total_points=13, player_id=self.get_players[0])
        Man_of_Match_table.objects.create(id=3, points=7, total_points=7, player_id=self.get_players[2])
        self.man_of_match_table = Man_of_Match_table.objects.values()
        Goals_Assist_table.objects.create(id=1, points=5, total_points=10, player_id=self.get_players[0])
        Goals_Assist_table.objects.create(id=3, points=5, total_points=5, player_id=self.get_players[2])
        self.goals_assist_table = Goals_Assist_table.objects.values()

        self.assertEqual(6, self.man_of_match_table[0].get('points'))
        self.assertEqual(13, self.man_of_match_table[0].get('total_points'))
        self.assertEqual(5, self.goals_assist_table[0].get('points'))
        self.assertEqual(10, self.goals_assist_table[0].get('total_points'))

        self.assertEqual(7, self.man_of_match_table[1].get('points'))
        self.assertEqual(7, self.man_of_match_table[1].get('total_points'))
        self.assertEqual(5, self.goals_assist_table[1].get('points'))
        self.assertEqual(5, self.goals_assist_table[1].get('total_points'))
    
