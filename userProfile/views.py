from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from accounts.models import Profile
from blog.models import BlogPost
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def profile_page(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        instagram_link = request.POST.get('instagram_link')
        # profile_image = request.FILES.get('profile_image')
        profile_image = request.FILES.get('profile_image')
        facebook_link = request.POST.get('facebook_link')
        user_bio = request.POST.get('user_bio')
        mobile_number = request.POST.get('mobile_number')

        
        if profile:
            profile.instagram_link = instagram_link
            if profile_image:
                profile.profile_image = profile_image
            profile.facebook_link = facebook_link
            profile.user_bio = user_bio
            profile.mobile_number = mobile_number
            profile.save()

        messages.success(request, 'Profile updated successfully.')
        return redirect('profile_view')

    return render(request, 'userProfile/profile_list.html', {'profile': profile})

def profile_view(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    blog_posts = BlogPost.objects.filter(user=user,status=1)
    return render(request, 'userProfile/profile.html', {'blog_posts': blog_posts,'profile': profile})