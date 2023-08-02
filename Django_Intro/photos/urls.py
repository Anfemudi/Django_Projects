from django.urls import path 
from photos import views
from django.contrib.auth.decorators import login_required 




##from users import views as User_view
urlpatterns = [

    ##photos urls
    path('', views.HomeView.as_view(),name='photos_home'),
    path('photos/', views.PhotoListView.as_view(),name='photos_list'),
    path('photos/<int:pk>/',views.DetailView.as_view(),name='photos_detail'),
    path('photos/new/', views.CreateView.as_view() ,name='create_photo'),
    path('my-photos/', login_required(views.UserPhotosView.as_view()) ,name='user_photos'),
    
]

