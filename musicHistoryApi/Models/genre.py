from django.db import models

class Genre(models.Model):
    """
    Genre will only hold name
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')

    def __str__(self):
       
        return self.name

    class Meta:
        
        ordering = ('name',)