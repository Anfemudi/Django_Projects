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
from django.urls import path , include
from flickr_user import urls as users_urls, api_urls as users_api_urls
from photos import urls as photos_urls, api_urls as photos_api_urls




##from users import views as User_view
urlpatterns = [
    path('admin/', admin.site.urls),
    ## Users URLs
    path('',include(users_urls)),
    path('api/',include(users_api_urls)),

    ## Photos URLs
    path('',include(photos_urls)),
    path('api/',include(photos_api_urls)),
]


