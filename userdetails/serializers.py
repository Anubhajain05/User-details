from rest_framework import serializers
from authentication.models import user
from .models import Experience, Project

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['company_name','designation', 'start_date','end_date', 'user_id' ]


class ProjectSerializer():
    class Meta:
        model = Project
        fields = ['project_titel','description', 'start_date','end_date', 'user_id']


