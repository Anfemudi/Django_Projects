from django.contrib.auth.models import User
from flickr_user.serializers import userSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from flickr_user.permissions import UserPermissions

class UserListAPI(APIView):


    permission_classes=(UserPermissions,)

    def get(self,request):
        self.check_permissions(request)
        users=User.objects.all()
        ##Paging of queryset
        paginator=PageNumberPagination()
        paginator.paginate_queryset(users,request)
        serializer=userSerializer(users,many=True)
        serialized_users=serializer.data #dictionaries' list
        ##return pagination anwer
        return paginator.get_paginated_response(serialized_users)
    
    def post(self,request):
        ##rest framework takes post and convert it to data so we replace request.POST with request.data
        ## VALIDATES IF USER HAS PERMISSIONS TO DO THE ACTION
        self.check_permissions(request)
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

