from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm
from django.shortcuts import render, redirect
# Create your views here.
@login_required(login_url='/login/')
def welcome (request):

    return render(request, 'landing.html')

def register(request):
    return render(request, 'registration/registration_form.html')

def login (request):
    return render(request, 'registration/login.html')

# @login_required(login_url='/login/')
def new_post(request):
   
    return render(request, 'new_post.html')
    