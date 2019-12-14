from django.urls import include, path
from rest_framework import routers
from api.views import CommentViewSet, LikeViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)


app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]