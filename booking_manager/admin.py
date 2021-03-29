from django.contrib import admin
from .models import Client, Order, Table, Booking, Category, Product, ProductOrder

# Register your models here.

admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Table)
admin.site.register(Booking)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductOrder)
