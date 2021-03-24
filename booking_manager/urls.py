from django.urls import path
from .views import BookingView, BookingListView

urlpatterns = [
    path('', BookingView.as_view(), name="booking"),
    path('list/', BookingListView.as_view(), name="list")
]
