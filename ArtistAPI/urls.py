from django.urls import re_path
from django.contrib import admin
from . import views

urlpatterns = [
    re_path('admin', admin.site.urls),
    re_path('login', views.login),
    re_path('register', views.register),
    re_path('api/works', views.work),
]
