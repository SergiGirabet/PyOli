from behave import *

use_step_matcher("parse")


@when(u'I add an address')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('create_address'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Create_Address').first.click()


@then(u'There is {count:n} address')
def step_impl(context, count):
    from booking_manager.models import Address
    assert count == Address.objects.count()
