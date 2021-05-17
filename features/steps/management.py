from behave import *

use_step_matcher("parse")


@given('Exists a table "{table}" with capacity 4')
def step_impl(context, table):
    from booking_manager.models import Table
    Table.objects.create(capacity=4)

