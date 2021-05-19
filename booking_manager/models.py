from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect


class Address(models.Model):
    address_field = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address_field

    @classmethod
    def verifier(cls):
        def wrapper(func):
            def innner(*args, **kwargs):
                object_ = cls.objects.get(pk=kwargs["pk"])
                request = args[1]
                if object_.user != request.user:
                    return redirect('profile')
                return func(*args, **kwargs)

            return innner

        return wrapper

    class Meta:
        verbose_name_plural = 'addresses'


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

    class Meta:
        ordering = ["product_category"]

    def __str__(self):
        return self.name


class Order(models.Model):
    PENDING = "PENDING"
    PREPARING = "PREPARING"
    DELIVERING = "DELIVERING"
    COMPLETED = "COMPLETED"
    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (PREPARING, "Preparing"),
        (DELIVERING, "Delivering"),
        (COMPLETED, "Completed"))
    order_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    deliver_address = models.ForeignKey('Address', on_delete=models.CASCADE)
    date_order = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    expected_delivery_date = models.DateTimeField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f"{type(self).__name__}(id={self.id}, user={self.order_user})"

    @classmethod
    def verifier(cls):
        def wrapper(func):
            def innner(*args, **kwargs):
                object_ = cls.objects.get(pk=kwargs["pk"])
                request = args[1]
                if object_.order_user != request.user:
                    return redirect('profile')
                return func(*args, **kwargs)

            return innner

        return wrapper


class ProductOrder(models.Model):
    ordered_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{type(self).__name__}(product={self.ordered_product}, quantity={self.quantity})"


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

    @classmethod
    def verifier(cls):
        def wrapper(func):
            def innner(*args, **kwargs):
                object_ = cls.objects.get(pk=kwargs["pk"])
                request = args[1]
                if object_.booking_user != request.user:
                    return redirect('profile')
                return func(*args, **kwargs)
            return innner
        return wrapper
