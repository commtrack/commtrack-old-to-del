from django.db import models
import datetime
#from hq.models import ExtUser



class AuditTrail(models.Model):
    user_id = models.IntegerField(max_length=11)
    action = models.CharField(max_length=200)
    audit = models.CharField(max_length=200)
    item_id = models.IntegerField(max_length=11)
    timestamp = models.DateTimeField(default=datetime.datetime.now())

def __unicode__(self):
        return self.actor

