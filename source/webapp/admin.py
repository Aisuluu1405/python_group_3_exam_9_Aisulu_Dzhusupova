from django.contrib import admin
from webapp.models import Image, Comment, Like


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'note', 'like', 'author', 'create']
    list_filter = ['author']
    exclude = []
    readonly_fields = ['create']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_comment', 'create_comment']
    list_filter = ['author_comment']
    exclude = []
    readonly_fields = ['create_comment']

class LikeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'photo')


admin.site.register(Image, ImageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
