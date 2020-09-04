from django.test import TestCase
from product import models as prd
from core import filler as fil


# import pur_beurre.core.filler as fil
# import pur_beurre.product.models as prd

# from pur_beurre.product import models
# f.Filler().start(10)

class FillerTestCase(TestCase):
    def setUp(self):
        pass

    def test_filler_start(self):
        """ test if filler works and model is instancied """
        fil.Filler().start(10)
        # vérifie qu'il y a bien 10 objets dans le model product
        self.assertEqual(prd.Product.objects.count(), 10)
        pass
