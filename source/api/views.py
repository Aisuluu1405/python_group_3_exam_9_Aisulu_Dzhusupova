from rest_framework.viewsets import ModelViewSet
from api.serializers import CommentSerializer, LikeSerializer

from webapp.models import Comment, Like


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer




class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

