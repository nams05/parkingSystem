from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CarDetails(TimeStampedModel):
    colorOptions = (('BLACK', 'Black'), ('WHITE', 'White'), ('BLUE', 'Blue'), ('RED', 'Red'))
    registration_number = models.CharField(max_length=13)
    color = models.CharField(max_length=5, choices=colorOptions)

    def __str__(self):
        return self.registration_number + " " + self.color


class SlotDetails(TimeStampedModel):
    carId = models.ForeignKey(CarDetails, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.carId


