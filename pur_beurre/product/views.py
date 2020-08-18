from django.http import HttpResponse

from django.views.generic import ListView
from product import models as prd
from django.db.models import Q
from django.shortcuts import render
import pprint

class ListProductsView(ListView):
    template_name = "product/query_products.html"  # chemin vers le template à afficher
    model = prd.Product
    context_object_name = "produits_trouves"
    paginate_by = 5

    def get_queryset(self):
        my_query = self.request.GET.get("query")
        if my_query is not None:
            return prd.Product.objects.filter(Q(generic_name__icontains=my_query) | Q(brands__icontains=my_query))
