from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    """

    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        """
        Method to create a string representing a Product sold by a
            particular User(seller) of Bangazon API
        """
        return self.name

    class Meta:
        """
        Class defining metadata for results of querying the Product table of
            Bangazon API
        """
        ordering = ('name',)

class Album(models.Model):
    """
    """
    name = models.CharField(max_length=50, default='')
    genre = models.ForeignKey("Genre",  on_delete=models.CASCADE)

    def __str__(self):
        """
        Method to create a string representing a Product Category of
            Bangazon API
        """
        return self.name

    class Meta:
        """
        Class defining metadata for results of querying the Product Category
            table of Bangazon API
        """
        ordering = ('name',)

class Song(models.Model):
    """
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, default='')
    artist_name = models.ForeignKey("Artist", on_delete=models.CASCADE)
    album_name = models.ForeignKey("Album", on_delete=models.CASCADE)
    genre = models.ForeignKey("Genre",  on_delete=models.CASCADE)


    def __str__(self):
        """
        Method to create a string representing a Order of a particular User
            (customer) of Bangazon API
        """
        return str(self.id)

    class Meta:
        """
        Class defining metadata for results of querying the Order table of
            Bangazon API
        """
        ordering = ('name',)

class Artist(models.Model):
  
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        """
        Method to create a string representing a Payment Method of a
            particular User(customer) of Bangazon API

        Returns a string representaion of the payment method's name field
        """
        return self.name

    class Meta:
        """
        Class defining metadata for results of querying the Payment Method
            table of Bangazon API
        """
        ordering = ('name',)










