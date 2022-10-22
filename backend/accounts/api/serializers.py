from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.models import SocialMedia

User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        exclude=('password',)


class SocialMediaSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=SocialMedia
        fields="__all__"
