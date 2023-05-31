from django.shortcuts import render
from blog.models import BlogPost
def homepage(request):
    return render(request, 'homeblog.html')

def blog_approval(request):
    posts = BlogPost.objects.filter(status=0)
    return render(request,'admin/approval.html',{'posts':posts})