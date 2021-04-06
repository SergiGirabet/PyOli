from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, related_name='user_id', on_delete=models.CASCADE)
    phone_number = models.DecimalField(decimal_places=0, max_digits=9, blank=True, null=True)

    def __str__(self):
        return f"{type(self).__name__}(id={self.id}, username={self.user.username})"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    date_order = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{type(self).__name__}(id={self.id}, client={self.client})"


class Table(models.Model):
    reserve = models.BooleanField()
    capacity = models.IntegerField()

    def __str__(self):
        return str(self.id)


class Booking(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateTimeField()

    people_number = models.IntegerField()

    def __str__(self):
        return f"{type(self).__name__}(table={self.table}, date={self.date.strftime('%d/%m/%Y - %H:%M')})"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    stock = models.IntegerField()
    modifiable = models.BooleanField()

    def __str__(self):
        return self.name


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{type(self).__name__}(product={self.product}, order={self.order}, quantity={self.quantity})"