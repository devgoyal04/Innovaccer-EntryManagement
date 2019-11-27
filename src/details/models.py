from django.db import models
from django.utils import timezone

class Visitor(models.Model):
    visitorName = models.CharField(max_length=50)
    visitorEmail = models.EmailField(max_length=60)
    visitorContactNo = models.CharField(max_length=13)
    hostName = models.CharField(max_length=50)
    hostEmail = models.EmailField(max_length=60)
    hostContactNo = models.CharField(max_length=13)
    checkIn = models.DateTimeField(default=timezone.now)
    checkOut = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.visitorName