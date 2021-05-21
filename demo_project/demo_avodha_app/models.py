from django.db import models

# Create your models here.

class shop(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField(upload_to='images')
    desc = models.TextField()