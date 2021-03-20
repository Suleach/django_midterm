from django.shortcuts import render

# Create your views here.


def index(request):
    return(request, 'index.html')


def login(request):
    return(request, 'login.html')


def register(request):
    return(request, 'registration.html')
