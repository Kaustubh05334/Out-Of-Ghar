
from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class ProfileManager(models.Manager):
    def create_profile(self,user,mobile_number):
        profile = self.create(user=user,mobile_number=mobile_number)
        return profile

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None,related_name='user_profile') 
    mobile_number = models.CharField(max_length=13, unique=True)
    user_bio = models.TextField(max_length=50,blank=True)
    instagram_link = models.URLField(max_length=50,blank=True)
    facebook_link = models.URLField(max_length=50,blank=True)
    profile_image = models.ImageField(upload_to='profile_pic/')

    objects = ProfileManager()

    def __str__(self) -> str:
        return self.user.username
    
    