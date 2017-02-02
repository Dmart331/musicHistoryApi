from rest_framework import serializers
from musicHistoryApi.models import *
from django.contrib.auth import models
from django.contrib.auth.models import User


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: ProductCategory
    """

    class Meta:
        model = Artist
        fields = ('id', 'url', 'name',)


class SongSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: ProductOrder
    """

    class Meta:
        model = Song
        fields = ('id', 'url', 'name', 'artist_name', 'genre')


class AlbumSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: Order
    Added ProductOorderSerializer to make nested serializers in the
        OrderSerializer
    """
    class Meta:
        model = Album
        fields = ('id', 'url','name',
            'song_name','genre')
        depth = 0


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: User
    If user is not staff, This UserSerializer will be picked up on the
        ViewSet
    """

    class Meta:
        model = Genre
        fields = ('id', 'url', 'name',)
        depth = 0

