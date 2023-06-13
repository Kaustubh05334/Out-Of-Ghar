from django.urls import path
from .views import blogPostPage,preview_blog,blog_details,delete_blog,search
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('postblog',blogPostPage,name='blog_post_page'),
    path('edit/<int:blog_id>/',preview_blog,name='blog_preview'),
    path('view/<int:blog_id>/',blog_details,name='blog_details'),
    path('blog/<int:blog_id>/delete/', delete_blog, name='delete_blog'),
    path('search/', search, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)