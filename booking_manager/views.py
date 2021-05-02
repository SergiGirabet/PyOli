from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import FormView, TemplateView, CreateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from booking_manager.models import Order, Booking, UserAddress, Product, ProductOrder


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


class DeliveryView(TemplateView):
    # Show all the products grouped by category
    # Input field for the quantity
    # When user clicks submit button -> check if there's stock
    # If all ok: create the Order after creating all the ProductOrder objects
    # TODO: Here we have to save the estimated hour (now + estimated) from google maps api (maybe a field in the model and substract it in the template??)
    # TODO: add a status field (Preparing, delivering, completed)
    template_name = "delivery.html"

    def get_context_data(self, **kwargs):
        context = {}
        context["products"] = Product.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        querydict: dict = request.POST.dict()
        querydict.pop("csrfmiddlewaretoken")
        address = querydict.pop("address")
        # TODO: address as input of form
        order = Order.objects.create(deliver_address_id=address, order_user=request.user, date_order=timezone.now())
        for product_id, quantity in querydict.items():
            if quantity > 0:
                product_order = ProductOrder.objects.create(ordered_product_id=product_id, quantity=quantity)
                product_order.save()
                order.products_ordered.add(product_order)
        order.save()
        return self.get(request, *args, **kwargs)


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
        context["orders"] = Order.objects.filter(order_user=self.request.user)
        context["bookings"] = Booking.objects.filter(booking_user=self.request.user)
        return context


class BookingView(CreateView):
    # Select number of people, day and hour
    # if there's a table with capacity >= num_people -> Create the booking and assign the table.
    pass
