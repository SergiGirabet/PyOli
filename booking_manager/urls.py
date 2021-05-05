from django.urls import path
from .views import Home, Login, Register, ProfileView, DeliveryView, BookingCreate, BookingList, Backoffice, BookingDelete
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('register/', Register.as_view(), name="register"),
    path('logout/', LogoutView.as_view(next_page="home"), name="logout"),
    path('login/', Login.as_view(), name="login"),
    path('backoffice/', Backoffice.as_view(), name="backoffice"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('delivery/', DeliveryView.as_view(), name="delivery"),
    path('bookings/', BookingList.as_view(), name="bookings"),
    path('book/', BookingCreate.as_view(), name="book"),
    path('deletebooking/<int:pk>', BookingDelete.as_view(), name="deletebooking")
]
