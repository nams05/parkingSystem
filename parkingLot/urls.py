# urlConf file to map url to views

from django.urls  import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
