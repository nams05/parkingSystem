# Generated by Django 2.2.1 on 2019-06-04 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parkingLot', '0005_delete_slotdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlotDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('registration_number', models.CharField(default='AVAILABLE', max_length=13)),
                ('color', models.CharField(choices=[('BLACK', 'Black'), ('WHITE', 'White'), ('BLUE', 'Blue'), ('RED', 'Red')], default='NULL', max_length=5)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]