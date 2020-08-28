"""pur_beurre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
# from substitute import views
# from product import views
# from user import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='pur_beurre/home.html'), name='home'),
    path('substitutes/', include('substitute.urls')),
    path('products/', include('product.urls')),
    path(r"user/", include("user.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path('^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    
    
    
    