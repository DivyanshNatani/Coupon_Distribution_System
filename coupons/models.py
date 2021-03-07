from django.db import models

# Create your models here.
class couponsTable(models.Model):
    allotedTo = models.CharField(max_length=30)
    allocationStatus = models.CharField(max_length=30, choices=[('Using', 'Using'), ('Submitted', 'Submitted')], default='Using')
    # venderID =  models.CharField(max_length=30)
    venderName = models.CharField(max_length=30)
    venderStatus = models.CharField(max_length=30, choices=[('Recieved', 'Recieved'), ('Not Recieved', 'Not Recieved'), ('Processing','Processing')], default='Not Recieved')
    
    objects=models.Manager()

