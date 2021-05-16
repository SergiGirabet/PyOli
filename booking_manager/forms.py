from django import forms
from django.forms import DateTimeInput, DateInput

from booking_manager.models import ProductOrder, Booking


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = ProductOrder
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductOrder
        fields = "__all__"


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['people_number', 'date']
