from django.contrib.auth.models import User
from django.db import models

class Image(models.Model):
    photo = models.ImageField(upload_to='user_photo', verbose_name='Фотография')
    note = models.CharField(max_length=100, verbose_name='Подпись')
    like = models.IntegerField(default=0, verbose_name='Лайк')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(User, related_name='author_image', on_delete=models.CASCADE, default=None, verbose_name='Автор фото')

    def __str__(self):
        return self.note

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Comment(models.Model):
    text = models.TextField(max_length=3000, verbose_name='Комментарий')
    photo = models.ForeignKey('webapp.Image', related_name='comments', on_delete=models.CASCADE, verbose_name='Фотография')
    author_comment = models.ForeignKey(User, related_name='author_comment', on_delete=models.CASCADE, default=None, verbose_name='Автор комментария')
    create_comment = models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Like(models.Model):
    user = models.ForeignKey(User, related_name='like_user', on_delete=models.CASCADE, verbose_name='Пользователь')
    photo = models.ForeignKey('webapp.Image', related_name='like_photo', on_delete=models.CASCADE, verbose_name='Фото')



