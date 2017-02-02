from rest_framework import viewsets
from musicHistoryApi.Serializers import *
from musicHistoryApi.Models import *

class SongViewSet(viewsets.ModelViewSet):
	
	queryset = song.Song.objects.all()
	serializer_class = songSerializer.SongSerializer