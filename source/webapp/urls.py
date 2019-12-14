from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from webapp.views import IndexView, ImageView, ImageCreateView, ImageEditView, ImageDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('image/<int:pk>', ImageView.as_view(), name='image_detail'),
    path('image/create/',ImageCreateView.as_view(), name='image_create'),
    path('image/<int:pk>/edit/', ImageEditView.as_view(), name='image_edit'),
    path('image/delete/<int:pk>/', ImageDeleteView.as_view(), name='image_delete'),
    path('webapp/login/', LoginView.as_view(), name='login'),
    path('webapp/logout/', LogoutView.as_view(), name='logout'),

]