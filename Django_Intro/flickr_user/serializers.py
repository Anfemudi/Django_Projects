from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError


class userSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField() # as i can send and recieve data , i want id to be read only field
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()

    def create(self,validated_data):
        """
        create an user instance based on the validated-data which are non serialized values
        :param: validated_data: dict with user data
        :return: User Object
        """
        instance = User()
        
        return self.update(instance,validated_data)

    def update(self,instance,validated_data):
        """
        update an user instance based on the validated-data which are non serialized
        :param: validated_data: dict with user data
        :param: instance: user object to be updated
        :return: updated User Object
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password')) ## as the password comes  encrypted by django the set_password method needs to be userd to be able to read it and decrypt it
        instance.save()
        return instance

    def validate_username(self,data):
        """
        Validates if username already exists when creating user
        """
        users=User.objects.filter(username=data)
        if not self.instance and len(users) !=0:
            print("User name exist 1")
            raise serializers.ValidationError("Username allready exists")
        

         ###   if im updating the username and there are existing uses with the new username
        elif self.instance and self.instance.username !=data and len(users) !=0 :
            print("User name exist 2")
            raise serializers.ValidationError("Username allready exists 2")
            
        else:
            return data



