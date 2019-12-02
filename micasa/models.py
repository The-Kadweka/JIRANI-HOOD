from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Location(models.Model):
    locations = (
        ('Nairobi', 'Nairobi'),
        ('Kiambu', 'Kiambu'),
        ('Eastlands', 'Eastlands'),
        ('Machakos', 'Machakos'),
        ('Nakuru', 'Nakuru'),
        ('London', 'London'),
        ('Paris', 'Paris'),
        ('Vienna', 'Vienna'),
        ('Sydney', 'Sydney'),
        ('Stockholm', 'Stockholm'),
        ('Tokyo', 'Tokyo'),
        ('Hongkong', 'Hongkong'),        
        ('Thika', 'Thika'),
        ('Dubai', 'Dubai'),
        ('New York', 'New York'),
        ('Los Angeles', 'Los Angeles'),
        ('Venice', 'Venice'),
        ('Cairo', 'Cairo'),
        ('Himalayas', 'Himalyas'),
        ('Antarctica', 'Antarctica'),        
        ('Arctic', 'Arctic'), 
        ('Fantasy', 'Fantasy'),  
        ('Sparta', 'Sparta'),
        ('Mombasa', 'Mombasa'),        
    )
    name = models.CharField(max_length=65, choices=locations)



    def save_loc(self):
        self.save()

    def delete_loc(self):
        self.delete()


    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Hood(models.Model):
    name = models.CharField(max_length=50)
    image = ImageField()
    occupants = models.CharField(max_length=50)
    location = models.ForeignKey(Location)
    created_on = models.DateTimeField(auto_now_add=True, null=True)




    class Meta:
        ordering = ['-pk']

    def save_hood(self):
        self.save()


    def delete_hood(self):
        self.delete()


    @classmethod
    def search_hood(cls, search_term):
        hood = Hood.objects.filter(name__icontains=search_term)
        return hood


    def __str__(self):
        return self.name





class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'profile/',blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.CharField(max_length = 255,null = True)
    full_name = models.CharField(max_length=255, null=True)
    hood = models.ForeignKey(Hood,null=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()



    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Business(models.Model):
    business_name = models.CharField(max_length=50)
    owner = models.ForeignKey(User)
    hood = models.ForeignKey(Hood)
    address = models.CharField(max_length=50)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.business_name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_by_category(cls, category):
        biz = cls.objects.filter(category__name__icontains=category)
        return biz

    @classmethod
    def search_business(cls, search_term):
        business = Business.objects.filter(business_name__icontains=search_term)
        return business


    @classmethod
    def get_business(cls, id):
        business = Business.objects.filter(hood__pk=id)
        return business



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    hood = models.ForeignKey(Hood, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=65)

    def __str__(self):
        return self.title

    @classmethod
    def get_post(cls, id):
        post = Post.objects.filter(hood__pk=id)
        return post




