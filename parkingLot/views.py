from django.http import HttpResponse, Http404
from .models import SlotDetails, Revenue
import random
import rstr
import re
from .utils import revenue_utils

# Create your views here.


def welcome_page(request):
    return HttpResponse("WELCOME TO THE PARKING LOT")


def create_lot(request, total_lots):
    lot_instance = SlotDetails.objects.all().count()
    if lot_instance:
        return HttpResponse("Parking Lot already exists with " + str(lot_instance) + " slots.")
    for i in range(total_lots):
        new_slot = SlotDetails()
        new_slot.save()
    initial_filled_slots = random.randint(1, (total_lots//2))
    filled_slots = random.sample(range(1, total_lots+1), initial_filled_slots)
    for i in filled_slots:
        car_registration_number = rstr.xeger(r'^[A-Z]{2}-[0-9]{2}-[A-Z]{2}-[0-9]{4}')
        car_color = random.choice(['BLUE', 'BLACK', 'WHITE', 'RED'])
        instance = SlotDetails(id=i, registration_number=car_registration_number, color=car_color, is_occupied=True)
        instance.save()

    return HttpResponse(str(total_lots) + " have been created. " + str(initial_filled_slots) + " have been filled.")


def add_car(request):
    find_empty_slot = SlotDetails.objects.filter(is_occupied=False).order_by('id')[0].id
    update_lot = SlotDetails(id=find_empty_slot, registration_number=request.POST['registration_number'], color=request.POST['color'], is_occupied=True)
    update_lot.save()
    return HttpResponse("Your car with registration number " + request.POST['registration_number'] +
                        " is parked in slot " + str(find_empty_slot))


def fetch_all_parked_cars(request):
    find_cars = SlotDetails.objects.filter(is_occupied=True)
    response = ''
    for i in find_cars:
        response += "Car with registration number " + i.registration_number + " is parked in slot " + str(
            i.id) + ".<br>"
    return HttpResponse(response)


def search(request, key):
    x = re.search("^[A-Z]{2}-[0-9]{2}-[A-Z]{2}-[0-9]{4}$", key)
    if x:
        find_slot = SlotDetails.objects.filter(registration_number=key)[0].id
        return HttpResponse("Car with registration number " + key + " is parked in slot " + str(find_slot))
    elif key in ['BLACK', 'WHITE', 'BLUE', 'RED']:
        find_cars = SlotDetails.objects.filter(color=key)
        response = ''
        for i in find_cars:
            response += "Car with registration number "+i.registration_number+" is parked in slot " + str(i.id)+".<br>"
        return HttpResponse(response)
    return Http404(key+" is not found.Try again.")


def remove_car(request):
    if 'registration_number' in request.POST:
        car_reg_number = request.POST['registration_number']
        find_slot = SlotDetails.objects.filter(registration_number=car_reg_number)[0]
        if find_slot:
            update_lot = SlotDetails(id=find_slot.id, registration_number=None,
                                     color=None, is_occupied=False)
            update_lot.save()
            parking_fee = calculate_revenue(find_slot)
            return HttpResponse("Car with registration number " + request.POST['registration_number']
                                + " has been removed. Total fee to be paid is Rs." + str(parking_fee))
    if 'slot_number' in request.POST:
        car_slot = request.POST['slot_number']
        car_details = SlotDetails.objects.filter(id=int(car_slot))[0]
        update_lot = SlotDetails(id=int(car_slot), registration_number=None,
                                 color=None, is_occupied=False)
        update_lot.save()
        parking_fee = calculate_revenue(car_details)
        return HttpResponse("Car in slot " + request.POST['slot_number'] +
                            " has been removed. Total fee to be paid is Rs." + str(parking_fee))

    return Http404("Information is incorrect.")


# calculates parking fee for the car and save it in DB
def calculate_revenue(car_info):
    parking_fee = revenue_utils.parking_fee(car_info.updated_at)
    add_revenue = Revenue(car_number=car_info.registration_number, parking_fee=parking_fee)
    add_revenue.save()
    return int(parking_fee)


# calculates total revenue(currently weekly)
def total_revenue(request):
    revenue = revenue_utils.calculate_total_revenue()
    return HttpResponse("Total revenue for last week is " + str(revenue))



