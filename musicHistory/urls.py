from django.conf.urls import url, include
from rest_framework import routers
from musicHistoryApi.Views import *

# Create a router, using DefaultRouter
# Register each ViewSet with it.
router = routers.DefaultRouter()
router.register(r'artists', artistView.ArtistViewSet)
router.register(r'songs', songView.SongViewSet)
router.register(r'albums', albumView.AlbumViewSet)
router.register(r'genres', genreView.GenreViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

