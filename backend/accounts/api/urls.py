from rest_framework import routers

from accounts.api.views import UserViewSet,SocialMediaViewSet

router=routers.DefaultRouter()

router.register('users',UserViewSet)
router.register('socialmedia',SocialMediaViewSet)

urlpatterns=router.urls