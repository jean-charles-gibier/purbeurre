import os
import pytest
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from product import models as prd
from django.contrib.auth.models import User

BASE_DIR = \
    os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2])
os.environ["PATH"] += os.pathsep + os.path.join(BASE_DIR,'driver')

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

    def test_login_success(self):
        self.user = User.objects.create(username='Jose', password='J053_1234', email='Jose@free.fr')
        self.user.save()

        self.driver.get('http://localhost:8000/user/login/')
        self.driver.implicitly_wait(5)

        username = self.driver.find_element_by_id('id_username')
        username.send_keys('Jose')
        self.driver.implicitly_wait(5)

        password = self.driver.find_element_by_id('id_password')
        password.send_keys('J053_1234')
        self.driver.implicitly_wait(5)

        try:
            submit = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((((By.XPATH, "//button[@type='submit' and text()='Login']")))))
            submit.click()
        except:
            self.assertIsNotNone(submit)

        try:
              WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((((By.XPATH, "//h2[contains(text(), 'Hello')]")))))
        except:
            assert(1 == 0)



    def test_login_fail(self):
        self.user = User.objects.create(username='Sejo', password='J053_1234', email='Jose@free.fr')
        self.user.save()

        self.driver.get('http://localhost:8000/user/login/')
        self.driver.implicitly_wait(5)

        username = self.driver.find_element_by_id('id_username')
        username.send_keys('Sejo')
        self.driver.implicitly_wait(5)

        password = self.driver.find_element_by_id('id_password')
        password.send_keys('false_pwd')
        self.driver.implicitly_wait(5)

        try:
            submit = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((((By.XPATH, "//button[@type='submit' and text()='Login']")))))
            submit.click()
        except:
            self.assertIsNotNone(submit)

        try:
             WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((((By.XPATH, "//p[contains(@class, 'danger') and contains(text(), 'Veuillez saisir à nouveau vos identifiants ou créer un compte')]")))))
        except:
            assert(1 == 0)

