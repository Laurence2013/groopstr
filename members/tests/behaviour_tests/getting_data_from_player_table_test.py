from django.test import TestCase
from nose.tools import nottest
from members.models import *

class Getting_Data_From_Player_Table_Test(TestCase):
    def setUp(self):
        self.form = Form_table.objects.all()
        
    def test_01_sample_test(self):
        self.assertTrue(True)

    def test_02_sample_test(self):
        self.assertTrue(False)
