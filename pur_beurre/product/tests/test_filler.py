from django.test import TestCase
# from user import models as usr
from product import models as prd
from core import filler as fil


class FillerTestCase(TestCase):
    def setUp(self):
        pass

    def test_filler_start(self):
        """ test if filler works and model is instancied """
        fil.Filler().start(10)
        # vérifie qu'il y a bien 10 objets dans le model product
        self.assertEqual(prd.Product.objects.count(), 10)
        pass



