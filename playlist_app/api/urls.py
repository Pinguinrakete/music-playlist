from django.urls import path
from .views import playlist_view, playlist_single_view

urlpatterns = [
    path('endpoint/', playlist_view),
    path('endpoint/<int:pk>/', playlist_single_view, name='endpoint-detail'),
]