from django.urls import path
from .views import Booking


urlpatterns = [
    path('', Booking.as_view(), name="Booking")
]