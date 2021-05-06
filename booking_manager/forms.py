from django import forms

from booking_manager.models import ProductOrder, Address


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = ProductOrder
        fields = "__all__"
