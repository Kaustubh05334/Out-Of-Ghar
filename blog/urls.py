from django.urls import path
from .views import blogPostPage,preview_blog,blog_details,delete_blog,search,delete_comment,report_blog,liked
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('postblog',blogPostPage,name='blog_post_page'),
    path('edit/<int:blog_id>/',preview_blog,name='blog_preview'),
    path('view/<int:blog_id>/',blog_details,name='blog_details'),
    path('blog/delete/<int:blog_id>', delete_blog, name='delete_blog'),
    path('search/', search, name='search'),
    path('delete_comment/<int:blog_id>/<int:comment_id>/',delete_comment, name='delete_comment'),
    path('report/<int:blog_id>/', report_blog, name='report_blog'),
    path('like/<int:blog_id>/', liked, name='liked'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)