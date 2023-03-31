from django.shortcuts import render
from .models import Accessory


def coffee_accessories(request):
    accessories = Accessory.objects.all()
    context = {'accessories': accessories}
    return render(request, 'coffee_accessories.html', context)

