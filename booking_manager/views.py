import os
from datetime import datetime

import googlemaps
from behave.formatter import null
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import FormView, TemplateView, CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import BaseFormView

from booking_manager.forms import *
from booking_manager.models import Order, Booking, Product, ProductOrder, Address, Table

RESTAURANT_ADDRESS = "Carrer de Jaume II, 69, 25001 Lleida"


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


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = Order.objects.filter(order_user=self.request.user)
        context["bookings"] = Booking.objects.filter(booking_user=self.request.user)
        context["addresses"] = Address.objects.filter(user_id=self.request.user)
        return context


class AddressCreate(CreateView):
    model = Address
    fields = ['address_field']
    template_name = 'createaddress.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        address = Address.objects.create(user=self.request.user, address_field=form.cleaned_data['address_field'])
        address.save()
        return redirect('profile')


class AddressDelete(LoginRequiredMixin, DeleteView):
    model = Address
    template_name = 'deletingaddress.html'
    success_url = reverse_lazy('profile')

    @model.verifier()
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @model.verifier()
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class AddressEdit(LoginRequiredMixin, UpdateView):
    model = Address
    template_name = "editaddress.html"
    fields = ["address_field"]
    success_url = reverse_lazy('profile')

    @model.verifier()
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @model.verifier()
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DeliveryView(LoginRequiredMixin, TemplateView):
    template_name = "delivery.html"

    def get_context_data(self, **kwargs):
        context = {"products": Product.objects.all(),
                   "addresses": Address.objects.filter(user_id=self.request.user)}
        return context

    def post(self, request, *args, **kwargs):
        querydict: dict = request.POST.dict()
        querydict.pop("csrfmiddlewaretoken")

        if not request.POST.get("address"):
            return redirect('delivery')
        address = querydict.pop("address")

        order = Order.objects.create(deliver_address_id=address, order_user=request.user, date_order=timezone.now(),
                                     expected_delivery_date=timezone.now())
        total_quantity = 0
        for product_id, quantity in querydict.items():
            quantity = int(quantity)
            product = Product.objects.get(pk=product_id)
            if 0 < quantity <= product.stock:
                product.stock -= quantity
                product_order = ProductOrder.objects.create(ordered_product_id=product_id, quantity=quantity,
                                                            order=order)
                product_order.save()
                product.save()
            total_quantity += quantity
        if total_quantity == 0:
            order.delete()
            return redirect('delivery')

        user_address = Address.objects.get(pk=address, user=request.user)
        api_key = os.environ.get("API_KEY")
        if api_key:
            client = googlemaps.Client(key=api_key)
            response = client.distance_matrix(RESTAURANT_ADDRESS, user_address.address_field)
            distance_seconds = response["rows"][0]["elements"][0]["duration"]["value"]
        else:
            distance_seconds = 10 * 60  # 10 minutes if api not available
        average_preparing_time = 20 * 60  # 20 minutes in seconds for preparing
        order.expected_delivery_date = datetime.fromtimestamp(timezone.now().timestamp() +
                                                              distance_seconds + average_preparing_time)
        order.save()
        return redirect('profile')


class Backoffice(LoginRequiredMixin, TemplateView):
    template_name = "backoffice.html"
    form_class = OrderForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["pending"] = Order.objects.filter(status=Order.PENDING).order_by('-expected_delivery_date')
        context["preparing"] = Order.objects.filter(status=Order.PREPARING).order_by('-expected_delivery_date')
        context["delivering"] = Order.objects.filter(status=Order.DELIVERING).order_by('-expected_delivery_date')

        today = datetime.today()
        context["bookings"] = Booking.objects.filter(date__year=today.year,
                                                     date__month=today.month,
                                                     date__day=today.day).order_by('date')
        context["form"] = OrderForm()
        return context


class OrderUpdateStatus(LoginRequiredMixin, BaseFormView):
    form_class = OrderForm
    success_url = reverse_lazy('backoffice')

    def form_valid(self, form):
        order = Order.objects.get(pk=self.kwargs["pk"])
        order.status = form.cleaned_data["status"]
        order.save()
        return super().form_valid(form)


class BookingCreate(LoginRequiredMixin, FormView):
    form_class = BookingForm
    template_name = 'creatingbooking.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        tables = Table.objects.filter(capacity__gte=form.cleaned_data['people_number']).order_by('capacity')
        for table in tables:
            bookings = Booking.objects.filter(reserved_table=table, date=form.cleaned_data['date'],
                                              time_zone=form.cleaned_data['time_zone'])
            if not bookings:
                book = Booking(booking_user=self.request.user, reserved_table=table,
                               people_number=form.cleaned_data['people_number'], date=form.cleaned_data['date'],
                               time_zone=form.cleaned_data['time_zone'])
                book.save()
                return super(BookingCreate, self).form_valid(form)

        return HttpResponseRedirect(reverse_lazy('book'))


class BookingDelete(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'deletingbooking.html'
    success_url = reverse_lazy('profile')

    @model.verifier()
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @model.verifier()
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class BookingUpdate(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'creatingbooking.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        book = Booking.objects.get(pk=self.kwargs['pk'])

        tables = Table.objects.filter(capacity__gte=form.cleaned_data['people_number']).order_by('capacity')
        for table in tables:
            bookings = Booking.objects.filter(reserved_table=table, date=form.cleaned_data['date'],
                                              time_zone=form.cleaned_data['time_zone'])
            if not bookings:
                book.people_number = form.cleaned_data['people_number']
                book.date = form.cleaned_data['date']
                book.time_zone = form.cleaned_data['time_zone']
                book.reserved_table = table
                return super(BookingUpdate, self).form_valid(form)

        return HttpResponseRedirect(reverse_lazy('profile'))

    @model.verifier()
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @model.verifier()
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
