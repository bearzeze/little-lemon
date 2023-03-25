from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/menu/', views.MenuItemsView.as_view()),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/bookings/', views.BookingsView.as_view()),
    path('api/bookings/<int:pk>', views.SingleBookingView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]