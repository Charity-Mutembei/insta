from django.test import TestCase
from .models import Post, Profile, tags, Follow, Stream

#create tests for the model classes

class PostTestClass(TestCase):
    """
    this test class is one to test the class model Post
    """
    #setupmethod
    def setUp(self):
        self.post_text = Post(post_text= '')

    #testing whether we are being instanciated properly

    def test_instance (self):
        self.assertTrue(isinstance(self.post_text, Post))


    #testing the save method

    def test_save_method(self):
        self.post_text.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts)>0)
