from django.contrib import admin
from .models import BlogPost,SubBlogPost,Comment
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(SubBlogPost)
admin.site.register(Comment)
