from .models import Post
from django import forms
from django.forms import ModelForm


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }