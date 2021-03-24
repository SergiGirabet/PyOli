from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

# Create your views here.


class Booking(CreateView):
    template_name = "main.html"
    model = None