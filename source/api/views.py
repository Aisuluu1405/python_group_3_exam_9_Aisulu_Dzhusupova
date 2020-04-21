from rest_framework.viewsets import ModelViewSet
from api.serializers import CommentSerializer, LikeSerializer

from webapp.models import Comment, Like
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


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

