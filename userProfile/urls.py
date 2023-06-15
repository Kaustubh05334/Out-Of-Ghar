from django.urls import path
from .views import profile_page,profile_view,reject_blog_page,all_notification
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/',profile_page,name='profile_page'),
    path('profile/view/', profile_view, name='profile_view'),
    path('reject/<int:ad_id>/', reject_blog_page, name='rejected_notf'),
    path('all_notf',all_notification,name='all_notf')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
