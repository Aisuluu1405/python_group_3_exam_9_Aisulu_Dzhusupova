from django.urls import include, path
from rest_framework import routers
from api.views import CommentViewSet, LikeView, DislikeView

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet)



app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('like/<int:pk>/', LikeView.as_view(), name='like_image'),
    path('dislike/<int:pk>/', DislikeView.as_view(), name='dislike_image')
]