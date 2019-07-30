from django.db import models

# Create your models here.
class  CSE(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    roll = models.CharField(max_length=64, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    areas_of_interest = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'CSE'



class  ECE(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    roll = models.CharField(max_length=64, blank=True, null=True)
    areas_of_interest = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=64, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'ECE'
