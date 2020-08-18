from django.urls import path, include, reverse, re_path
from .views import dashboard, login, register, dashboard_section
from django.contrib import admin
from django.contrib.auth import views as auth_views
# from user.views import dashboard

urlpatterns = [
    path(r"accounts/", include("django.contrib.auth.urls")),
    path(r'login/', login, name='login'),
    path(r"register/", register, name="register"),
    path(r"dashboard/", dashboard, name='dashboard'),
    re_path(r"^dashboard/(?P<section>\w+)$", dashboard_section, name='dashboard_section'),
    path(r'admin/', admin.site.urls),
]
