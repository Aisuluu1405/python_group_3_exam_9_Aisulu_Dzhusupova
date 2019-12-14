from webapp.models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    create = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    author_comment = serializers.CharField(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'text', 'photo', 'author_comment', 'create')


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    photo = serializers.ImageField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'photo')