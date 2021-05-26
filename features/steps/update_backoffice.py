import time

from behave import *

import booking_manager.models

use_step_matcher("parse")


@step(u'Exists an order "{order}"')
def step_impl(context, order):
    from booking_manager.models import Order, User, Address
    user = User.objects.get()
    address = Address.objects.create(address_field='Rambla Ferran 32, Lleida',
                                     user=user)
    Order.objects.create(order_user=user, deliver_address=address,
                         date_order='2021-05-25 18:31:46', status='PENDING',
                         expected_delivery_date='2021-05-25 18:55:46')
    print(Order.objects.get())


@then(u'I update the status')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('backoffice'))
        context.browser.find_by_text(row['status']).first.click()
        context.browser.find_by_value('Update').click()


@step(u'The status of an order is {status}')
def step_impl(context, status):
    from booking_manager.models import Order
    assert status == Order.objects.get().status
