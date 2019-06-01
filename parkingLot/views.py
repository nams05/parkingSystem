from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello world!")


def setCarDetails(request):
    return HttpResponse("Your car with registration number is parked in slot.")


def fetchAllParkedCars(request):
    return HttpResponse("All the cars")


def search(request, key):
    return HttpResponse("search result")

def removeCar(request):
    return HttpResponse("car has been removed")

