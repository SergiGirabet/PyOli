import django.db.models
from behave import *

use_step_matcher("parse")


@given('Exists a table "{table}" with capacity 2')
def step_impl(context, table):
    from booking_manager.models import Table
    Table.objects.create(capacity=2)


@given('Exists a book by "{username}" with password "{password}" at the table "{table}" 2 people this "{date}" day')
def step_impl(context, username, password, table, date):
    from booking_manager.models import Booking, Table
    from django.contrib.auth.models import User
    user = User.objects.create_user(username=username, email='user@example.com', password=password)

    table = Table.objects.create(capacity=2)
    Booking.objects.create(booking_user=user, reserved_table=table,
                           date="2021-05-18 19:17:16", people_number=2)


@when(u'I edit a book')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('edit_booking'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Book').first.click()


@then(u'The new date of the booking is {date}')
def step_impl(context, date):
    from booking_manager.models import Booking
    assert date == Booking.objects.get(date)
