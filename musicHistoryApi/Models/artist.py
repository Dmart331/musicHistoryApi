from django.db import models

class Artist(models.Model):
    """
    Artist will only hold a name
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        
        return self.name

    class Meta:
        
        ordering = ('name',)
