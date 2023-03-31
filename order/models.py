from django.db import models


class CoffeeBean(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='coffee_beans/')
    roasting_level = models.ForeignKey(
        'RoastingLevel', on_delete=models.PROTECT)
    flavor_profile = models.ForeignKey(
        'FlavorProfile', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class RoastingLevel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class FlavorProfile(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
