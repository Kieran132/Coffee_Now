from django import forms
from .models import CoffeeBean


class BeanForm(forms.ModelForm):

    class Meta:
        model = CoffeeBean
        fields = ['name', 'description', 'price', 'image', 'roasting_level', 'flavor_profile', 'strength_level']

        #image = forms.ImageField(
        #    label='Image', required=False)

    #def __init__(self, *args, **kwargs):
    #super().__init__(*args, **kwargs)
