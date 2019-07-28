from django.db import models

# Create your models here.

class  CSE_Faculty(models.Model):
    name = models.CharField(max_length=20, help_text='Enter Name')
    designation = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(max_length=64, blank=True, null=True, help_text='Enter a working E-Mail address')
    number = models.CharField(max_length=64, blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    areas_of_interest = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    url = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        verbose_name_plural = "CSE Faculty"

    def __str__(self):
        return self.name
