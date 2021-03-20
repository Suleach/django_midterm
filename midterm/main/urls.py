from django.urls import path
from main.views import index, login, register

urlpatterns = [
    path('', index),
    path('auth/login/', login),
    path('auth/regster/', register)
]
