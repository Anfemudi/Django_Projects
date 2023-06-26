from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from photos.models import Photo, PUBLIC

# Create your views here.

# as a controler it has a Request parameter

def home(request):

   
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

    
def detail(request,pk):
     

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
    

    possible_photos = Photo.objects.filter(pk=pk)
    photo = possible_photos[0] if len(possible_photos) >=1 else None

    if photo is not None:
        # Load detail template
        context= {

            'photo': photo
        }

        return render(request, 'photos/detail.html',context)

    else:
        return HttpResponseNotFound('The Photo Does not Exist') # 404 not found


    

