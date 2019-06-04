# urlConf file to map url to views

from django.urls import path
from .views import *

urlpatterns = [
    path('create/<int:total_lots>',  create_lot, name='create_lot'),
    path('parkCar/', add_car, name='add_car'),
    path('removeCar/', remove_car, name='remove_car'),
    path('search/<str:key>/', search, name='search'),
    path('parkedCars/', fetch_all_parked_cars, name='fetch_all_parked_cars'),

]
