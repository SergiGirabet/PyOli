from django.views.generic import FormView, ListView
from django.contrib.auth.views import LoginView
from .models import Booking
from django.urls import reverse


# Create your views here.


class Login(LoginView):
    template_name = "login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('home')


class Register(FormView):
    template_name = "register.html"


class Home(ListView):
    model = Booking
    template_name = "home.html"
