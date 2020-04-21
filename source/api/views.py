from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from api.serializers import CommentSerializer

from webapp.models import Comment, Like, Image
from rest_framework.permissions import BasePermission

class IsAuthorPermission(BasePermission):            #Наследуется от BasePermission базовый класс для всех разрешений
                                                     #Разрешение для удаления файла для автора или пользователя с правом 'delete'

    # def has_permission(self, request, view):                 #только для комментария можно использовать
    #     if view.action == 'destroy':
    #         comment = Comment.objects.get(pk=view.kwargs.get('pk'))
    #         return comment.author_comment == request.user or request.user.has_perm('webapp.delete_comment')
    #     return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):                  #это вариант лучше
        if request.method in('DELETE', 'PUT', 'PATCH'):
            return obj.author_comment == request.user or request.user.has_perm('webapp.delete_comment')
        return True






class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAuthorPermission(), ]             #можно удалять только автору или пользвоателю с правом для удаления
        else:
            return super().get_permissions()


class LikeView(APIView):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            photo = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return Response({'error:' 'Фото не найдено'}, status=404)
        try:
            Like.objects.get(photo=photo, author=request.user)                 #гарантировано будет юзер
            return Response({'error': 'Вы уже поставили лайк на это фото'}, status=400)
        except Like.DoesNotExist:
            Like.objects.create(photo=photo, author=request.user)          #если лайка не было , создаем лайк
            photo.like += 1
            photo.save()
            return Response({'id': photo.pk, 'like': photo.like})


class DislikeView(APIView):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            photo = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return Response({'error:' 'Фото не найдено'}, status=404)
        try:
            Like.objects.get(photo=photo, author=request.user).delete()                 #если лайк был поставлпен, меняем на dislike
            photo.like += 1
            photo.save()
            return Response({'id': photo.pk, 'like': photo.like})
        except Like.DoesNotExist:
            return Response({'error': 'Вы еще не ставили лайк на это фото'}, status=400)

