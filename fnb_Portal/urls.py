from django.contrib import admin
from django.urls import path, include
from fnb_Portal import views

urlpatterns = [
    path('', views.loginCheck),
]
