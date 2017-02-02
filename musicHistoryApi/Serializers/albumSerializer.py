from rest_framework import serializers
from musicHistoryApi.Models import *

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = album.Album
        fields = ('id', 'url','name',
                'genre')
        depth = 0
