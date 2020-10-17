# coding=utf-8

from django.db.models import Q
from django.test import TestCase
from django.urls import reverse
from product import models as prd
from django.contrib.auth.models import User

import inspect
import pprint

class ProductTestCase(TestCase):
    def setUp(self):
        """
        prepare a bunch of products
        categories etc.
        :return:
        """
        prd.Product.objects.all().delete()
        prd.Category.objects.all().delete()


        dummy_cat = prd.Category.objects.create(
            tag='tg0000',
            name='category 000',
            url='url000')

        p101 = prd.Product.objects.create(
            code='1000000000001',
            name='product 101',
            generic_name='Coca Cola 1L',
            brands='Coca',
            stores='stores001',
            url='url001',
            nutrition_grade='C')

        p102 = prd.Product.objects.create(
            code='1000000000002',
            name='product 102',
            generic_name='Coke 1L',
            brands='cola',
            stores='stores001',
            url='url001',
            nutrition_grade='D')

        p001 = prd.Product.objects.create(
            code='0000000000001',
            name='product 001',
            generic_name='product prd 001',
            brands='Brand of prd 001',
            stores='stores001',
            url='url001',
            nutrition_grade='E')

        p002 = prd.Product.objects.create(
            code='0000000000002',
            name='product 002',
            generic_name='product prd 002',
            brands='Brand of prd 002',
            stores='stores002',
            url='url002',
            nutrition_grade='A')

        p001.categories.add(dummy_cat)
        p002.categories.add(dummy_cat)
        p101.categories.add(dummy_cat)
        p102.categories.add(dummy_cat)

    def test_products_are_products(self):
        """Products are correctly identified"""
        prd1 = prd.Product.objects.get(
            code='0000000000001',
            name='product 001',
            generic_name='product prd 001',
            brands='Brand of prd 001',
            stores='stores001',
            url='url001')

        prd2 = prd.Product.objects.get(
            code='0000000000002',
            name='product 002',
            generic_name='product prd 002',
            brands='Brand of prd 002',
            stores='stores002',
            url='url002')

        self.assertEqual(prd1.code, '0000000000001')
        self.assertEqual(prd2.code, '0000000000002')

    def test_products_like_(self):
        """Test search products where attrbute
        'name' or 'brand' like cola"""
        raws = prd.Product.objects.filter(Q(generic_name__icontains='cola')
                                          | Q(brands__icontains='cola'))
        self.assertEqual(len(raws), 2)

    def test_products_like_with_better_score(self):
        """Test search product wihh same catecgory
        but with a better score """
        # p002 # best score => no one better => 0 results
        p002 = prd.Product.objects.get(code='0000000000002')
        p002_categories = p002.categories.all()
        p002_nutrition_grade = p002.nutrition_grade

        raws = prd.Product.objects.filter(
            categories__in=p002_categories,
            nutrition_grade__lt=p002_nutrition_grade)
        self.assertEqual(len(raws), 0)

        # p001 # worst score => 3 others are better
        p001 = prd.Product.objects.get(code='0000000000001')
        p001_categories = p001.categories.all()
        p001_nutrition_grade = p001.nutrition_grade

        raws = prd.Product.objects.filter(
            categories__in=p001_categories,
            nutrition_grade__lt=p001_nutrition_grade)
        self.assertEqual(len(raws), 3)


    def test_list_right_number_products(self):
        """
        vérifie la pertinence des objets (produits/categories) collectés 
        le nombre d'elements retournés doit être exact.
        :return:
        """
        # tous les cocas
        response = self.client.get(reverse('query_products')+'?query=cola')
        self.assertEqual(response.status_code, 200)

        # pprint.pprint(response.context['produits_trouves'])
        self.assertTrue(len(response.context['produits_trouves']) == 2)


    def test_list_content_lowest_NG(self):
        """
        vérifie la pertinence des objets (produits/categories) collectés 
        dans les listes remontées par les choix utilisateur.
        Le "nutrition grade" doit être moindre que cleui du produit sélectionné
        :return:
        """
        # tous les prd fde même categorie que la selection avec un meilleur 
        # nutriscore
        # On prend le 3eme enregistrement (le plus mauvais nutriscore) 
        # Il y en a 3 meilleurs
        self.user = User.objects.create_user(username='some_user',
                                             email='some_user@somewhere.com',
                                             password='Abcz1198!')
        self.client.login(username='some_user@somewhere.com',
                          password='Abcz1198!')

        p001 = prd.Product.objects.get(code='0000000000001')
        rev = reverse('query_substituts')+'?id='+ str(p001.pk)
        response = self.client.get(rev)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['substituts_trouves']) == 3)


class CategoryTestCase(TestCase):
    def setUp(self):
        """ prepare items for test """
        prd.Category.objects.create(
            tag='tg0001',
            name='category 001',
            url='url001')

        prd.Category.objects.create(
            tag='tg0002',
            name='category 002',
            url='url002')

    def test_categories_are_categories(self):
        """categories are correctly identified"""
        cat1 = prd.Category.objects.get(
            tag='tg0001',
            name='category 001',
            url='url001')

        cat2 = prd.Category.objects.get(
            tag='tg0002',
            name='category 002',
            url='url002')

        self.assertEqual(cat1.tag, 'tg0001')
        self.assertEqual(cat2.tag, 'tg0002')

