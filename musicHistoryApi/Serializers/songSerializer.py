from rest_framework import serializers
from musicHistoryApi.Models import *

class SongSerializer(serializers.HyperlinkedModelSerializer):
   

    class Meta:
        model = song.Song
        fields = ('id', 'url', 'name', 'artist_name', 'album_name', 'genre')
