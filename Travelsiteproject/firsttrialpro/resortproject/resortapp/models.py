from django.db import models

# Create your models here.
class Place(models.Model):    # Place is the table name in database
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
class Team(models.Model):
    pname = models.CharField(max_length=250)
    pimg = models.ImageField(upload_to='team')
    pdesc = models.TextField()

def __str__(self):
    return self.name
