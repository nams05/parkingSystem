from django.db import models

# Create your models here.


class CarDetails(models.Model):
    colorOptions = (('BLK', 'Black'), ('WHT', 'White'), ('BLU', 'Blue'), ('RED', 'Red'))
    registration_number = models.CharField(max_length=13)
    color = models.CharField(max_length=5, choices=colorOptions)


class SlotDetails(models.Model):
    carId = models.ForeignKey(CarDetails, on_delete=models.CASCADE, default=0)
