from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import FormView, TemplateView, ListView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from booking_manager.models import Order, Booking, UserAddress, Product, Table
from booking_manager.forms import *


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
    pass


class BookingList(ListView):
    model = Booking
    template_name = 'bookinglist.html'

    def get_queryset(self):
        return Booking.objects.filter(booking_user=self.request.user)


class BookingCreate(FormView):
    form_class = BookingForm
    template_name = 'creatingbooking.html'
    success_url = reverse_lazy('bookings')

    def form_valid(self, form):
        tables = Table.objects.filter(capacity__gte=form.cleaned_data['people_number'])
        for table in tables:
            bookings = Booking.objects.filter(reserved_table=table, date=form.cleaned_data['date'])
            if not bookings:
                t = table
                book = Booking(booking_user=self.request.user, reserved_table=t,
                               people_number=form.cleaned_data['people_number'], date=form.cleaned_data['date'])
                book.save()
                return super(BookingCreate, self).form_valid(form)

        return HttpResponseRedirect(reverse_lazy('book'))

class BookingDelete(DeleteView):
    form_class = BookingForm
    model = Booking
    template_name = 'deletingbooking.html'
    success_url = reverse_lazy('bookings')
