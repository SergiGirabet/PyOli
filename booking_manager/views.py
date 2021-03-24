from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Booking
from django.urls import reverse

# Create your views here.


class BookingView(CreateView):
    template_name = "main.html"
    model = Booking
    fields = "__all__"
    context_object_name = "booking"
    success_url = "/"


class BookingListView(ListView):
    template_name = "list.html"
    model = Booking
    context_object_name = "bookings"
