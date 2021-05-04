import datetime

from django.test import TestCase
from django.contrib.auth.models import User, Table

from .models import Booking


# Create your tests here.


'''
class BookATableTestCase(TestCase):



    def setUp(self):
        user1 = User.objects.create(username="user")
        table1 = Table(False, 4)
        #Booking.objects.create(booking_user=user, reserved_table="table", date=datetime.datetime)

    def test_empty_table(self):
        """The table is empty before a booking"""
        reserve = table1.reserve
        self.assertEqual(reserve, False)
'''