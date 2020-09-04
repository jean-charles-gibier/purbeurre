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
        self.user_login = {
            'username': 'username',
            'password': 'Abcz1198!'
        }

    def test_regForm_is_valid(self):
        data = self.user_register
        form = CustomUserCreationForm(data)
        is_valid = form.is_valid()
        self.assertTrue(is_valid)

    def test_logForm_is_not_valid(self):
        data = self.user_login
        form = AuthenticationForm(None, data=data)
        is_valid = form.is_valid()
        self.assertFalse(is_valid)
