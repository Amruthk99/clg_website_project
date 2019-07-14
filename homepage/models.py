from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')

    #for naming the objects in Database
    #def __str__(self):
    #    return self.title
