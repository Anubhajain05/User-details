from django.shortcuts import render
from rest_framework import generics, status, request
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .serializers import ExperienceSerializer, ProjectSerializer
from rest_framework.response import Response
#from authentication.models import User
from .models import Experience, Project
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions





class UserExperienceView(generics.GenericAPIView):
    serializer_class = ExperienceSerializer


    def get(self, request):
        pk = request.user.pk
        experience = Experience.objects.filter(user=pk)
        serializer = ExperienceSerializer(experience, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        try:
            experience = self.request.data
            serializer = self.serializer_class(data={**experience, **{"user": request.user.pk}})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': True,
                                 'message': 'experience details added successfully',
                                 'data': serializer.data})
        except ValidationError:
            return Response(serializer.errors)



class UserExperienceDetail(APIView):
    serializer_class= ExperienceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_obj(self,request,id):
        try:
            return Experience.objects.get_obj(id=id)
        except Experience.DoesNotExist:
            raise ValidationError("No experience found with this id")

    def get(self,requests, id):
        experience = self.get(requests, id = id)
        serializer = ExperienceSerializer(experience, data= request.data)
        return Response({
            'status': True,
            'message': "user experience details ",
            'data': serializer.data
        })


    def put(self,request, id):
        experience = self.get(request, id = id)
        serializer = self.serializer_class(isinstance= experience,data={**self.request.data, **{"user": request.user.pk}})

        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response({'status': True,
                                 'message': " experience updated successfully",
                                 'data': serializer.data})
        return Response(serializer.errors)



    def delete(self, request, id):
        experience = self.get_obj(request, id=id)
        experience.delete()
        return Response({"message": "user details does not exist"})



class UserProjectView(APIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get(self, request):
        pk = request.user.pk
        projects = Project.objects.filter(user=pk)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data={**self.request.data, **{"user": request.user.pk}})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': True,
                                 'message': 'project details added successfully',
                                 'data': serializer.data})
        except ValidationError:
            return Response(serializer.errors)
        # except Exception as e:
        #     return Response(str(e))


class UserProjectDetails(APIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_obj(self, request, id):
        try:
            return Project.objects.get(id=id)
        except Project.DoesNotExist:
            raise ValidationError("No project found with this id")

    def get(self, request, id):
        project = self.get_obj(request, id=id)
        serializer = ProjectSerializer(project)
        return Response({
            'status': True,
            'message': "user project details",
            'data': serializer.data
        })

    def put(self, request, id):
        try:
            project = self.get_obj(request, id=id)
            serializer = self.serializer_class(instance=project,
                                               data={**self.request.data, **{"user": request.user.pk}})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': True,
                                 'message': " project updated successfully",
                                 'data': serializer.data})
        except ValidationError:
            return Response(serializer.errors)

    def delete(self, request, id):
        project = self.get_obj(request, id=id)
        project.delete()
        return Response({"message": "user details does not exist"})