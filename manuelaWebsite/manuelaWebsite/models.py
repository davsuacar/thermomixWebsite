from django.db import models

def upload_to(filename):
    return 'images/recipes/%s' % (filename)

# Create your models here.

class MeetingRequest(models.Model):
    client_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=200)
    date = models.DateTimeField()
    
    def __unicode__(self):
        return self.client_name
    
    
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ForeignKey('manuelaWebsite.Ingredient')
    steps = models.ForeignKey('manuelaWebsite.Step')
    date = models.DateTimeField()
    thumbnail = models.ImageField(upload_to=upload_to)
    
    def __unicode__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unit_measure = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name
    
class Step(models.Model):
    description = models.TextField(max_length=200)
    position = models.IntegerField()
    
    def __unicode__(self):
        return self.description    