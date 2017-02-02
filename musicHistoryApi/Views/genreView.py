from rest_framework import viewsets
from musicHistoryApi.Serializers import *
from musicHistoryApi.Models import *

class GenreViewSet(viewsets.ModelViewSet):

	queryset = genre.Genre.objects.all()
	serializer_class = genreSerializer.GenreSerializer