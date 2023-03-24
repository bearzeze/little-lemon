from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["title", "price"]
        

class BookingSerializer(serializers.ModelSerializer):
    number_of_guests = serializers.IntegerField(source="no_of_guests")
    date = serializers.DateTimeField(source="booking_date")
    class Meta:
        model = Booking
        fields = ["date","name", "number_of_guests"]