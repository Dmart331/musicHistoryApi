from rest_framework import serializers
from musicHistoryApi.Models import *

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    

    class Meta:
        model = artist.Artist
        fields = ('id', 'url', 'name',)