from django.db import models
from . import genre




class Album(models.Model):
    """
    Album will have name and genre
    """
    name = models.CharField(max_length=50, default='')
    genre = models.ForeignKey(genre.Genre,  on_delete=models.CASCADE)

    def __str__(self):
       
        return self.name

    class Meta:
      
        ordering = ('name',)