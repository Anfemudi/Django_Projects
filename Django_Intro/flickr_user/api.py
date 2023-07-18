from django.contrib.auth.models import User
from flickr_user.serializers import userSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status

class UserListAPI(APIView):

    def get(self,request):
        users=User.objects.all()
        serializer=userSerializer(users,many=True)
        serialized_users=serializer.data #dictionaries' list
        return Response(serialized_users)
    
    def post(self,request):
        ##rest framework takes post and convert it to data so we replace request.POST with request.data
        serializer= userSerializer(data=request.data)

        if serializer.is_valid():
            new_user=serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserDetailAPI(APIView):

    def get(self,request,pk):
        user=get_object_or_404(User,pk=pk)
        serilizer=userSerializer(user)
        return Response(serilizer.data)

    def put(self,request,pk):
        user=get_object_or_404(User,pk=pk)
        serializer=userSerializer(instance=user, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        user=get_object_or_404(User,pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

