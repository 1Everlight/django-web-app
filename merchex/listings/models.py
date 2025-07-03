from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


#creation of method Band() for group object creating
class Band(models.Model):
    
    def __str__(self):
        return f'{self.name}'
    
    class Genre(models.TextChoices):
        Hip_Hop = 'HH'
        SYNTH_HO = 'SH'
        ALTERNATIVE_ROCK = 'AR'
        
    
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices = Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1980), MaxValueValidator(2025)])
    active = models.fields.BooleanField(default = True)
    offical_page = models.fields.URLField(null=True, blank=True)
    
    
    
class Listing(models.Model):
    
    
    def __str__(self):
        return f'{self.title}'
    
    
    class Types(models.TextChoices):
        disques = 'Records'
        vetements = 'Clothing'
        affiches = 'Posters'
        divers = 'Miscellaneous'
    
    
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=500)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2025)],null=True, blank=True)
    types = models.fields.CharField(choices = Types.choices, max_length=50)
    band = models.ForeignKey(Band,null=True,on_delete=models.SET_NULL)