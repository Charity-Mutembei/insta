from django.test import TestCase
from .models import Post, Profile, Tags, Follow, Stream

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

class ProfileTestClass(TestCase):
    """
    a test class of the model class Profile
    """
    #setup method for this class
    def setUp(self):
        self.Bio = Profile(Bio = '')

    #testing whether we are being instanciated in the right way
    def test_instance(self):
        self.assertTrue(isinstance(self.Bio, Profile))

    #testing the save method for this class
    def test_save_method(self):
        self.Bio.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
class TagsTestClass(TestCase):
    """
    a test class of the model class tags
    """
    #setup method for the class tags
    def setUp(self):
        self.name = Tags(name= '')

    #testing whether the instance is properly made
    def test_instance(self):
        self.assertTrue(isinstance(self.name, Tags))

    #testing that the save method is proper for this class
    def test_save_method(self):
        self.name.save_tags()
        tags = Tags.objects.all()
        self.assertTrue(len(tags)>0)
class FollowTestClass(TestCase):
    """
    a test class of the model class tags
    """
    #setup method for the class tags
    def setUp(self):
        self.follower = Follow (follower= '')
