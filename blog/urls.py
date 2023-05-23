from django.urls import path
from .views import blogPostPage
urlpatterns = [
    path('postblog',blogPostPage,name='blog_post_page'),
]