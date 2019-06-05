# urlConf file to map url to views

from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('create/<int:total_lots>',  create_lot, name='create_lot'),
    path('parkCar/', csrf_exempt(add_car), name='add_car'),
    path('removeCar/', remove_car, name='remove_car'),
    path('search/<str:key>/', search, name='search'),
    path('parkedCars/', fetch_all_parked_cars, name='fetch_all_parked_cars'),

]
