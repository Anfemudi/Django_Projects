from django.urls import path , include
from photos import api as api_photos
from rest_framework.routers import DefaultRouter

##API Routers
##trailing_slash its when you whant and slash at the end of the url
router=DefaultRouter(trailing_slash=True)
router.register('photos',api_photos.PhotoViewSet)

##from users import views as User_view
urlpatterns = [
    ##Photos and Users API URLS with router

    path('1.0/',include(router.urls)),  # includes API URLS
    
]
