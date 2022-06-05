from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    location = models.CharField(max_length= 100)
    post = models.ImageField(upload_to = 'media/posts', blank = False)
    tags = models.ManyToManyField(tags)

class tags(models.Model):
    name = models.CharField(max_length = 30)

    def __str__ (self):
        return self.name