from django.db import models

class Venue(models.Model):

    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    longitude = models.DecimalField (max_digits=8, decimal_places=3)
    latitude = models.DecimalField (max_digits=8, decimal_places=3)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



