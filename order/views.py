from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CoffeeBean
from .forms import BeanForm


def coffee_list(request):
    """
    This allows for the page to be viewed by the user
    """
    coffee_beans = CoffeeBean.objects.all()
    return render(
        request, 'coffee_list.html', {'coffee_beans': coffee_beans})


def coffee_detail(request, id):
    """
    This takes the information from the form used and shows in more detail the
    profile of the coffee being viewed
    """
    coffee = get_object_or_404(CoffeeBean, pk=id)
    form = BeanForm()

    context = {
        'coffee': coffee,
        'form': form
    }
    return render(request, 'coffee_detail.html', context)


@login_required
def add_product(request):
    """
    This function only allows admin users to be able to add a product to the
    coffee product lise
    """
    form = BeanForm()
    if request.method == 'POST':
        form = BeanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('coffee_list')
        else:
            messages.error(request,
             'Error adding product. Please check if the form is valid.')
    return render(request, 'add_product.html', {'form': form})


@login_required
def edit_product(request, coffee_id):
    """
    This function only allows admin users to be able to edit a product to the
    coffee product lise
    """
    coffee = get_object_or_404(CoffeeBean, pk=coffee_id)
    form = BeanForm(instance=coffee)
    if request.method == 'POST':
        form = BeanForm(request.POST, request.FILES, instance=coffee)
        if form.is_valid():
            print("Form submitted")
            form.save()
            return redirect('coffee_list')
        else:
            messages.error(
                request,
                'Error adding product, please check the the form is valid')
    else:
        form = BeanForm(instance=coffee)
    
    context = {
        'form': form,
        'coffee': coffee
    }
       
    return render(request, 'edit_product.html', context)


@login_required
def delete_product(request, id):
    """
    This function only allows admin users to be able to delete a product from the
    coffee product lise
    """
    coffee_beans = CoffeeBean.objects.get(id=id)
    coffee_beans.delete()
    return redirect('coffee_list')