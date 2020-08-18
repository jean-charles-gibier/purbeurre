from django.urls import path, include, re_path
from .views import ListProductsView


urlpatterns = [
    re_path(r"results?",
            ListProductsView.as_view(), name='query_products'),
]
