# songs/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .models import Song

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class ListSongsView(ListView):
    model = Song
    template_name = 'song_list.html'

class SongDetailView(DetailView):
    model = Song
    template_name = 'song_detail.html'
    
class SongEditView(UpdateView):
    model = Song
    fields = ('title', 'artist')
    template_name = 'song_edit.html'
    
class SongDeleteView(DeleteView):
    model = Song
    template_name = 'song_delete.html'
    success_url = reverse_lazy('song_list')
    
class SongNewView(CreateView):
    model = Song
    fields = ('title', 'artist')
    template_name = 'song_new.html'