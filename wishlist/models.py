from django.db import models
from django.contrib.auth.models import User
from order.models import CoffeeBean
from accessories.models import Accessory


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CoffeeBean = models.ForeignKey(
        CoffeeBean, on_delete=models.CASCADE, null=True, blank=True)
    Accessory = models.ForeignKey(
        Accessory, on_delete=models.CASCADE, null=True, blank=True)
