from django.db import models

# Create your models here.
class venderTable(models.Model):
    venderName=models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
    contectNumber = models.TextField(blank=True)

    objects=models.Manager()
    
    def __str__(self):
        return self.venderName

    