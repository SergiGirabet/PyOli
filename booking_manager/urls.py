from django.urls import path, reverse
from .views import Home, Login, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('register/', Register.as_view(), name="register"),
    path('logout/', LogoutView.as_view(next_page="home"), name="logout"),
    path('login/', Login.as_view(template_name="login.html"), name="login")
]
