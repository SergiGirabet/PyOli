from django.views.generic import FormView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from .models import Booking
from django.urls import reverse_lazy


class Login(LoginView):
    template_name = "login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class Register(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')


class Home(ListView):
    model = Booking
    template_name = "home.html"
