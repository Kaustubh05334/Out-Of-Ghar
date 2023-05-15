from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Retrieve a user with username "johndoe"

# Create your views here.
def profile_page(request):
    user = request.user
    if user.is_authenticated():
        username = user.username
        user = User.objects.get(username=username)
    else:
        return redirect('/')