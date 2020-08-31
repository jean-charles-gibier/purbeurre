import pytest
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["PATH"] += os.pathsep + os.path.join(BASE_DIR,'/driver/geckodriver')

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AccountTestCase(LiveServerTestCase):
    @pytest.mark.skipif('DEPLOY_ENVIRON' in os.environ and os.environ['DEPLOY_ENVIRON'] == 'PRODUCTION')
    def test_login(self):
        driver = webdriver.Firefox()
        driver.get('http://127.0.0.1:8000/accounts/login/')
#        username = driver.find_element_by_id('id_username')
#        password = driver.find_element_by_id('id_password')
#        submit = driver.find_element_by_tag_name('button')
#        username.send_keys('superusername')
#        password.send_keys('superuserpassword')
#        submit.send_keys(Keys.RETURN)

