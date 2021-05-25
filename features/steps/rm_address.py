import time

from behave import *

use_step_matcher("parse")


@then(u'I delete the address "{address_field}"')
def step_impl(context, address_field):
    from booking_manager.models import Address
    address = Address.objects.filter(address_field=address_field).get()
    context.browser.visit(context.get_url('delete_address', pk=address.id))
    context.browser.find_by_value('Yes').click()


@then(u'I cancel to delete the address "{address_field}"')
def step_impl(context, address_field):
    from booking_manager.models import Address
    address = Address.objects.filter(address_field=address_field).get()
    context.browser.visit(context.get_url('delete_address', pk=address.id))
    context.browser.find_by_value('Cancel').click()
