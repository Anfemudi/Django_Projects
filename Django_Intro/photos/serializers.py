from rest_framework import serializers
from photos.models import Photo

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Photo

        ## this is because it is taking the authenticated user as owner so it wont make sence to use it as param .
        read_only_fields=('owner',)

class PhotoListSerializer(PhotoSerializer):
    ## this is because Meta is not inhering the model class which is in the Meta class from Photo Serializer
    class Meta(PhotoSerializer.Meta):
        fields=('id','name','url')
        
        
        
        

