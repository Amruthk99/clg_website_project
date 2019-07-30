from django.db import models

# Create your models here.
class  CSE(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    roll = models.CharField(max_length=64, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=64, blank=True, null=True)
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_OF_JOINING_CHOICES = [
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2021', '2021'),
    ]
    year_of_joining = models.CharField(
        max_length=2,
        choices=YEAR_OF_JOINING_CHOICES,
        default=2017,
    )
    class Meta:
        verbose_name_plural = 'CSE'



    def __str__(self):
        return self.roll


class  ECE(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    roll = models.CharField(max_length=64, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=64, blank=True, null=True)
    def __str__(self):
        return self.roll
    class Meta:
        verbose_name_plural = 'ECE'
