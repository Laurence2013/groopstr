import time
from django.test import TestCase
from nose.tools import nottest
from selenium import webdriver
import pickle

class AdminUpdateTest(TestCase):
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    def setUp(self):
        self.driver.get('http://localhost:8000/admin_update/')
        # self.driver.get('http://www.google.co.uk')
        name = {'name' : 'foo', 'value' : 'bar', 'secure' : False}
        self.driver.add_cookie(name)

    @nottest
    def test_00_testing(self):
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            print(self.driver.add_cookie(cookie))
    
    def test_01_first_test(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//li[@id="backg-colour"]/input[@id="check_w"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@id="submit_new_week"]').click()
        time.sleep(2)

    def test_02_testing(self):
        print(dir(self.driver))
        print()
        print(self.driver.get_cookies())

    def tearDown(self):
        self.driver.close()
