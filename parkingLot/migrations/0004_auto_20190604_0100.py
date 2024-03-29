# Generated by Django 2.2.1 on 2019-06-03 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingLot', '0003_auto_20190604_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slotdetails',
            name='color',
            field=models.CharField(choices=[('BLACK', 'Black'), ('WHITE', 'White'), ('BLUE', 'Blue'), ('RED', 'Red')], default='NULL', max_length=5),
        ),
        migrations.AlterField(
            model_name='slotdetails',
            name='registration_number',
            field=models.CharField(default='AVAILABLE', max_length=13),
        ),
    ]
