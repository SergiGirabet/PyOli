import time

from behave import *

import booking_manager.models

use_step_matcher("parse")


@given('Exists a table "{table}" with capacity 4')
def step_impl(context, table):
    from booking_manager.models import Table
    Table.objects.create(capacity=4)


@when(u'I book a table')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('book'))
        form = context.browser.find_by_tag('form').first
        context.browser.fill('people_number', row['people_number'])
        context.browser.fill('date', row['date'])
        context.browser.find_by_text(row['time_zone']).click()
        form.find_by_value('Submit').first.click()


@then(u'There is {count:n} booking')
def step_impl(context, count):
    from booking_manager.models import Booking
    assert count == Booking.objects.count()
