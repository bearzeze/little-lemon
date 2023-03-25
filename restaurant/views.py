from django.shortcuts import render
from django.http import JsonResponse
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

# Create your views here.
def home(request):
    return render(request, "index.html", {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get_permissions(self):
        permission_classes = []
        
        if self.request.method == "POST":
            permission_classes = [IsAdminUser]
        
        return [permission() for permission in permission_classes]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get_permissions(self):
        permission_classes = []
        
        if self.request.method != "GET":
            permission_classes = [IsAdminUser]
        
        return [permission() for permission in permission_classes]
    

class BookingsView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_permissions(self):
        permission_classes = []
        
        if self.request.method == "POST":
            permission_classes = [IsAdminUser]
        
        return [permission() for permission in permission_classes]    
    
    
class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_permissions(self):
        permission_classes = []
        
        if self.request.method != "GET":
            permission_classes = [IsAdminUser]
        
        return [permission() for permission in permission_classes]
    