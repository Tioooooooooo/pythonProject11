from django.db import models
class Product(models.Model):
    description = models.TextField()
    price = models.IntegerField()
    image_url = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'