import operator
import time
from functools import reduce

import django.db.models
from behave import *
from django.db.models import Q

use_step_matcher("parse")


@then('I edit the booking of a "{booking}"')
def step_impl(context, booking):
    for row in context.table:
        from booking_manager.models import Booking
        booking = Booking.objects.get()
        context.browser.visit(context.get_url('edit_booking', pk=booking.id))
        form = context.browser.find_by_tag('form').first
        context.browser.find_by_text(row['time_zone']).click()
        form.find_by_value('Submit').first.click()


@then(u'There is {count:n} booking with time zone {time_zone}')
def step_impl(context, count, time_zone):
    from booking_manager.models import Booking
    assert count == Booking.objects.count()
    assert time_zone == Booking.objects.get().time_zone
