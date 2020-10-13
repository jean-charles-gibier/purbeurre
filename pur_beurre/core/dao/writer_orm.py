# -*- coding: utf-8 -*- #
import logging as lg
import sys
import re
from product import models as prd
from collections import defaultdict
from django.core.exceptions import ObjectDoesNotExist
from django.apps import apps

import pprint 
logger = lg.getLogger(__name__)


class Writer:
    """
    Writer is a mapping substitution
    it is used for raw insertion
    """

    def __init__(self, table_name):
        """ init element list """
        self._bulk_list = list()
        """ columns names for insert """
        self._columns_names = ""
        """ columns values for insert """
        self._values_list = ""
        """ table name """
        self._table_name = table_name
        """ Categorie courante """
        self._current_category = None



    def add_rows(self, json_list, zcls):
        """ add a bunch of rows
        json_list :
        zcls : can be a class type or an dict
        """
        for idx, some in enumerate(json_list):
            try:
                # we get object (Category, Product)
                if not isinstance(zcls, dict):
                    if zcls.__name__ == "Product":
                        an_instance = None

                        try:
                            an_instance = prd.Product.objects.get(
                                code = some['code'][0:100] \
                                    if 'code' in some else '0000000000000'
                                )
                        except ObjectDoesNotExist:
                            an_instance = prd.Product(
                                code = some['code'][0:100] \
                                    if 'code' in some else '0000000000000',
                                name = some['product_name'][0:300] \
                                    if 'product_name' in some else '',
                                generic_name = some['generic_name_fr'][0:200] \
                                    if 'generic_name_fr' in some else '',
                                brands = some['brands'][0:100] \
                                    if 'brands' in some else 'None',
                                stores = some['stores'][0:100] \
                                    if 'stores' in some else '',
                                url = some['url'][0:200] if 'url' in some else '',
                                nutrition_grade = some['nutrition_grade_fr'] \
                                    if 'nutrition_grade_fr' in some else 'z' ,
                                image_front_url = some['image_front_url'][0:200] \
                                    if 'image_front_url' in some \
                                    else 'dist/assets/img/nothing.png'
                            )
                    elif zcls.__name__ == "Category":
                        an_instance = prd.Category(
                        tag = some['id'] if 'id' in some else None,
                        name = some['name'] if 'name' in some else None,
                        url = some['url'] if 'url' in some else None
                        )
                    self._bulk_list.append(an_instance)
                else:
                    try:
                        if self._current_category == None:
                            self._current_category = prd.Category.objects.get(
                            pk = zcls["category_id"]
                            )
                        new_instance = prd.Product.objects.get(
                                code = some['code'][0:100] \
                                    if 'code' in some else '0000000000000'
                                )
                        new_instance.categories.add(self._current_category)
                        new_instance.save()
                    except ObjectDoesNotExist:
                        logger.error('le prd [%s], ou la ctegorie [%s] est introuvable',
                            some['code'][0:100],
                            zcls["category_id"])
            except FloatingPointError :
                json_list.pop(idx)
                logger.error('[%s] Ne peut enregistrer l objet <%s> [%s]',
                             sys.exc_info()[0], zcls.__name__ if hasattr(zcls, '__name__') else 'dict', str(some))
        return json_list


    def write_rows(self):
        """ write specified values in specified table """
        cls = type(self._bulk_list[0])
        cls.objects.bulk_create(self._bulk_list, ignore_conflicts=True)
        # vide la liste qui vient d'être écrite
        self._bulk_list.clear()


    def join_rows(self, where_clause=None):
        """ write simple jointure many 2 many table """
        self._current_category = None

