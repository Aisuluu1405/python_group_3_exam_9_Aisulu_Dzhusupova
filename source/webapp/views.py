from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
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


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    template_name = 'create.html'
    form_class = PhotoForm
    # permission_required = 'webapp.add_services'
    # permission_denied_message = "Доступ запрещен!"

    def get_success_url(self):
        return reverse('webapp:image_detail', kwargs={'pk': self.object.pk})


class ImageEditView(PermissionRequiredMixin, UpdateView):
    template_name = 'edit.html'
    model = Image
    form_class = PhotoForm
    context_object_name = 'image'
    permission_required = 'webapp.change_image'


    # def form_valid(self, form):
    #     self.object.create(author=self.request.user, **form.cleaned_data)
    #     return redirect('webapp:index')
    #
    def get_success_url(self):
        return reverse('webapp:image_detail', kwargs={'pk': self.object.pk})


class ImageDeleteView(PermissionRequiredMixin, DeleteView):
    model = Image
    template_name = 'delete.html'
    context_object_name = 'image'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_image'


