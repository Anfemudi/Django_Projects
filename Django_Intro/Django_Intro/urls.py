"""Django_Intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from photos import views
from flickr_user import views as app_views
from django.contrib.auth.decorators import login_required 
from flickr_user import api
from photos import api as api_photos
##from users import views as User_view
urlpatterns = [
    path('admin/', admin.site.urls),

    ##photos urls
    path('home/', views.HomeView.as_view(),name='photos_home'),
    path('photos/', views.PhotoListView.as_view(),name='photos_list'),
    path('photos/<int:pk>/',views.DetailView.as_view(),name='photos_detail'),
    path('photos/new/', views.CreateView.as_view() ,name='create_photo'),
    path('my-photos/', login_required(views.UserPhotosView.as_view()) ,name='user_photos'),

    ##hotos API URLS

    path('api/1.0/photos/',api_photos.PhotoListAPI.as_view(),name='photo_list_api'),


    ##users URL
    path('login/',app_views.LoginView.as_view(),name='users_login'),
    path('logout/',app_views.logoutView.as_view(),name='users_logout'),

    #Users API URLs
    path('api/1.0/users/',api.UserListAPI.as_view(),name='user_list_api'),
    path('api/1.0/users/<int:pk>',api.UserDetailAPI.as_view(),name='user_Detail_api'),
]

