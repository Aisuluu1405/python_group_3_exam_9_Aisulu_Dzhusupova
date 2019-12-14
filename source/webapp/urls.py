from django.urls import path
from webapp.views import IndexView, ImageView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('image/<int:pk>', ImageView.as_view(), name='image_detail'),
    # path('image/create', CreateView.as_view(), name='image_create'),
    # path('image/<int:pk>/edit/', EditView.as_view(), name='image_edit'),
    # path('image/delete/<int:pk>/', DeleteView.as_view(), name='image_delete'),

]