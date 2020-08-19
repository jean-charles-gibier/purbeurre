from django.db import models
from product import models as prod
# from user import models as usr
from django.contrib.auth.models import User
"""
Test substitut
"""


class Substitute(models.Model):

    user_subst = models.ForeignKey(User, related_name='user_subst', on_delete=models.SET_NULL, null=True)
    product_origin = models.ForeignKey('product.Product', related_name='product_origin', on_delete=models.SET_NULL, null=True, blank=True)
    product_substitute = models.ForeignKey('product.Product', related_name='product_substitute', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Substitut"
        ordering = ['user_subst']
    
    def __str__(self):
        return self.user_subst
