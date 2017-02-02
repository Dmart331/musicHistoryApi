from musicHistoryApi.models import *
from musicHistoryApi.serializers import *
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from rest_framework import renderers 




class ArtistViewSet(viewsets.ModelViewSet):
	"""
	The User View provides the `list`, `create`, and `retrieve` actions.
	Please click on a specific User's url for the `update` and `destroy` actions.
	If user is not a staff, This will be the UserView
	"""
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer	





class SongViewSet(viewsets.ModelViewSet):
	"""
	The Order View provides the `list`, `create`, and `retrieve` actions.
	Please click on a specific Order's url for the `update` and `destroy` actions.
	"""
	queryset = Song.objects.all()
	serializer_class = SongSerializer




class AlbumViewSet(viewsets.ModelViewSet):
	"""
	The Payment Method View provides the `list`, `create`, and `retrieve` actions.
	Please click on a specific Method's url for the `update` and `destroy` actions.
	"""
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer


class GenreViewSet(viewsets.ModelViewSet):
	"""
	The Product Category View provides the `list`, `create`, and `retrieve` actions.
	Please click on a specific Category's url for the `update` and `destroy` actions.
	"""
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer

