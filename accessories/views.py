from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Accessory
from .forms import AccessoryForm


def coffee_accessories(request):
    accessories = Accessory.objects.all()
    context = {'accessories': accessories}
    return render(request, 'coffee_accessories.html', context)


@login_required
def add_product_b(request):
    form = AccessoryForm
    if request.method == 'POST':
        form = AccessoryForm(request.POST, request.FILES)
        print("errors in form", form.errors)
        if form.is_valid():
            print("Form submitted")
            form.save()
            return redirect('coffee_accessories')
        else:
            messages.error(
                request,
                'Error adding product, please check the the form is valid') 
    else:
        form = AccessoryForm()   
    return render(request, 'add_product_b.html', {'form': form})


@login_required
def edit_product_b(request, accessory_id):
    accessory = get_object_or_404(Accessory, pk=accessory_id)
    form = AccessoryForm(instance=accessory)
    if request.method == 'POST':
        form = AccessoryForm(request.POST, request.FILES, instance=accessory)
        if form.is_valid():
            print("Form submitted")
            form.save()
            return redirect('coffee_accessories')
        else:
            messages.error(
                request,
                'Error adding product, please check the the form is valid')
    else:
        form = AccessoryForm(instance=accessory)
    context = {
        'form': form,
        'accessory': accessory
    }  
    return render(request, 'edit_product_b.html', context)
