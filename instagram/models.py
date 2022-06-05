from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
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
    post = models.ImageField(upload_to = 'media/posts', blank = False)
    tags = models.ManyToManyField(tags)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)

