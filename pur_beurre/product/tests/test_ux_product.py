import pytest
import os
import pprint
BASE_DIR = \
    os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2])
os.environ["PATH"] += os.pathsep + os.path.join(BASE_DIR,'driver')

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.skipif('DEPLOY_ENVIRON' in os.environ and os.environ['DEPLOY_ENVIRON'] == 'PRODUCTION',
                    reason="requires production environement")
class AccountTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()


    def test_login(self):
        self.driver.implicitly_wait(5)
        self.driver.get('http://localhost:8000/user/login/')
        username = self.driver.find_element_by_id('id_username')
        username.send_keys('test_username')
        self.driver.implicitly_wait(5)

        password = self.driver.find_element_by_id('id_password')
        password.send_keys('test_password')
        self.driver.implicitly_wait(5)

        try:
            submit = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((((By.XPATH,'.//button[@type="submit" and text()="Login"]')))))
            submit.click()
        finally:
            self.driver.quit()


