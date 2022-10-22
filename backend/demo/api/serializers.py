from rest_framework import serializers
from demo.models import Project
from accounts.api.serializers import UserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=Project
        fields="__all__"
        depth=1