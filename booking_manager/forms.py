from django import forms

from booking_manager.models import ProductOrder


class ProductForm(forms.ModelForm):

    class Meta:
        model = ProductOrder
        fields = "__all__"
