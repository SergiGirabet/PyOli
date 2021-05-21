import django.db.models
from behave import *
from django.db import models

use_step_matcher("parse")


@given('Exists a product "{product}" with category "{category}"')
def step_impl(context, product, category):
    from booking_manager.models import Product, Category
    product_category = Category.objects.create(name=category)
    Product.objects.create(product_category=product_category, name=product,
                           description='Delicious', price=16.95, stock=10, modifiable=True)


@given('Exists an "{order}" by "{user}"')
def step_impl(context, order, user):
    from booking_manager.models import Order, Address, User
    user = User.objects.get(username=user)
    address = Address.objects.create(user=user, address_field="Rambla Ferran 32, Lleida")
    Order.objects.create(order_user=user, deliver_address=address,
                         date_order="2021-05-18 20:17:16",
                         date_created=models.DateTimeField(auto_now_add=True),
                         expected_delivery_date="2021-05-18 20:17:16",
                         status='Pending')


# DOESN'T WORK
@when("I create a delivery")
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('delivery'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Book').first.click()
