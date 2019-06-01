# urlConf file to map url to views

from django.urls  import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('parkCar/', views.setCarDetails, name='setCarDetails'),
    path('removeCar/', views.removeCar, name='removeCar'),
    path('search/<str:key>/', views.search, name='search'),
    path('parkedCars/', views.fetchAllParkedCars, name='fetchAllParkedCars'),

]
