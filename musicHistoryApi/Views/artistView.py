from rest_framework import viewsets
from musicHistoryApi.Serializers import *
from musicHistoryApi.Models import *


class ArtistViewSet(viewsets.ModelViewSet):
	
	queryset = artist.Artist.objects.all()
	serializer_class = artistSerializer.ArtistSerializer	