from .models import Post, Profile
from django import forms
from django.forms import ModelForm


class NewPostForm(forms.ModelForm):
    post_image  = forms.ImageField(required = True)
    post_text  = forms.CharField(max_length=250)
    tags = forms.CharField(max_length=100)

    class Meta:
        model = Post
        fields = ('post_image', 'post_text', 'tags')
class ProfileForm(forms.ModelForm):
    profilePhoto = forms.ImageField(required = True)
    Bio = forms.CharField(max_length=500)
