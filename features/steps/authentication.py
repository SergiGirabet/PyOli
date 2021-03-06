import time

from behave import *

use_step_matcher("parse")


@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, email='user@example.com', password=password)


@given('Exists a super user "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    User.objects.create_superuser(username=username, email='user@example.com', password=password)


@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('login'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('Login').first.click()


@then("I logout so there is {login}")
def step_impl(context, login):
    context.browser.visit(context.get_url('logout'))
    assert context.get_url('home') == context.browser.url
