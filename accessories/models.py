from django.db import models


class Accessory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    def __str__(self):
        return self.name
