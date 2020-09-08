# coding=utf-8
"""
Tests sur les vues user
"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from user import views as vuser


class UserViewTestCase  (TestCase):
    def setUp(self):
        pass


    def test_login_view(request):
        pass