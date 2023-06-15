from django.contrib import admin
from .models import BlogPost,SubBlogPost,Comment,AdminComment
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(SubBlogPost)
admin.site.register(Comment)
admin.site.register(AdminComment)
