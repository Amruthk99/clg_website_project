from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=64, blank=True, null=True)
    def __str__(self):
        return self.title


    #for naming the objects in Database
    #def __str__(self):
    #    return self.title
class Notification(models.Model):
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    def __str__(self):
        return self.title
class Event(models.Model):
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    def __str__(self):
        return self.title
