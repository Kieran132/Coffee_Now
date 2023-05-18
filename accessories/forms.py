from django import forms
from .models import Accessory


class AccessoryForm(forms.ModelForm):

    """
    Form outlines the information required for the accessory products
    """
    class Meta:
        model = Accessory
        fields = ['name', 'description', 'image', 'price']
