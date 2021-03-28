from django.db import models
from django.contrib.auth.models import User
from address.models import AddressField

# Create your models here.

class Client(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = AddressField(on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateTimeField()


class Booking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class Table(models.Model):
    capacity = models.IntegerField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

