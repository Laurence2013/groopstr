from django.test import TestCase
from nose.tools import nottest
from django.contrib.auth.models import User
from members.models import *
from members.forms import *

class Check_Username_In_Personal_Info_Table_Tests(TestCase):
    def setUp(self):
        self.get_user = User.objects.create_user('Tom123', 'tom123@gmail.com', 'qwerty123')
        self.get_user = User.objects.create_user('Mark123', 'mark123@gmail.com', 'qazwsx123')
        self.users = User.objects.all()
        self.personal_info = Personal_Info_table.objects.create(team_name='abc_fc', first_name='Tom', last_name='Clarke', has_username=self.users[0])
        self.personal_info = Personal_Info_table.objects.create(team_name='blue_fc', first_name='Mark', last_name='Clarke', has_username=self.users[1])

    def test_00_get_users(self):
        self.assertEqual('Tom123', str(self.users[0]))
        self.assertEqual('Mark123', str(self.users[1]))

    def test_01_check_if_user_team_exist_in_table(self):
        personal_info = Personal_Info_table.objects.values_list('team_name')
        self.assertEqual('abc_fc', str(personal_info[0][0]))
        self.assertEqual('blue_fc', str(personal_info[1][0]))

    def test_02_check_if_user_team_exist_in_table(self):
        form = PersonalInfoForm()
        print(form)
        pass
