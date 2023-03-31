from django.shortcuts import render, get_object_or_404
from .models import CoffeeBean


def coffee_list(request):
    coffee_beans = CoffeeBean.objects.all()
    return render(
        request, 'coffee_list.html', {'coffee_beans': coffee_beans})


def coffee_detail(request, id):
    coffee = get_object_or_404(CoffeeBean, pk=id)
    return render(request, 'coffee_detail.html', {'coffee': coffee})
