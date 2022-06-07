from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, ProfileForm
from django.shortcuts import render, redirect
from .models import Post, Stream, Profile
from django.db.models import Q
# Create your views here.
# @login_required(login_url='/login/')
# def welcome (request):
#     '''
#     this is the landing page. Containns the home page of this application
#     '''
#
#     posts = Post.objects.all()
#     print('post', posts)
#
#     return render (request, 'landing.html', {'posts': posts})


@login_required(login_url='/login/')
def welcome(request):
    posts= Post.objects.all()
    print('post', posts)

    return render(request, 'landing.html', {"posts": posts})
@login_required(login_url='/login/')
def userProfile(request):
    profiles = Profile.objects.all()
    print('profile', profiles)


    return render(request, 'profile.html', {"profiles": profiles})
@login_required(login_url='/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.editor = current_user
            post.save()
        return redirect('welcome')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'form': form})
@login_required(login_url='/login/')
def userProfileEdit(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.editor = current_user
            profile.save()

        return redirect('welcome')

    else:
        form = ProfileForm()

    return render(request, 'profile-edit.html', {'form': form})
