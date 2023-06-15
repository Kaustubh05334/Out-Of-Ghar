from django.urls import path
from .views import blogPostPage,preview_blog,blog_details,delete_blog,search,like_blog
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('postblog',blogPostPage,name='blog_post_page'),
    path('edit/<int:blog_id>/',preview_blog,name='blog_preview'),
    path('view/<int:blog_id>/',blog_details,name='blog_details'),
    path('blog/<int:blog_id>/delete/', delete_blog, name='delete_blog'),
    path('search/', search, name='search'),
    path('like/<int:blog_id>/', like_blog, name='like_blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)