from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from accounts.models import Profile
# Retrieve a user with username "johndoe"

# Create your views here.
def profile_page(request):
    user = request.user
    profile = Profile.objects.filter(username=user.username)
    print(profile)
    return render(request,'userProfile/profile.html',{'user':user,'profile':profile})
