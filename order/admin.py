from django.contrib import admin
from .models import CoffeeBean, RoastingLevel, FlavorProfile, StrengthLevel

admin.site.register(CoffeeBean)
admin.site.register(RoastingLevel)
admin.site.register(FlavorProfile)
admin.site.register(StrengthLevel)
