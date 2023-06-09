from django.db import models


class CoffeeBean(models.Model):
    """
    This model incorporates Roasting level, strength level and flavor profile
    into one model of its own
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    roasting_level = models.ForeignKey(
        'RoastingLevel', on_delete=models.PROTECT)
    flavor_profile = models.ForeignKey(
        'FlavorProfile', on_delete=models.PROTECT)
    strength_level = models.ForeignKey(
        'StrengthLevel', on_delete=models.PROTECT, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class RoastingLevel(models.Model):
    """
    Model allows user to select Roast level
    """
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class FlavorProfile(models.Model):
    """
    Model allows user to select Flavor Profile
    """
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class StrengthLevel(models.Model):
    """
    Model allows user to select Strength level
    """
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
