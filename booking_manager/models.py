from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    user = models.ManyToManyField(User)
    date = models.DateTimeField()
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class Table(models.Model):
    capacity = models.IntegerField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

