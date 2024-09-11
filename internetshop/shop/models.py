from django.db import models


# Create your models here.
class Product(models.Model):
    description = models.TextField()
    price = models.IntegerField()
    image_url = models.CharField(max_length=1024)
