from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Image, Like
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

@method_decorator(ensure_csrf_cookie, name='dispatch')               # при запросах чтобы токен приходил целиком
class IndexView(ListView):
    model = Image
    template_name = 'index.html'
    context_object_name = 'images_list'
    ordering = ['-create']

@method_decorator(ensure_csrf_cookie, name='dispatch')              # при запросах страниц токен должен приходить целиком
class ImageView(DetailView):
    model = Image
    template_name = 'detail.html'
    context_object_name = 'image'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            try:
                Like.objects.get(author= self.request.user, photo = self.object)  #self.object- текущий объект
                context['liked']=True
            except Like.DoesNotExist:
                context['liked'] = False
        return context


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    template_name = 'create.html'
    form_class = PhotoForm

    def form_valid(self, form):
        self.object = self.model.objects.create(author=self.request.user, **form.cleaned_data)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:image_detail', kwargs={'pk': self.object.pk})


class ImageEditView(PermissionRequiredMixin, UpdateView):
    template_name = 'edit.html'
    model = Image
    form_class = PhotoForm
    context_object_name = 'image'
    permission_required = 'webapp.change_image'

    def get_success_url(self):
        return reverse('webapp:image_detail', kwargs={'pk': self.object.pk})


class ImageDeleteView(PermissionRequiredMixin, DeleteView):
    model = Image
    template_name = 'delete.html'
    context_object_name = 'image'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_image'


