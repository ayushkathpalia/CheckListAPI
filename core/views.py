from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import CheckList,CheckListItem
from core.serializers import CheckListSerializer,CheckListItemSerializer
from rest_framework import status
# Create your views here.


class ChecklistsAPIView(APIView):
    serializer_class = CheckListSerializer
    def get(self,request,format = None): #shows all the data in DB
        data = CheckList.objects.all()
        serializer = self.serializer_class(data,many=True)
        serialized_data = serializer.data
        return Response(serialized_data,status=status.HTTP_200_OK) 

    def post(self,request,format=None):  #insertion of data in DB
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data    
            return Response(serialized_data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)           


class CheckListAPIView(APIView):
    serializer_class = CheckListSerializer

    def get_object(self,pk):   #function to check if data exists
        try:
            return CheckList.objects.get(pk=pk)
        except CheckList.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):  #function to get data acc to primary key/id
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data
        return Response(serialized_data,status.HTTP_201_CREATED)

    def put(self,request,pk,format=None):
        checklist = self.get_object(pk)
        serializer = self.serializer_class(checklist,data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data,status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        checklist = self.get_object(pk)
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CheckListItemCreateAPIView(APIView):
    serializer_class = CheckListItemSerializer
    def post(self,request,format=None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data    
            return Response(serialized_data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)           


class CheckListItemAPIView(APIView):
    serializer_class = CheckListSerializer
    
    def get_object(self,pk):   #function to check if data exists
        try:
            return CheckListItem.objects.get(pk=pk)
        except CheckListItem.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):  #function to get data acc to primary key/id
        checklist_item = self.get_object(pk)
        serializer = self.serializer_class(checklist_item)
        serialized_data = serializer.data
        return Response(serialized_data,status.HTTP_201_CREATED)

    def put(self,request,pk,format=None):
        checklist = self.get_object(pk)
        serializer = self.serializer_class(checklist,data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data,status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        checklist = self.get_object(pk)
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)