from django.test import TestCase
from .models import Hood, Profile, Business, Post
from django.contrib.auth.models import User

# Create your tests here.
class HoodTestClass(TestCase):
    def setUp(self):
        self.my_hood =Hood(name='wendani',location='kiambu',occupants=5)
        self.my_hood.save()

    def tearDown(self):
        Hood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.my_hood,Hood))

    def test_save_hood(self):
        self.my_hood.save_hood()
        hood = Hood.objects.all()
        self.assertTrue(len(Hood)>0)
        

class profileTestCLass(TestCase):
    '''
    setup self instance of profile
    '''

    def setUp(self):
        self.profile = Profile(bio='Lover of life', full_name='Wairimu Maina')

    ''' 
    test instance of profile
    '''

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        bio = Profile.objects.all()
        self.assertTrue(len(bio) > 0)
        
        
class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_user=User(username="nimz",email="nim@me.com")
        self.new_user.save()
        self.my_hood = Hood(name='wendani', location='kiambu', occupants=5)
        self.my_hood.save()
        self.burgers = Business(business_name='nim-burgers',email='nim@me.com',owner=self.new_user,hood=self.my_hood)
        self.burgers.save()

    def tearDown(self):
        User.objects.all().delete()
        Hood.objects.all().delete()
        Business.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.burgers,Business))

    def test_save_business(self):
        self.burgers.create_business()
        business =  Business.objects.all()
        self.assertTrue(len(business)>0)    
        
        
class PostTestClass(TestCase):
    def setUp(self):
        self.new_user = User(username="nimz", email="nim@me.com")
        self.new_user.save()
        self.my_hood = Hood(name='wendani', location='kiambu', occupants=5)
        self.my_hood.save()

        self.new_post=Post(title = 'Robbed',description = 'I was robbed')

    def tearDown(self):
        User.objects.all().delete()
        Hood.objects.all().delete()
        User.objects.all().delete()
        Post.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))                    