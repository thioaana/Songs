# songs /models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    
    def get_absolute_url(self):
        return reverse('song_detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.title} - {self.artist}'