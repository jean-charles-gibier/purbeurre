from django.http import HttpResponse

from django.views.generic import ListView
from product import models as prd
from substitute import models as sub
from django.contrib.auth.models import User

from django.db.models import Q
from django.views.generic import DetailView
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

class ListSubstitutesView(ListView):
    template_name = "product/query_substitutes.html"  # chemin vers le template à afficher
    model = prd.Product
    context_object_name = "substituts_trouves"
    paginate_by = 5

    def get_queryset(self):
        idProduct = self.request.GET.get("id")
        if idProduct is not None:
            p_selection = prd.Product.objects.get(pk=idProduct)
            p_categories = p_selection.categories.all()
            p_nutrition_grade = p_selection.nutrition_grade

            list_prod = prd.Product.objects.filter(
                categories__in=p_categories,
                nutrition_grade__lt=p_nutrition_grade
                ).order_by('nutrition_grade')
            return list_prod

    def get_context_data(self, **kwargs):
        idProduct = self.request.GET.get("id")
        if idProduct is not None:
            p_selection = prd.Product.objects.get(pk=idProduct)
            ctx = super(ListSubstitutesView, self).get_context_data(**kwargs)
            ctx['product_name'] = p_selection.name
            ctx['brand_name'] = p_selection.brands
            ctx['image_front_url'] = p_selection.image_front_url
            return ctx


def register_subsituts(request):
    idProduct = request.GET.get("id")
    idSubstitute = request.GET.get("sub")
    p_origin = prd.Product.objects.get(pk=idProduct)
    p_substitute = prd.Product.objects.get(pk=idSubstitute)
    reg_sub = sub.Substitute.objects.create(
        user_subst = request.user,
        product_origin = p_origin,
        product_substitute = p_substitute
        )

    return render(
        request, "product/register_substitutes.html",
        {"none": "none"}
    )

