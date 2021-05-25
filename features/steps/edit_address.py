import time

from behave import *

use_step_matcher("parse")


@then(u'There is {count:n} address with address {address_field}')
def step_impl(context, count, address_field):
    from booking_manager.models import Address
    assert count == Address.objects.count()
    assert address_field == Address.objects.get().address_field


@then(u'I edit the "{address}"')
def step_impl(context, address):
    for row in context.table:
        from booking_manager.models import Address
        address = Address.objects.get()
        context.browser.visit(context.get_url('edit_address', pk=address.id))
        context.browser.fill('address_field', row['address_field'])
        context.browser.find_by_value('Confirm').click()

