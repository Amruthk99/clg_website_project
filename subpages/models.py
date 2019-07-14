from django.db import models

# Create your models here.
class SubPageContent(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    
