from django.db import models
from . import album, artist, genre

class Song(models.Model):
    """
    Song holds all info. Artist name, album the song belongs to and the genre
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, default='')
    artist_name = models.ForeignKey(artist.Artist, on_delete=models.CASCADE)
    album_name = models.ForeignKey(album.Album, on_delete=models.CASCADE)
    genre = models.ForeignKey(genre.Genre,  on_delete=models.CASCADE)


    def __str__(self):
        
        return str(self.id)

    class Meta:
        
        ordering = ('name',)