from django.urls import path
from .views import *

urlpatterns = [
        path('login', login, name="login"),
        path('register', register, name="register"),
        path('contact_us', contact, name="contact_us"),
]