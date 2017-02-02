from django.conf.urls import url, include
from musicHistoryApi import views
from rest_framework.routers import DefaultRouter
from django.contrib import admin

# Create a router, using DefaultRouter
# Register each ViewSet with it.
router = DefaultRouter()
router.register(r'artists', views.ArtistViewSet)
router.register(r'songs', views.SongViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'genres', views.GenreViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

