from django.shortcuts import render,redirect,reverse
from .forms import BlogPostForm
from .models import BlogPost,SubBlogPost
from django.contrib.auth.models import User
# Create your views here.
def blogPostPage(request):
    if request.method == 'POST':
        #form = BlogPostForm(request.POST, request.FILES)
            title = request.POST.get('title')
            location = request.POST.get('location')
            content = request.POST.get('content')
            thumbnail =request.FILES.get('thumbnail')
        # Access the subform data
            arrSH,arrSL,arrSI,arrST=[],[],[],[]
            for i in range(10):
                subheading = request.POST.get(f'subheading{i+1}')
                subloc = request.POST.get(f'subloc{i+1}')
                subimage =request.FILES.get(f'subimage{i+1}')
                subtext = request.POST.get(f'subtext{i+1}')
                if subheading or subloc or subimage or subtext:
                    arrSH.append(subheading) 
                    arrSL.append(subloc) 
                    arrSI.append(subimage) 
                    arrST.append(subtext)
            user = request.user
            b1 = BlogPost(user=user,thumbnail=thumbnail,location=location,title=title,content=content)
            b1.save()
            for i in range(len(arrSH)):
                sb=SubBlogPost(subheading=arrSH[i],location=arrSL[i],image=arrSI[i],text=arrST[i])
                sb.save()
                b1.sub_posts.add(sb)
            url = reverse('home')
            return redirect(url)
     
    else:
        return render(request,'blog/blogPost.html',{'form':BlogPostForm})
    
def preview_blog(request,id):
    pass