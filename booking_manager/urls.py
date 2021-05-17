from django.urls import path
from .views import Home, Login, Register, ProfileView, DeliveryView, Backoffice, AddressCreate, \
    AddressDelete, AddressEdit, BookingCreate, BookingDelete, BookingUpdate, OrderUpdateStatus
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('register/', Register.as_view(), name="register"),
    path('logout/', LogoutView.as_view(next_page="home"), name="logout"),
    path('login/', Login.as_view(), name="login"),
    path('backoffice/', Backoffice.as_view(), name="backoffice"),
    path('orderupdatestatus/<int:pk>', OrderUpdateStatus.as_view(), name="order_update_status"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('delivery/', DeliveryView.as_view(), name="delivery"),
    path('book/', BookingCreate.as_view(), name="book"),
    path('delete-booking/<int:pk>', BookingDelete.as_view(), name="delete_booking"),
    path('edit-booking/<int:pk>', BookingUpdate.as_view(), name="edit_booking"),
    path('create-address/', AddressCreate.as_view(), name="create_address"),
    path('delete-address/<int:pk>', AddressDelete.as_view(), name="delete_address"),
    path('edit-address/<int:pk>', AddressEdit.as_view(), name="edit_address"),

]
