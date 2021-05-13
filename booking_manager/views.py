import datetime
from datetime import date
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import DateTimeField
from django.views.generic import FormView, TemplateView, CreateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.db import models
from booking_manager.models import Order, Booking, UserAddress, Product
from operator import attrgetter
from django.shortcuts import render
from django.http import HttpResponse


class Login(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class Register(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class Home(TemplateView):
    template_name = "home.html"


class ProfileView(TemplateView, LoginRequiredMixin):
    # User should be able to modify and delete an
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = Order.objects.filter(order_user=self.request.user)
        context["bookings"] = Booking.objects.filter(booking_user=self.request.user)
        context["addresses"] = UserAddress.objects.filter(user_id=self.request.user)
        return context


class DeliveryView(ListView):
    # Show all the products grouped by category
    # Input field for the quantity
    # When user clicks submit button -> check if there's stock
    # If all ok: create the Order after creating all the ProductOrder objects
    # TODO: Here we have to save the estimated hour (now + estimated) from google maps api (maybe a field in the model and substract it in the template??)
    # TODO: add a status field (Preparing, delivering, completed)
    template_name = "delivery.html"
    model = Product
    context_object_name = "products"


class Backoffice(TemplateView):
    # Show number of current orders
    # Show current orders (older first)
    # Show number of current bookings
    # Show current bookings (for today)
    # Manage orders, bookings and products ??? We can do it with admin interface
    # TODO: orders by state ?? And show a counter of the orders by state.
    template_name = "backoffice.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["n_pending"] = len(Order.objects.filter(status=Order.PENDING))
        context["pending"] = Order.objects.filter(status=Order.PENDING).order_by('-expected_delivery_date')

        context["n_preparing"] = len(Order.objects.filter(status=Order.PREPARING))
        context["preparing"] = Order.objects.filter(status=Order.PREPARING).order_by('-expected_delivery_date')

        context["n_delivering"] = len(Order.objects.filter(status=Order.DELIVERING))
        context["delivering"] = Order.objects.filter(status=Order.DELIVERING).order_by('-expected_delivery_date')

        today = datetime.datetime.today()
        context["n_bookings"] = len(Booking.objects.filter(date__year=today.year,
                                                           date__month=today.month,
                                                           date__day=today.day))
        context["bookings"] = Booking.objects.filter(date__year=today.year,
                                                     date__month=today.month,
                                                     date__day=today.day).order_by('date')

        return context

    '''

    def new_status(self, **kwargs):
        orders = Order.objects.get()
        orders.status =
        orders.save()
        return redirect()
        
'''


class BookingView(CreateView):
    # Select number of people, day and hour
    # if there's a table with capacity >= num_people -> Create the booking and assign the table.
    pass
