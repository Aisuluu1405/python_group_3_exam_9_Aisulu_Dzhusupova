from django.shortcuts import render
from django.views.generic import ListView, DetailView

from webapp.models import Image


class IndexView(ListView):
    model = Image
    template_name = 'index.html'
    context_object_name = 'images_list'
    ordering = ['-create']


class ImageView(DetailView):
    model = Image
    template_name = 'detail.html'
    context_object_name = 'image'


