from rest_framework import serializers
from authentication.models import User
from .models import Experience, Project
import uuid

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['company_name','designation', 'start_date','end_date', 'user' ]


class ProjectSerializer():
    class Meta:
        model = Project
        fields = ['project_title','description', 'start_date','end_date', 'user']


