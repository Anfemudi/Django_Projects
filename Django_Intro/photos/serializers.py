from rest_framework import serializers
from photos.models import Photo

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Photo

