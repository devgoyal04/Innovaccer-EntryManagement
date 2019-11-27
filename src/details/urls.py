from django.urls import path

from .views import HomeView, CheckinView, CheckoutView

app_name = 'details'

urlpatterns = [
    path('', HomeView, name='home'),
    path('checkin/', CheckinView, name='checkIn'),
    path('checkout/', CheckoutView, name='checkOut'),
]
