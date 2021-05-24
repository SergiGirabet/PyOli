import time

from behave import *

use_step_matcher("parse")


@then('I remove the "{booking}"')
def step_impl(context, booking):
    from booking_manager.models import Booking
    booking = Booking.objects.get()
    context.browser.visit(context.get_url('delete_booking', pk=booking.id))
    form = context.browser.find_by_tag('form').first
    form.find_by_text('Yes, delete it').click()


@then('I cancel the remove of a "booking"')
def step_impl(context):
    from booking_manager.models import Booking
    booking = Booking.objects.get()
    context.browser.visit(context.get_url('delete_booking', pk=booking.id))
    form = context.browser.find_by_tag('form').first
    form.find_by_text('Cancel').click()

