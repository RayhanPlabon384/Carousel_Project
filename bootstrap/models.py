from django.db import models

# Create your models here.
class Carousel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to = 'carousel/')

    def __str__(self):
        return self.title

class About(models.Model):
    heading = models.CharField(max_length=50)
    desc= models.TextField()
    img = models.ImageField(upload_to = 'About/')
    btn = models.TextField()

    def __str__(self):
        return self.heading

class Feature(models.Model):
    f_title = models.CharField(max_length=50)
    f_description = models.TextField()
    f_image = models.ImageField(upload_to = 'feature/')

    def __str__(self):
        return self.f_title

