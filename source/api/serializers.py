from webapp.models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    create_comment = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    author_comment = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'photo', 'author_comment', 'create_comment')     #прописываю поля, которые есть у модели Comment

    def create(self, request):
        print('test ')
        user = self.context['request'].user
        photo = request['photo']
        text = request['text']
        comment = Comment.objects.create(author_comment=user, photo=photo, text=text)
        return comment


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    photo = serializers.ImageField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'photo')