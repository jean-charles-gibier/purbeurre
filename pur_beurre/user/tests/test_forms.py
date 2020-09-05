from django.contrib.auth.forms import AuthenticationForm
from django.test import TestCase
from user.forms import CustomUserCreationForm


class TestFormsUsers(TestCase):

    def setUp(self):
        self.user_register = {
            'username': 'user_name',
            'email': 'name@free.fr',
            'password1': 'Abcz1198!',
            'password2': 'Abcz1198!'
        }

        self.user_register_wrong_pw = {
            'username': 'user_name',
            'email': 'name@free.fr',
            'password1': 'Zzzzzzzz!',
            'password2': 'Abcz1198!'
        }

        self.user_register_wrong_email = {
            'username': 'user_name',
            'email': 'name',
            'password1': 'Abcz1198!',
            'password2': 'Abcz1198!'
        }

        self.user_login = {
            'username': 'username',
            'password': 'Abcz1198!'
        }

    def test_regForm_is_valid(self):
        """
        data correct
        :return: true
        """
        data = self.user_register
        form = CustomUserCreationForm(data)
        is_valid = form.is_valid()
        self.assertTrue(is_valid)

    def test_regForm_wrong_pw(self):
        """
        Pb password incorrect
        :return: false
        """
        data = self.user_register_wrong_pw
        form = CustomUserCreationForm(data)
        is_valid = form.is_valid()
        self.assertFalse(is_valid)

    def test_regForm_wrong_email(self):
        """
        Pb email incorrect
        :return: false
        """
        data = self.user_register_wrong_email
        form = CustomUserCreationForm(data)
        is_valid = form.is_valid()
        self.assertFalse(is_valid)

    def test_logForm_is_not_valid(self):
        data = self.user_login
        form = AuthenticationForm(None, data=data)
        is_valid = form.is_valid()
        self.assertFalse(is_valid)
