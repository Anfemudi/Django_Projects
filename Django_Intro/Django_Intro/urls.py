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
##from users import views as User_view
urlpatterns = [
    path('admin/', admin.site.urls),

    ##photos urls
    path('home/', views.home,name='photos_home'),
    path('photos/<int:pk>/',views.detail,name='photos_detail'),

    ##users URL
    path('login/',app_views.login,name='users_login'),
    path('logout/',app_views.logout,name='users_logout'),
]

