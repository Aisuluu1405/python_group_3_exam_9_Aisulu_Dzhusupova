from django import forms
from webapp.models import Image, Comment


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['create_at']


class ImageCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        exclude =['author_comment', 'create_comment']

