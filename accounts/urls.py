from django.urls import path,include
from .views import login_page,register_user,logout_page
urlpatterns = [
    
    path('login/',login_page,name='login_page'),
    path('register/',register_user,name='register_user'),
    path('logout/',logout_page,name='logout_page'),

]