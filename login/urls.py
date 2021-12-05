from django.contrib import admin
from django.urls import path, include
from login import views

urlpatterns = [
    path('', views.loginPage),
    path('fnblogin/', views.loginPage2),
    path('home/', views.loginCheck),
]