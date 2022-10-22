from rest_framework import viewsets
from .serializers import ProjectSerializer
from demo.models import Project

class ProjectViewset(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer