# songsAPI/urls.py

from django.urls import path

from .views import SongsListCreateAPIView

urlpatterns = [
    # path('<int:pk>/', )
    path('list_create/', SongsListCreateAPIView.as_view()),
]