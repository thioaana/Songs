# songsAPI/views.py

from django.shortcuts import render
from rest_framework import generics

from songs.models import Song
from .serializers import SongSerializer


# Create your views here.
class SongsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
    
    def perform_create(self, serializer):
        print(serializer)
        title = serializer.validated_data.get('title')
        artist = serializer.validated_data.get('artist') or None
        if artist is None:
            artist = 'Unknown'
        serializer.save()
        
        
    
class SongsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
    
    