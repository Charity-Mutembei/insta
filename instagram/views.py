from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def welcome (request):

    return render(request, 'landing.html')

def register(request):
    return render(request, 'registration/registration_form.html')

def login (request):
    return render(request, 'registration/login.html')