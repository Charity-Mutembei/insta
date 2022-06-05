from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank = True)


    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()
    class Meta:
        ordering = ['first_name']
class tags(models.Model):
    name = models.CharField(max_length = 30)

    def __str__ (self):
        return self.name
class Post(models.Model):
    location = models.CharField(max_length= 100)
    post = HTMLField(default="Some String")
    post_image = models.ImageField(upload_to = 'media/posts', blank = False, default='')
    tags = models.ManyToManyField(tags)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)

