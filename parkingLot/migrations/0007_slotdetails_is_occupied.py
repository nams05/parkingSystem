# Generated by Django 2.2.1 on 2019-06-04 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingLot', '0006_slotdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='slotdetails',
            name='is_occupied',
            field=models.BooleanField(default=False),
        ),
    ]
