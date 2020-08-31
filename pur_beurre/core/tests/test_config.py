from django.test import TestCase
from core import dbconnector as dbc


class FillerTestCase(TestCase):
    def setUp(self):
        pass

    def test_filler_installation(self):
        """ test if db is responsive """
        # vérifie qu'il y a bien une db fonctionnelle
        handle = dbc.DbConnector()
        self.assertIsNotNone(handle)





