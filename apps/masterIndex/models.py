from django.db import models
#from locations.models import *
#from resources import *

class MasterIndex(models.Model):
        location_id = models.CharField(max_length=50)
        resource_id = models.CharField(max_length=50)

#        location_id = models.ForeignKey(Resource, blank=True, null=True)
#        resource_id = models.ForeignKey(Resource, blank=True, null=True)
#    location = models.ForeignKey(Location)


def __unicode__(self):
        return self.resource_id
    

# Create your models here.
