import time

from behave import *

use_step_matcher("parse")


@step(u'Exists a product "{product}" with category "{category}"')
def step_impl(context, product, category):
    from booking_manager.models import Category, Product
    category = Category.objects.create(name='Wine')
    Product.objects.create(product_category=category, name='Sweet wine',
                           description='Nice and smooth', price=9.89,
                           stock=20, modifiable=True)


@step(u'Exists an address "{address}" by "{user}"')
def step_impl(context, address, user):
    from booking_manager.models import Address, User
    user = User.objects.get()
    Address.objects.create(address_field='Rambla Ferran 32, Lleida',
                           user=user)


@when(u'I add a delivery')
def step_impl(context):
    from booking_manager.models import Product
    for row in context.table:
        context.browser.visit(context.get_url('delivery'))
        product = Product.objects.get()
        context.browser.fill(product.id, row['quantity'])
        context.browser.find_by_value('Order now').click()


@then(u'There is {count:n} delivery')
def step_impl(context, count):
    from booking_manager.models import Order
    assert count == Order.objects.count()
