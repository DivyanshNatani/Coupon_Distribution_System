from django.db import models

# Create your models here.
class userDetail(models.Model):
    userID = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    userPost = models.CharField(max_length=30, choices=[('CG', 'CG'), ('Coordinator', 'Coordinator'), ('Organiser', 'Organiser')], default='CG')
    # userPost = models.TextChoices("userPost","CG Coordinator Organiser")
    # usr = models.TextChoices()
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=50, blank=True)
    mobNumber = models.IntegerField()

    objects=models.Manager()

    def __str__(self):
        return self.userID
    



