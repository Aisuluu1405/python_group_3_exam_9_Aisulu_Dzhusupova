from django.contrib import admin
from webapp.models import Image, Comment


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


admin.site.register(Image, ImageAdmin)
admin.site.register(Comment, CommentAdmin)

