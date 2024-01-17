from django.db import models
from django.contrib.auth.models import User
from order.models import CoffeeBean


class Wishlist(models.Model):
    """
    Model takes information from existing models
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CoffeeBean = models.ForeignKey(
        CoffeeBean, on_delete=models.CASCADE, null=True, blank=True)
