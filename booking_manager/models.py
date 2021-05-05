from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    address_field = models.CharField(max_length=150)

    def __str__(self):
        return self.address_field

    class Meta:
        verbose_name_plural = 'addresses'


class UserAddress(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "User Addresses"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    stock = models.IntegerField()
    modifiable = models.BooleanField()

    def __str__(self):
        return self.name


class ProductOrder(models.Model):
    ordered_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{type(self).__name__}(product={self.ordered_product}, quantity={self.quantity})"


class Order(models.Model):
    order_user = models.ForeignKey(User, on_delete=models.CASCADE)
    deliver_address = models.ForeignKey('Address', on_delete=models.CASCADE)
    date_order = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    products_ordered = models.ManyToManyField(ProductOrder)

    def __str__(self):
        return f"{type(self).__name__}(id={self.id}, user={self.order_user})"


class Table(models.Model):
    capacity = models.IntegerField()

    def __str__(self):
        return str(self.id)


class Booking(models.Model):
    booking_user = models.ForeignKey(User, on_delete=models.CASCADE)
    reserved_table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateTimeField()
    people_number = models.IntegerField()

    def __str__(self):
        return f"{type(self).__name__}(table={self.reserved_table}, date={self.date.strftime('%d/%m/%Y - %H:%M')})"
