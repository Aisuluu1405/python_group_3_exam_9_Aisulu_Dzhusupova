from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'', вьюшка)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    # path('login/', name='api_token_auth'),
    # path('logout/',  name='api_token_delete')

]