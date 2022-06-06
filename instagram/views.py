from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm
from django.shortcuts import render, redirect
# Create your views here.
@login_required(login_url='/login/')
def welcome (request):

    return render(request, 'landing.html')



@login_required(login_url='/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.editor = current_user
            post.save()
        return redirect('landing')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'form': form})
    