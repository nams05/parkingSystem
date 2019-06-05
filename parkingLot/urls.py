# urlConf file to map url to views

from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', welcome_page, name='welcome_page'),
    path('create/<int:total_lots>',  create_lot, name='create_lot'),
    path('parkCar/', csrf_exempt(add_car), name='add_car'),
    path('removeCar/', csrf_exempt(remove_car), name='remove_car'),
    path('search/<str:key>', search, name='search'),
    path('allParkedCars/', fetch_all_parked_cars, name='fetch_all_parked_cars'),
    path('revenue/', total_revenue, name='total_revenue'),
]
