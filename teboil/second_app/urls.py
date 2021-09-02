from django.urls import path
from . import views

urlpatterns = [
    path('', views.second_render, name='second_render'),
    path('redirect/', views.second_redirect, name='second_redirect'),
    path('httpresponse/', views.httpresponse, name='second_httpresponse'),
]