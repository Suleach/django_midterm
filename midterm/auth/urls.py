from django.urls import path
from main.views import login, register

urlpatterns = [
    path('auth/login/', login),
    path('auth/regster/', register)
]
