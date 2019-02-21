from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name=''),
    path('books/', views.books, name=''),
    path('all/', views.books, name='allbooks'),
    path('all/', views.cars, name='allcars'),
]