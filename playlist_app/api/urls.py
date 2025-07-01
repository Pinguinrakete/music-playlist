from django.urls import path
from .views import playlist_view, playlist_single_view, RegistrationView, LoginView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('endpoint/', playlist_view),
    path('endpoint/<int:pk>/', playlist_single_view, name='endpoint-detail'),
    path('registration/<int:pk>/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login')
]