from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class SlotDetails(TimeStampedModel):
    colorOptions = (('BLACK', 'Black'), ('WHITE', 'White'), ('BLUE', 'Blue'), ('RED', 'Red'))
    registration_number = models.CharField(max_length=13,  default=None, null=True)
    color = models.CharField(max_length=5, choices=colorOptions, default=None, null=True)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return str(id) + self.registration_number + " " + self.color

    class Meta:
        ordering = ('id',)


class Revenue(TimeStampedModel):
    parking_fee = models.IntegerField()
    car_number = models.CharField(max_length=13, null=True)

    class Meta:
        ordering = ('created_on',)

