from __future__ import unicode_literals

from django.db import models

# Create your models here.

class WhereUsed(models.Model): 
    LIVINGROOM = 'LIVINGROOM'
    KITCHEN = 'KITCHEN'
    POWDERROOM = 'POWDERROOM'
    ANDREASBEDROOM = 'ANDREASBEDROOM'
    ELLIESBEDROOM = 'ELLIESBEDROOM'
    MASTERBEDROOM = 'MASTERBEDROOM'
    MASTERBATH = 'MASTERBATH'
    GIRLSBATH = 'GIRLSBATH'
    GARAGE = 'GARAGE'
    FRONTYARD = 'FRONTYARD'
    BACKYARD = 'BACKYARD'

    CHOICES = (
        (LIVINGROOM, 'Living Room'),
        (KITCHEN, 'Kitchen Room'),
        (POWDERROOM, 'Powder Room'),
        (ANDREASBEDROOM, 'Andrea\'s Bedroom'),
        (ELLIESBEDROOM, 'Ellie\'s Bedroom'),
        (MASTERBEDROOM, 'Master Bedroom'),
        (MASTERBATH, 'Master Bath'),
        (GIRLSBATH, 'Girl\'s Bath'),
        (GARAGE, 'Garage'),
        (FRONTYARD, 'Front Yard'),
        (BACKYARD, 'Back Yard'),
    )

class WishList(models.Model):
    what = models.CharField(max_length=50)
    desc = models.TextField(blank=True)
    where = models.CharField(max_length=15,choices=WhereUsed.CHOICES)
