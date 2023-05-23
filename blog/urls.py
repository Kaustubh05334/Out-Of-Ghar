from django.urls import path
from .views import blogPostPage,preview_blog
urlpatterns = [
    path('postblog',blogPostPage,name='blog_post_page'),
    path('<int:blog_id>/',preview_blog,name='blog_details')
]