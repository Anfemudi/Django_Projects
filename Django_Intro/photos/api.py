from photos.models import Photo
from photos.serializers import PhotoSerializer,PhotoListSerializer
from rest_framework .permissions import IsAuthenticatedOrReadOnly
from photos.views import PhotosQuerySet
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter,OrderingFilter


class PhotoViewSet(PhotosQuerySet,ModelViewSet):
    queryset = Photo.objects.all()
    permission_classes=(IsAuthenticatedOrReadOnly,)

    ## Class that are used to filter the data to show
    filter_backends= (SearchFilter,OrderingFilter)
    ## let it search by Name, Descriptions and owners name for specific data with match the search criteria
    search_fields=('name','description','owner__first_name')
    ##allows to order the data by name and owners name
    ordering_fields = ('name','owner')
    def get_queryset(self):
        return self.get_photos_queryset(self.request)
    
    def get_serializer_class(self):
        if self.action == "list":
            return PhotoListSerializer
        else:
            return PhotoSerializer

    def perform_create(self, serializer):
        """
        assign the photo author to the autenicated user
        
        """
        serializer.save(owner=self.request.user)
