import unittest

from selenium import webdriver
from django.urls import resolve
from django.test import TestCase

from VK_API_Check.home.views import home_visit

class UnitClientTest(unittest.TestCase):  #check title web-site

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://127.0.0.1:8000/home/')
        self.assertIn(self.browser.title, 'VK Check')
        


class HomeTestPage(unittest.TestCase):
    def test_root_url_resolves_to_home_page_vies(self):
        found = resolve('/')
        self.assertEqual(found.func, home_visit)

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')