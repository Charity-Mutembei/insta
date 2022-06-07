from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class tags(models.Model):
    name = models.CharField(max_length = 30)

    def __str__ (self):
        return self.name

class Profile(models.Model):
    profilePhoto = models.ImageField()
    Bio = models.TextField(max_length=500, blank=True)


class Post(models.Model):
    post_text = models.TextField(max_length= 100, blank = True)
    post_image = models.ImageField(upload_to = 'posts', blank = False, default='')
    tags = models.ManyToManyField(tags)

    def __str__(self):
        return self.post_text


    def save_post(self):
        self.save()


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete= models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete= models.CASCADE, related_name='following')
class Stream (models.Model):
    following = models.ForeignKey(User, on_delete= models.CASCADE, related_name='stream_following')
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def add_post(sender, instance, *args, **kwargs):
        post= instance
        user = post.user
        followers = Follow.objects.all().filter(following = user)
        for follower in followers:
            stream = Stream(post = post, user = follower.follower, date= post.posted, following= user)
            stream.save()
    # def post_save.connect(Stream.add_post, sender = Post)
