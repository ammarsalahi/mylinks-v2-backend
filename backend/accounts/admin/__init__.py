from django.contrib import admin
from .socialmedia import SocialMediaAdmin
from .user import UserAdmin

from accounts.models import (
    User,
    SocialMedia
)

admin.site.register(User,UserAdmin)
admin.site.register(SocialMedia,SocialMediaAdmin)
