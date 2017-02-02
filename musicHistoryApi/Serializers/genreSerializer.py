from rest_framework import serializers
from musicHistoryApi.Models import *

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    

    class Meta:
        model = genre.Genre
        fields = ('id', 'url', 'name',)
        depth = 0