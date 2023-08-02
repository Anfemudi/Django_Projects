from django.urls import path
from flickr_user import views as app_views


urlpatterns = [

    ##users URL
    path('login/',app_views.LoginView.as_view(),name='users_login'),
    path('logout/',app_views.logoutView.as_view(),name='users_logout'),
    
]

