from django.db import models

# Create your models here.
class  Content_with_1_image(models.Model):
    image = models.ImageField(upload_to='images/')
    html = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Content with 1 Image'


class Content_with_2_image(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Content with 2 Image'


class Content_with_3_image(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Content with 3 Image'


class Photo(models.Model):
    image1 = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=64, blank=True, null=True)
    def __str__(self):
        return self.title
