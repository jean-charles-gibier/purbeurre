import os
import pytest
import pprint
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from product import models as prd
from core.dbconnector import DbConnector

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
        """
        Test fonctionnel de création d'un user
        :return:
        """
        self.sub_register_success()
#        self.sub_login_success()
#        self.sub_register_fail_yet_registered()
        self.sub_register_clean()


    def sub_register_clean(self):
        """  supprime un user
        précedemment créé pour les tests"""
        print("Cleaning datas : 1")

        db = DbConnector()
        print("Cleaning datas : connected")
        cnx = db.handle
        print("Cleaning datas cnx : {}".format(cnx))
        cursor = cnx.cursor()
        print("Cleaning datas cursor : {}".format(cursor))
        try:
            str_sql = 'DELETE FROM "public"."auth_user" WHERE "username"={} and "email"={}'.format("'Jose'", "'Jose@dummies.com'")
            print("[{}]".format(str_sql))
            cursor.execute(str_sql)
            print("Cursor execute status msg : {}".format(cursor.statusmessage))
        except Exception as err:
            print("Failed cleaning datas : {}".format(err))
        cursor.close()
        print("Cleaning datas cursor close:")
        cnx.commit()
        cnx.close()


    def sub_register_success(self):
        """  crée un user pour le test """
        self.driver.get('http://127.0.0.1:8000/user/register/#register_section')
        self.driver.implicitly_wait(5)
        username = self.driver.find_element_by_id('id_username')
        username.send_keys('Jose')
        self.driver.implicitly_wait(5)

        password1 = self.driver.find_element_by_id('id_password1')
        password1.send_keys('J053_1234')
        self.driver.implicitly_wait(5)

        email = self.driver.find_element_by_id('id_email')
        email.send_keys('Jose@dummies.com')
        self.driver.implicitly_wait(5)

        password2 = self.driver.find_element_by_id('id_password2')
        password2.send_keys('J053_1234')
        self.driver.implicitly_wait(5)

        try:
            submit = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((((By.XPATH, "//button[@type='submit' and text()='Créer le compte']")))))
            submit.click()
        except:
            self.assertIsNotNone(submit)

        try:
              test = WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((((By.XPATH, "//h2[contains(text(), 'Hello')]")))))
        except:
            assert(1 == 0)


    def sub_register_fail_yet_registered(self):
        """  crée un user existant pour le test
        on ne vérifie juste que le msg d'erreur
        concernant l'adresse mail deja utilisée """
        self.driver.get('http://127.0.0.1:8000/user/register/#register_section')
        self.driver.implicitly_wait(5)
        username = self.driver.find_element_by_id('id_username')
        username.send_keys('Jose')
        self.driver.implicitly_wait(5)

        password1 = self.driver.find_element_by_id('id_password1')
        password1.send_keys('J053_1234')
        self.driver.implicitly_wait(5)

        email = self.driver.find_element_by_id('id_email')
        email.send_keys('Jose@dummies.com')
        self.driver.implicitly_wait(5)

        password2 = self.driver.find_element_by_id('id_password2')
        password2.send_keys('J053_1234')
        self.driver.implicitly_wait(5)

        try:
            submit = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((((By.XPATH, "//button[@type='submit' and text()='Créer le compte']")))))
            submit.click()
        except:
            self.assertIsNotNone(submit)

        try:
              test = WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((((By.XPATH, "//p[contains(@class, 'text-info') and contains(text(), '[Un utilisateur avec ce nom existe déjà.]')]")))))
        except:
            assert(1 == 0)



    def sub_login_success(self):
        """ doit réussir si le user a été créée """
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
              test = WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((((By.XPATH, "//h2[contains(text(), 'Hello')]")))))
        except:
            assert(1 == 0)

    def sub_login_success(self):
        """ doit réussir si le user a été créée """
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
              test = WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((((By.XPATH, "//h2[contains(text(), 'Hello')]")))))
        except:
            assert(1 == 0)



    def test_login_fail(self):
        """
        User does not exist
        err msg should appear
        """
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


