from django.test import TestCase
from nose.tools import nottest
from members.models import *
from players.models import *
'''
Scenario: At the start of the season, before the first week begins, there are 2 fixtures, the champions league qualifier and the weekend of premiership games.
Get a user named Adam to pick the players, get Adam to choose the right players, get Adam to submit it and finally the Admin to check it.
00 - User named Adam picks 14 players
01 - Show that Adam chooses players that are within the given credits limit e.g. 8000
02 - Show that if Adams goes over the limit inform Adam that this is not allowed
03 - Admin enters week 1 and the example fixtures within week 1
04 - Check that the neccessary tables has the week 1 id as their foreign key
05 - As an example, Show that Admin cannot choose some of his players who are not eligible to play in the first week because 'is_player_playing' set to False
06 - Show that Adam chosen 4-4-2 formation
07 - Show that Adam has 4 defenders, 4 midfielders, 2 strikers and 1 goalkeeper
08 - Show that Adam chosen 3-5-2 formation
09 - Show that adam has 3 defenders, 5 midfielders, 2 strikers and 1 goalkeeper
10 - Show in the formations tables, Adam chosen 11 players for his 4-4-2 formation, for this first week, 'player_eligible' field is set to True
11 - Show in the formations tables, Adams 3 players not chosen this first week, 'player_eligible' field is set to False
12 - In the Admin section, show that he choosen Adams squad for the first week and checked that he chosen a formation and the correct players for that formation, also check that the chosen players are eligible
The idea here is to get the Admin to set week 1 to all the related tables -> Inform users that the season begins (email, text, etc)

'''
class Scenario_before_week_1_begins(TestCase):
    def setup(self):
        return False
