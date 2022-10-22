from rest_framework import viewsets
from accounts.models import SocialMedia,User
from accounts.api.serializers import UserSerializer,SocialMediaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset=SocialMedia.objects.all()
    serializer_class=SocialMediaSerializer