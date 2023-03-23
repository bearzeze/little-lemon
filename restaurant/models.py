from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(default=2)
    booking_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.name} on {self.booking_date.day}.{self.booking_date.month}.{self.booking_date.year} time - {self.booking_date.hour}:{self.booking_date.minute}h"
    
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(default=1)
    
    def __str__(self):
        return f"{self.title} - {self.price} €"
    
    