from django.contrib import admin
from .models import Address, Order, Table, Booking, Category, Product, ProductOrder

# Register your models here.

admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Table)
admin.site.register(Booking)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductOrder)
