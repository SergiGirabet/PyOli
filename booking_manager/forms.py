from django import forms
from django.forms import DateInput

from booking_manager.models import ProductOrder, Booking, Order


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = ProductOrder
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductOrder
        fields = "__all__"


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']


class MyDateInput(DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['people_number', 'date', 'time_zone']
        widgets = {'date': MyDateInput}
