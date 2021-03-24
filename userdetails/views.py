from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView

from .serializers import ExperienceSerializer, ProjectSerializer
from rest_framework.response import Response
from authentication.models import User
from .models import Experience

# Create your views here.
class UserProjectView(generics.GenericAPIView):
    serializer_class = ProjectSerializer

    def post(self, reqquest):
        projects = self.request.data
        serializer = self.serializer_class(data = projects)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({'status': True, 'message': 'project details added successfully', 'data':serializer.data})



class UserExperienceView(generics.GenericAPIView):
    serializer_class = ExperienceSerializer


    def post(self,request):
        projects = self.request.data
        serializer = self.serializer_class(data = projects)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response({'status': True, 'message': 'experience deatils added successfully', 'data': serializer.data})


class UserExperienceDetail(APIView):

    def get(self,requests, pk, format = None):
        experience = self.get(pk)
        serializer = ExperienceSerializer(experience)
        return Response(serializer.data)


    def put(self, request, pk, format = None):
        experience = self.get()