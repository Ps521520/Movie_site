from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField()
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    movie_choice = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)

class Movie_Data(models.Model):
    SERIAL_NO=models.IntegerField()
    MOVIES_NAME=models.CharField(max_length=100)
    MOVIES_TYPE=models.CharField(max_length=100)
    MOVIES_LANGUAGE = models.CharField(max_length=100)
    MOVIES_REGION= models.CharField(max_length=100)
    RATINGS=models.DecimalField(decimal_places=2,max_digits=4)
    LINKS = models.CharField(max_length=500)


