from django.db import models

# Create your models here.


#creation of method Band() for group object creating
class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    
    
class Listing(models.Model):
    title = models.fields.CharField(max_length=100)