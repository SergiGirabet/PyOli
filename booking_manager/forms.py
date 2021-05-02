from django import forms

from booking_manager.models import ProductOrder


class DeliveryForm(forms.ModelForm):

    class Meta:
        model = ProductOrder
        fields = "__all__"
