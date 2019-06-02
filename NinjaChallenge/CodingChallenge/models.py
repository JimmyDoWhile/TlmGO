from django.db import models


# Create your models here.
class SuperNinja(models.Model):
    name = models.CharField(max_length=128, unique=True)
    agility = models.IntegerField()
    strength = models.IntegerField()
    intelligence = models.IntegerField()
    vitality = models.IntegerField()
    katana = models.IntegerField()
    
    def __unicode__(self):
        return self.name
