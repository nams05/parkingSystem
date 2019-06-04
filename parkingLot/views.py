
from django.http import HttpResponse
from rest_framework import generics
from .serializers import *
from .models import SlotDetails
import random
import rstr
# Create your views here.


def create_lot(request, total_lots):
    lot_instance = SlotDetails.objects.all().count()
    if(lot_instance):

        return HttpResponse("Parking Lot already exists with " + str(lot_instance) + " slots.")
    for i in range(total_lots):
        new_slot = SlotDetails()
        new_slot.save()
    initial_filled_slots = random.randint(1, (total_lots//2))
    filled_slots = random.sample(range(1, total_lots+1), initial_filled_slots)
    for i in filled_slots:
        car_registration_number = rstr.xeger(r'^[A-Z]{2}-[0-9]{2}-[A-Z]{2}-[0-9]{4}')
        car_color = random.choice(['BLUE', 'BLACK', 'WHITE', 'RED'])
        instance = SlotDetails(id=i, registration_number=car_registration_number, color=car_color)
        instance.save()

    return HttpResponse(str(total_lots) + " have been created. " + str(initial_filled_slots) + " have been filled.")


def add_car(request):
    find_empty_slot = SlotDetails.objects.filter(is_occupied='FALSE').order_by('id')[0:1]
    # update_lot = SlotDetails(id=find_empty_slot)
    return HttpResponse("Your car with registration number is parked in slot.")


def fetch_all_parked_cars(request):
    return HttpResponse("All the cars")


def search(request, key):
    return HttpResponse("search result")


def remove_car(request):
    return HttpResponse("car has been removed")

# class CreateLotView(generics.ListCreateAPIView):
#     queryset = SlotDetails.objects.all()
#     serializer_class = SlotDetailsSerializer
#
#     def create_lot(self, serializer):
#         """Save the post data when creating a new lot."""
#
#         serializer.save()
#
#
# class CreateView(generics.ListCreateAPIView):
#     """This class defines the create behavior of our rest api."""
#     queryset = CarDetails.objects.all()
#     serializer_class = CarDetailsSerializer
#
#     def park_car(self, serializer):
#         """Save the post data when creating a new bucketlist."""
#         serializer.save()
#
#
# class DetailsView(generics.RetrieveUpdateDestroyAPIView):
#     """This class handles the http GET, PUT and DELETE requests."""
#
#     queryset = CarDetails.objects.all()
#     serializer_class = CarDetailsSerializer
#
#
#
