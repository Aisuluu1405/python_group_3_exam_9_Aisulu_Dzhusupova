from django import forms
from webapp.models import Image


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['create_at', 'author']

