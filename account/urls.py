from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.UserView.as_view(), name='user-detail'),
    path('api-token/', obtain_auth_token, name='api_token_auth'),
]
