# songs/urls.py

from django.urls import path

from .views import HomePageView, ListSongsView, SongDetailView, SongEditView, SongDeleteView, SongNewView

urlpatterns = [
    path('',HomePageView.as_view() ,name='home'),
    path('list', ListSongsView.as_view(), name='song_list'),
    path('<int:pk>/', SongDetailView.as_view(), name='song_detail'),
    path('<int:pk>/edit/',SongEditView.as_view() , name='song_edit'),
    path('<int:pk>/delete/', SongDeleteView.as_view(), name='song_delete'),
    path('new/', SongNewView.as_view(), name='song_new'),
]