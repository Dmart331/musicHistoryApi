from rest_framework import viewsets
from musicHistoryApi.Serializers import *
from musicHistoryApi.Models import *


class AlbumViewSet(viewsets.ModelViewSet):
	
	queryset = album.Album.objects.all()
	serializer_class = albumSerializer.AlbumSerializer