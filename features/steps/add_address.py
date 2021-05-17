from behave import *

use_step_matcher("parse")


@when(u'I book a table')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('book'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Book').first.click()


@then(u'There is {count:n} booking')
def step_impl(context, count):
    from booking_manager.models import Booking
    assert count == Booking.objects.count()
