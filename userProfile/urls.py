from django.urls import path
from .views import profile_page,profile_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/',profile_page,name='profile_page'),
    path('profile/view/', profile_view, name='profile_view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
