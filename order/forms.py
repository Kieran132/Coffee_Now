from django import forms
from .models import CoffeeBean


class BeanForm(forms.ModelForm):

    class Meta:
        model = CoffeeBean
        fields = ['name', 'description', 'price', 'image', 'roasting_level', 'flavor_profile', 'strength_level']
