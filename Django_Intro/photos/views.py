from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from photos.models import Photo, PUBLIC
from photos.forms import PhotoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required 
from django.views.generic import View , ListView
from django.utils.decorators import method_decorator
from django.db.models import Q





# Create your views here.


class PhotosQuerySet(object):

    
    def get_photos_queryset(self,request):

        if not request.user.is_authenticated:
            photos=Photo.objects.filter(visibility=PUBLIC)
        elif request.user.is_superuser:
            photos=Photo.objects.all()
        else:
            ## Q class helps create an or at bit level . so i can have either one of the  conditions to show the photos
            photos=Photo.objects.filter(Q(owner=request.user)|Q(visibility=PUBLIC))

        return photos





# as a controler it has a Request parameter

class HomeView(View):
    def get(self,request):

   
        ## TRAER el nombre de TODAS LAS FOTOS A HOME
        ## the order_by is like de SQL statement, the - sign before the field is the order by Desc in sql
        ## the all method is equivalent to select *

        ## photos= Photo.objects.all().order_by('-created_at')


        ##filter is equivalent to Where squl statement
        ## if i used , inside the filter is equivalent to the AND in sql
        photos= Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
        
        context= {
            'photos_list' : photos[:5]
        }
        return render(request,"photos/home.html",context)
    


class DetailView(View,PhotosQuerySet):
    

    def get(self,request,pk):


         ###Load the page of the photo detail
         ###:param request: HttpRequest 
         ###:param pk: id of the photo
         ###:return:HttpResponse 

        ### to avoid errors if photos does not exist
        ###try:
            ### pk attribute is a django default to search primary key
           ### possible_photos = Photo.objects.filter(pk=pk)
        ####except Photo.DoesNotExist:
            ###photo=None
        ###except Photo.MultipleObjects:
            ###photo=None


        ## this case / except can also be replaced by :

        ## the selecte_related brings the owner field in the same query , and not in separete queries
        ## Select_related and prefetch_related helps optimize django queries
        possible_photos = self.get_photos_queryset(request).filter(pk=pk).select_related('owner')
        photo = possible_photos[0] if len(possible_photos) >=1 else None

        if photo is not None:
            # Load detail template
            context= {

                'photo': photo
            }

            return render(request, 'photos/detail.html',context)

        else:
            return HttpResponseNotFound('The Photo Does not Exist') # 404 not found

## decorator to allow just authenticated users to accss this url


class AuthenticatedView(View):

    def get(self,request):
        if request.user.is_authenticated:
            return super(AuthenticatedView,self).get(request)



class CreateView(View):

    ## the login required decorator is just for functions not for methods , that is why it needs the method decorator to work
    @method_decorator(login_required())
    def get(self,request):
        """ shows a form to create a photo and creates it if the call is post 
        "param request: HttpRequest
        :return: HttpResponse """


        success_message=''
        form=PhotoForm()
        context={
            'form':form,
            'success_message': success_message
        }
        return render(request,'photos/new_photo.html',context)

    @method_decorator(login_required())
    def post(self,request):
        """ shows a form to create a photo and creates it if the call is post 
        "param request: HttpRequest
        :return: HttpResponse """
        success_message=''
        photo_with_owner=Photo()
        photo_with_owner.owner=request.user
        form = PhotoForm(request.POST,instance=photo_with_owner)
        if form.is_valid():
            new_photo= form.save() # save the object in DB and then return it
            form=PhotoForm()
            success_message='Photo Succesfully saved'
            success_message +='<a href="'+reverse('photos_detail',args=[new_photo.pk])+'">'
            success_message+='See Photo'
            success_message+='</a>'
        context={
            'form':form,
            'success_message': success_message
        }
        return render(request,'photos/new_photo.html',context)


class PhotoListView(View,PhotosQuerySet):
    def get(self,request):
        ### returns:
        ###- all public photos if user not authenticated
        ###- all authenticated user's photos and public photos 
        ###- all photos if user is super admin user
        
        
        context = {
            'photos': self.get_photos_queryset(request)
            }
        
        return render(request,'photos/photos_list.html',context)
            
class UserPhotosView(ListView):
    model= Photo
    template_name='photos/user_photos.html'

    def get_queryset(self):
        queryset=super(UserPhotosView,self).get_queryset()
        return queryset.filter(owner=self.request.user)
