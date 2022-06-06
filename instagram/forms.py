from .models import Post
from django.forms import ModelForm


class NewPostForm(ModelForm):    

    class Meta:
        model = Post
        exclude = ['editor', 'likes', 'comment']
       