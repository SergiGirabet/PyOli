from django.urls import path
from .views import Home, Login, Register, ProfileView, DeliveryView, BookingView, Backoffice, AddressCreate, \
    AddressDelete
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('register/', Register.as_view(), name="register"),
    path('logout/', LogoutView.as_view(next_page="home"), name="logout"),
    path('login/', Login.as_view(), name="login"),
    path('backoffice/', Backoffice.as_view(), name="backoffice"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('delivery/', DeliveryView.as_view(), name="delivery"),
    path('booking/', BookingView.as_view(), name="booking"),
    path('createaddress/', AddressCreate.as_view(), name="createaddress"),
    path('deleteaddress/', AddressDelete.as_view(), name="deleteaddress"),

]
